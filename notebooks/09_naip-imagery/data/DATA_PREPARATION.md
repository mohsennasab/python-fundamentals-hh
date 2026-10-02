# Module 9 Data Preparation

This note records how the Module 9 course data were prepared, so the files can be reviewed, reproduced, or replaced. The script `prepare_teaching_data.py` in this folder rebuilds everything except the watershed ZIP.

## Teaching AOI

| Property | Value |
|---|---|
| Bounds (W, S, E, N) | 517750, 4549350, 518850, 4550900 |
| CRS | EPSG:26913, NAD83 / UTM zone 13N (the NAIP source CRS here) |
| Size | 1,100 m x 1,550 m, about 1.7 km² (421 acres) |
| Watershed | Entirely inside HUC-12 `101900090108`, Town of South Greeley, Cheyenne, WY |
| NAIP tile | Quarter quad `4110458_ne` for every year from 2012 to 2022 |

The AOI was chosen after a catalog check of the whole watershed (Gate A in the development plan):

- Five NAIP years intersect the watershed on Planetary Computer: 2012, 2015, 2017, 2019, and 2022. All are four-band.
- One item from each year fully covers the AOI, so the core lessons need no mosaicking.
- 2012 and 2022 were selected for comparison: both were flown in late June (June 23 and June 21), ten years apart, at different GSDs (1.0 m and 0.6 m).
- The AOI contains interpretable examples of all four Lesson 3 classes: irrigated turf, trees, and dry rangeland; graded construction soil; roofs, asphalt, and concrete; and two ponds.
- Image matching over the campus put the registration offset between the 2012 and 2022 images at about 1 to 2 m.

## Imagery Crops

| File | Year | Acquired | Source item | GSD | Size |
|---|---|---|---|---|---|
| `naip_2022_teaching_aoi.tif` | 2022 | 2022-06-21 | `wy_m_4110458_ne_13_060_20220621` | 0.6 m | 1,834 x 2,584 |
| `naip_2012_teaching_aoi.tif` | 2012 | 2012-06-23 | `wy_m_4110458_ne_13_1_20120623_20121004` | 1.0 m | 1,100 x 1,550 |

Processing:

1. Search the Planetary Computer `naip` collection with the AOI bounding box.
2. Keep the item for the target year whose footprint covers the AOI in projected meters.
3. Sign the image asset in memory and read the AOI window, rounded outward to whole source pixels. No reprojection or resampling is applied, so pixel values are the source values. The 2022 crop extends 0.4 m past the AOI on the west and north edges because of that rounding.
4. Write a four-band `uint8` GeoTIFF (deflate, predictor 2, 256-pixel tiles) with an internal valid-data mask, band descriptions `Red, Green, Blue, Near infrared`, and tags for source item, year, acquisition date, GSD, source EPSG, access date, processing, and license.
5. Record each crop in `naip_source_manifest.csv`. Both the manifest and the tags are checked for token-like strings before saving. No signed URL or token is stored anywhere.

Lesson 1 writes its own 2022 crop with the same code, so the live and fallback paths produce the same file layout and pass the same checks.

**License:** NAIP imagery is public domain (USDA Farm Service Agency). The Planetary Computer catalog lists the FSA as producer and licensor.

## Lesson 3 Labels

### Class Definitions

| Code | Class | Includes | Excluded from training |
|---|---|---|---|
| 1 | Vegetation | Irrigated turf, dry rangeland grass, shrubs, trees | Tree shadows, mixed lawn and roof edges |
| 2 | Bare soil | Graded construction ground, dirt roads, exposed soil pads | Areas with partial regrowth |
| 3 | Built/paved | Roofs, asphalt, concrete, parked vehicles | Sidewalk edges and roof overhangs next to lawns |
| 4 | Water | Open water in ponds | Shoreline pixels, shaded water edges |

Built/paved is a visual land cover class. It is not a measurement of impervious or connected impervious area.

### How the Labels Were Made

- **Imagery:** the 2022 crop only, viewed at full 0.6 m resolution in 350 m panels with a 25 m coordinate grid, plus 10 m-grid zooms around ponds, roofs, and streets.
- **Training polygons (13):** drawn in the interior of clearly identifiable, homogeneous areas, inset several meters from edges. Class totals are about 40,000 m² vegetation, 15,400 m² bare soil, 18,100 m² built/paved, and 2,100 m² water.
- **Validation points (48):** 12 vegetation, 11 bare soil, 16 built/paved, and 9 water. Every point is at least 30 m from every training polygon; the closest is 35 m. The script enforces this before writing.
- **Checks:** every validation point was reviewed in a 20 m and a 40 m image chip, and per-label band statistics were compared for outliers. Eight points were moved during that review because they sat on a sidewalk, curb, lawn strip, or the wrong surface, and two street points were added. One training polygon (the light campus roof) was redrawn after its NDVI spread showed it included a sidewalk and lawn.
- **Water design:** the only water training polygon is in the east lobe of the north pond. Water validation points are in the middle and west arm of the north pond and in the separate campus pond. This is deliberate: in testing, the campus pond was misclassified as built/paved, which gives Lesson 3 a real failure to investigate.
- **Storage:** GeoJSON in EPSG:4326 per RFC 7946. The label coordinates in EPSG:26913 are listed in `prepare_teaching_data.py`.

### Review Status

Each label carries `review_status = "Draft - course author review required before teaching"`. The labels were drafted with AI assistance during module development and checked as described above, but they haven't yet had an independent review by the course author. After reviewing them against the imagery, update `REVIEW_STATUS` in the script and rerun `python prepare_teaching_data.py --labels`.

### Results When the Module Was Prepared

scikit-learn 1.8.0, seed 42, 100 trees, 2,000 pixels per class, four bands:

| Class | Validation points | Producer's accuracy | User's accuracy |
|---|---|---|---|
| Vegetation | 12 | 0.83 | 0.91 |
| Bare soil | 11 | 0.91 | 0.83 |
| Built/paved | 16 | 1.00 | 0.76 |
| Water | 9 | 0.44 | 1.00 |

Overall accuracy was 40 of 48 (83.3 percent; 95 percent Wilson interval 70 to 91 percent). All five campus pond points were mapped as built/paved. Adding NDVI as a fifth feature (Lesson 3, Exercise 1) raised the independent score to 44 of 48 (91.7 percent), mostly by fixing campus pond points. The core lesson keeps four bands so the failure stays visible. A random 70/30 split of training pixels scored about 99 percent, and training on the validation points as well (the Lesson 3 bug) reported 100 percent.

## Rebuilding

```bash
cd notebooks/09_naip-imagery/data
python prepare_teaching_data.py            # crops, manifest, and labels (needs internet)
python prepare_teaching_data.py --labels   # labels only
```

Rebuilding the crops refreshes `access_date`. The pixel values should be identical as long as Planetary Computer serves the same items.
