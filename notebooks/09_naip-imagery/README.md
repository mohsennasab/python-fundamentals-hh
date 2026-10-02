# Module 9: NAIP Aerial Imagery for Watershed Visualization and Land Cover Classification

## Overview

This intermediate to advanced module teaches water resources engineers how to find, compare, and classify high-resolution aerial imagery from the National Agriculture Imagery Program (NAIP). NAIP is flown from aircraft, not collected by satellite, and covers the lower 48 states at roughly 0.6 to 1 meter resolution. The lessons use free, anonymous access through Microsoft Planetary Computer. Students do not need a cloud account, an API key, a GPU, or local GIS software.

The three core lessons follow one engineering question through a small teaching area inside the Town of South Greeley HUC-12 (`101900090108`) near Cheyenne, Wyoming, the same watershed used in Modules 3, 4, 5, and 8:

> What can high-resolution aerial imagery show about a watershed, what changed visually between acquisitions, and how cautiously can we turn imagery into a screening-level land cover map?

The teaching area includes a community college campus with two ponds, an athletic field, parking lots, a subdivision that was built between 2012 and 2022, and open rangeland.

## Lessons

| Lesson | Notebook | Question | Level | Status |
|---|---|---|---|---|
| 1 | `09_01_find_download_naip.ipynb` | How do I get a trustworthy, right-sized image for my area? | Intermediate | Available |
| 2 | `09_02_visualize_compare_naip.ipynb` | What changed between two acquisitions, and what only looks like it changed? | Intermediate | Available |
| 3 | `09_03_classify_naip_landcover.ipynb` | Can a small labeled sample produce a useful screening map, and where does it fail? | Advanced | Coming soon |
| Optional | `09_04_advanced_watershed_mosaic.ipynb` | How do I build a full-watershed mosaic from the raw web services? | Advanced | Coming soon |

Lesson 3 and the optional advanced notebook are written and tested but are still under review, so they are not published yet. The sections below describe the full module.

Each core lesson runs on its own in a fresh Colab session. If a lesson needs an earlier lesson's output and can't find it, it downloads the matching course copy and says so.

### Lesson 1: Find, Download, and Inspect NAIP Aerial Imagery

- Aerial versus satellite imagery; STAC items versus image assets
- Catalog search and an acquisition inventory with per-item AOI coverage
- Why "intersects" is not "covers"
- Download size planning before any transfer
- Signed, bounded window reads from a Cloud Optimized GeoTIFF, with no resampling
- A PASS/FAIL check of CRS, bounds, bands, pixel size, valid pixels, and provenance
- True-color and single-band views, including near infrared
- **Practice debugging:** a selection rule that picks the newest image and quietly returns a partial one

### Lesson 2: Visualize and Compare NAIP Acquisitions

- Metadata comparison before pixel comparison (June 2012 at 1 m versus June 2022 at 0.6 m)
- Band-order checks and true-color and color-infrared composites
- Resampling both years onto one verified 1 m grid, and why a shared map extent isn't enough
- NDVI as a within-image visual aid, and why its values don't transfer between acquisitions
- Fixed-patch comparison and an observation log that separates visible difference from confirmed change
- **Practice debugging:** an NDVI map with swapped red and NIR bands that looks convincing

### Lesson 3: Build and Check a Simple NAIP Land Cover Classification

- Supervised classification with four classes: vegetation, bare soil, built/paved, and water
- Reviewed training polygons and independent validation points, with an automated separation check
- Balanced, capped training samples and a CPU Random Forest
- Chunked prediction and a georeferenced class raster with a color table
- Confusion matrix, producer's and user's accuracy, and a confidence interval for overall accuracy
- Close inspection of every misclassified point, including a pond the model maps as pavement
- Class areas over valid pixels only, with Annual NLCD from Module 8 as context rather than truth
- **Practice debugging:** validation leakage that turns an 83 percent map into a "100 percent" one

### Optional: NAIP Mosaic for a Whole Watershed

The advanced notebook builds a clipped 2 m NAIP mosaic for one or more HUC-12 watersheds using raw STAC HTTP requests, server-side pagination, year-by-year footprint coverage, temporary access tokens, and remote window reads. It shows what `pystac-client` handles for you in Lessons 1 to 3. None of the core lessons depend on it.

## Data Source

NAIP imagery is produced by the USDA Farm Service Agency and is in the public domain. The lessons read it from the Microsoft Planetary Computer STAC catalog, which hosts four-band (red, green, blue, near infrared) Cloud Optimized GeoTIFFs. The catalog is publicly searchable; reading an image asset requires a short-lived token, which the `planetary-computer` package requests automatically. Tokens are never printed or saved.

Acquisitions covering the teaching area, as found in the catalog when the module was prepared:

| Year | Acquisition date | Source GSD | Item |
|---|---|---|---|
| 2022 | 2022-06-21 | 0.6 m | `wy_m_4110458_ne_13_060_20220621` |
| 2019 | 2019-08-24 | 0.6 m | `wy_m_4110458_ne_13_060_20190824_20191029` |
| 2017 | 2017-08-21 | 1.0 m | `wy_m_4110458_ne_13_1_20170821_20171006` |
| 2015 | 2015-06-20 | 0.5 m | `wy_m_4110458_ne_13_.5_20150620_20151021` |
| 2012 | 2012-06-23 | 1.0 m | `wy_m_4110458_ne_13_1_20120623_20121004` |

Every one of these items covers the whole teaching area by itself, so no mosaicking is needed in the core lessons. The notebooks verify coverage live rather than assuming it.

## Data Files

| File | Used in | Description |
|---|---|---|
| `NHD__Watershed_Boundaries_HUC_12_Selected.zip` | 1, Optional | Nineteen course HUC-12 watershed boundaries (same file as Modules 3 to 8) |
| `naip_2022_teaching_aoi.tif` | 1, 2, 3 | Course copy of the 2022 teaching crop, 0.6 m, four bands, EPSG:26913 |
| `naip_2012_teaching_aoi.tif` | 2 | Course copy of the 2012 teaching crop, 1.0 m, four bands, EPSG:26913 |
| `naip_source_manifest.csv` | Reference | Source item, date, GSD, grid, and access date for both crops |
| `naip_training_polygons.geojson` | 3 | 13 training polygons across four classes |
| `naip_validation_points.geojson` | 3 | 48 validation points, each at least 30 m from any training polygon |
| `prepare_teaching_data.py` | Reference | Script that rebuilt the crops, manifest, and label files |
| `DATA_PREPARATION.md` | Reference | How the crops and labels were made, and their review status |

Lesson 3 also reads `annual_nlcd_2025_land_cover.tif` from the Module 8 data folder for an optional context comparison.

## Source Order and Fallbacks

Each lesson uses the first source that works and prints which one it used:

1. A validated local file (an earlier lesson's output, or a cloned copy of this repository)
2. The live Planetary Computer service
3. The matching course copy in this repository's `data` folder

Lesson 1 tries the live service first, because the download is what it teaches. Every source passes the same checks. A fallback isn't accepted just because it exists.

### Rate Limits

The NAIP catalog is free and anonymous, so everyone using it shares one pool of capacity. When requests arrive too quickly it replies **HTTP 429, "too many requests"**. This is common in a classroom because Colab routes many users through a small set of outgoing addresses, so a group can reach the limit together without anyone misusing the service.

The notebooks handle this in four ways, and Lesson 1 Part 4 teaches why each one matters:

1. **Retry with exponential backoff.** `open_naip_catalog()` builds a session that retries 429 responses, waiting about 1, 2, 4, 8, then 16 seconds and honoring the server's `Retry-After` header. A rate-limited search cell can take up to a minute; that's the retry working, not a hang.
2. **Search once and cache.** Lesson 1 reuses a successful search if its cell is re-run. Lesson 2 searches once for both years, and remembers a *failure* too, so a rate limit doesn't trigger a second round of retries for the second year.
3. **A clear message.** A 429 is reported as a rate limit with guidance, never as a generic failure or a raw traceback.
4. **A fallback that isn't a downgrade.** The course copies came from the same NAIP items and pass the same validation, so a rate-limited session still completes every lesson.

Worth knowing: urllib3, which sits under `requests` and `pystac-client`, retries dropped connections but **not** HTTP status codes unless you list them. A default client passes a 429 straight through to your code.

## Outputs

All outputs are written to a `module9_outputs` folder.

| Lesson | Outputs |
|---|---|
| 1 | `naip_2022_teaching_aoi.tif`, `naip_source_inventory.csv`, `naip_2022_quicklook.png` |
| 2 | `naip_2012_aoi_1m_common.tif`, `naip_2022_aoi_1m_common.tif`, `naip_two_year_views.png`, `naip_patch_comparison.png`, `naip_comparison_metadata.csv`, `naip_observation_log.csv` |
| 3 | `naip_2022_landcover_screening.tif`, `naip_landcover_screening_map.png`, `naip_validation_results.csv`, `naip_confusion_matrix.csv`, `naip_landcover_class_area.csv`, `naip_classification_summary.txt` |

## Figures

Every figure uses Arial. Colab runs on Linux, which does not ship Arial, so each notebook sets a font preference list and falls back to Liberation Sans, a font drawn with the same letter widths and shapes. The setup cell prints which font is in use. Naming a font that exists also prevents matplotlib from logging a warning for every label it draws.

## Engineering QA/QC

The lessons check, before any interpretation:

- Single-item coverage of the AOI, in projected meters
- Download size against a limit
- Band count, data type, and band order
- CRS, bounds, pixel size versus source GSD, and valid-pixel fraction
- Provenance tags, and the absence of access tokens in every saved file
- Common-grid CRS, origin, pixel size, and dimensions before any pixel comparison
- Label class codes, geometry types, extent, and training-to-validation separation
- Class raster grid and codes against the source image
- Class-area totals against the valid-pixel count

## Engineering Limitations

- NAIP pixel values are 8-bit and adjusted for appearance. They aren't calibrated reflectance, so NDVI and raw values don't compare directly across years.
- Horizontal positions can differ by a meter or two between acquisitions. Edge shifts of that size are not evidence of change.
- A visual two-date comparison is qualitative. Numeric change needs consistent, separately validated classifications for both years.
- The Lesson 3 map is a screening product. Built/paved is a visual cover class, not percent impervious or connected impervious area, and not a curve number or roughness map.
- The classifier was trained and validated on one acquisition. It shouldn't be applied to another year without new labels and validation.
- Forty-eight validation points support finding failures, not a precise accuracy claim.

## Getting Started

1. Open `09_01_find_download_naip.ipynb` in Google Colab.
2. Run the notebook from the top. The watershed file and imagery are fetched automatically.
3. Read the printed source line for each file and confirm every QA/QC check passes before interpreting results.
4. Continue with Lessons 2 and 3 in any session. Each one gets its own inputs.

## Troubleshooting

| Issue | What to check |
|---|---|
| "You have exceeded a rate limit" (HTTP 429) | Expected on a free shared service, especially from Colab's shared addresses. The notebooks wait and retry automatically, then use the identical course copy. Nothing to fix; rerun in a minute for the live path |
| Catalog search or image read fails | Usually a temporary service problem. The notebook falls back to the course copy and says so |
| A local file is rejected | It failed validation (wrong year, extent, or bands). Delete it from `module9_outputs` and rerun |
| Exercise needs another NAIP year | The course copies only include 2012 and 2022; other years need the live service |
| Colors look wrong in a composite | Check band descriptions; NAIP is Red, Green, Blue, Near infrared |
| Classification accuracy differs from the lesson text | Package versions can shift results slightly; compare the confusion-matrix pattern |
| NLCD comparison is skipped | The Module 8 file couldn't be downloaded; the rest of Lesson 3 is unaffected |

## Official Resources and References

- [NAIP on Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/dataset/naip)
- [Planetary Computer: reading data from the STAC API](https://planetarycomputer.microsoft.com/docs/quickstarts/reading-stac/)
- [Planetary Computer: access tokens](https://planetarycomputer.microsoft.com/docs/concepts/sas/)
- [USDA FSA NAIP imagery program](https://www.fsa.usda.gov/programs-and-services/aerial-photography/imagery-programs/naip-imagery/)
- [Earth Data Science: NAIP multiband imagery in Python](https://earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-naip/)
- [GeoAI: download NAIP imagery](https://opengeoai.org/examples/download_naip/)
- [GeoAI: data visualization](https://opengeoai.org/examples/data_visualization/)
- [GeoAI: classification API](https://opengeoai.org/classify/)
- [GeoAI: train a land cover classification model](https://opengeoai.org/examples/train_landcover_classification/)
- [GeoAI: AutoGeoModel examples](https://opengeoai.org/examples/AutoModel/)
