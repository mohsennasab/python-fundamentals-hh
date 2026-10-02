"""Rebuild the Module 9 NAIP teaching crops and source manifest.

This script documents how the course fallback files in this folder were made.
Students do not need to run it. It needs internet access and the packages
pystac-client, planetary-computer, rasterio, geopandas, shapely, and pandas.

What it does, for each teaching year:
1. Searches the Microsoft Planetary Computer NAIP STAC collection for items
   that intersect the teaching AOI.
2. Keeps only items whose footprint fully covers the AOI (no mosaicking).
3. Reads the AOI window from the source Cloud Optimized GeoTIFF on its own
   pixel grid. No reprojection or resampling is applied.
4. Writes a compressed four-band GeoTIFF with an internal mask, band
   descriptions, and provenance tags. Signed URLs and tokens are never saved.
5. Appends one row per crop to naip_source_manifest.csv.

It also writes the Lesson 3 label files from the coordinates listed in
TRAINING_POLYGONS and VALIDATION_POINTS below. Those coordinates were placed
by visual interpretation of the 2022 crop at full resolution, then checked
with image chips and per-label band statistics. See DATA_PREPARATION.md.

Run from this data folder:
    python prepare_teaching_data.py              # crops, manifest, labels
    python prepare_teaching_data.py --labels     # labels only (no internet)
"""

import datetime
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import geopandas as gpd
import rasterio
from rasterio.windows import Window, from_bounds
from shapely.geometry import Point, Polygon, box, shape

# Teaching AOI, in NAD83 / UTM zone 13N meters (the NAIP source CRS here).
# It sits inside HUC-12 101900090108 (Town of South Greeley, Cheyenne, WY)
# and inside a single NAIP quarter-quad tile for every year used below.
AOI_CRS = 'EPSG:26913'
AOI_BOUNDS = (517750.0, 4549350.0, 518850.0, 4550900.0)  # W, S, E, N

YEARS = [2022, 2012]
STAC_URL = 'https://planetarycomputer.microsoft.com/api/stac/v1'
BAND_NAMES = ('Red', 'Green', 'Blue', 'Near infrared')
OUT_DIR = Path(__file__).resolve().parent

# Lesson 3 classes
CLASS_NAMES = {1: 'Vegetation', 2: 'Bare soil', 3: 'Built/paved', 4: 'Water'}
LABEL_IMAGE = 'naip_2022_teaching_aoi.tif (NAIP acquired 2022-06-21)'
REVIEW_STATUS = 'Draft - course author review required before teaching'

# Training polygons in EPSG:26913: (class_id, polygon, description)
TRAINING_POLYGONS = [
    (1, box(518180, 4550322, 518262, 4550425), 'Irrigated turf athletic field, campus'),
    (1, box(517900, 4550580, 518000, 4550760), 'Dry rangeland grass, field north of campus'),
    (1, box(518590, 4549930, 518730, 4550020), 'Darker rangeland grass and shrubs east of roundabout'),
    (1, box(518026, 4550400, 518040, 4550470), 'Dense tree row west of campus pond'),
    (2, box(518530, 4549760, 518640, 4549850), 'Graded construction ground, bright soil'),
    (2, box(518295, 4550612, 518345, 4550700), 'Graded soil and dark spoil pile north of campus'),
    (2, box(518010, 4550020, 518032, 4550068), 'Reddish bare soil pad beside new building'),
    (3, box(518405, 4550420, 518480, 4550490), 'Asphalt parking lot with cars'),
    (3, Polygon([(518326, 4550372), (518356, 4550372), (518356, 4550434),
                 (518362, 4550434), (518362, 4550457), (518318, 4550457),
                 (518318, 4550434), (518326, 4550434)]), 'Light roof, campus building'),
    (3, box(518690, 4550545, 518730, 4550625), 'Gray roof, large campus building'),
    (3, box(517770, 4550127, 517990, 4550136), 'Asphalt arterial road'),
    (3, box(518760, 4550240, 518820, 4550320), 'Light concrete parking lot with cars'),
    (4, Polygon([(518488, 4550705), (518535, 4550708), (518540, 4550730),
                 (518515, 4550752), (518488, 4550755)]), 'Open water, east lobe of north pond'),
]

# Independent validation points in EPSG:26913: (class_id, x, y, description)
# Every point is at least 30 m from every training polygon.
VALIDATION_POINTS = [
    (1, 517800, 4549600, 'Rangeland southwest'),
    (1, 517850, 4549480, 'Rangeland southwest'),
    (1, 517780, 4549700, 'Rangeland southwest'),
    (1, 517880, 4549870, 'Rangeland west of roundabout'),
    (1, 517960, 4549830, 'Rangeland west of roundabout'),
    (1, 518300, 4549790, 'Rangeland south of arterial'),
    (1, 518380, 4549800, 'Rangeland south of arterial'),
    (1, 517950, 4550850, 'Rangeland north field'),
    (1, 518395, 4550272, 'Campus lawn'),
    (1, 518790, 4550402, 'Campus lawn with trees'),
    (1, 518088, 4550360, 'Tree cluster south of campus pond'),
    (1, 518790, 4550090, 'Darker rangeland northeast of construction'),
    (2, 518720, 4549660, 'Graded construction ground'),
    (2, 518640, 4549700, 'Graded construction ground'),
    (2, 518820, 4549600, 'Graded construction ground'),
    (2, 518560, 4549690, 'Graded construction ground'),
    (2, 518612, 4549470, 'Graded lot inside new street loop'),
    (2, 518560, 4549500, 'Graded lot inside new street loop'),
    (2, 518660, 4549470, 'Graded lot inside new street loop'),
    (2, 518615, 4550698, 'Dirt access road north of campus'),
    (2, 518440, 4550670, 'Bright bare pad north of campus'),
    (2, 518465, 4550650, 'Bright bare pad north of campus'),
    (2, 518805, 4550655, 'Brown bare soil beside building'),
    (3, 518505, 4550375, 'Light roof, campus building'),
    (3, 518620, 4550350, 'Light roof, campus building'),
    (3, 518715, 4550370, 'Gray roof, campus building'),
    (3, 518835, 4550430, 'Light roof, campus building'),
    (3, 518558, 4550235, 'Asphalt parking lot'),
    (3, 518520, 4550440, 'Asphalt parking lot'),
    (3, 518515, 4550240, 'Asphalt parking lot'),
    (3, 518735, 4550455, 'Asphalt parking lot'),
    (3, 518170, 4550240, 'Asphalt parking lot'),
    (3, 518620, 4550575, 'Asphalt parking lot'),
    (3, 518320, 4550166, 'Campus loop road'),
    (3, 518453, 4549820, 'New north-south street'),
    (3, 517974, 4549650, 'Subdivision street'),
    (3, 518075, 4549505, 'Subdivision street'),
    (3, 518600, 4549414, 'New street, east subdivision'),
    (3, 518697, 4549480, 'New street, east subdivision'),
    (4, 518080, 4550450, 'Campus pond'),
    (4, 518095, 4550420, 'Campus pond'),
    (4, 518075, 4550410, 'Campus pond'),
    (4, 518100, 4550460, 'Campus pond'),
    (4, 518085, 4550435, 'Campus pond'),
    (4, 518440, 4550792, 'North pond, middle section'),
    (4, 518460, 4550778, 'North pond, middle section'),
    (4, 518365, 4550830, 'North pond, west arm'),
    (4, 518390, 4550827, 'North pond, west arm'),
]
MIN_SEPARATION_M = 30.0


def find_covering_item(catalog, year):
    """Return the one NAIP item of `year` whose footprint covers the AOI."""
    aoi = gpd.GeoSeries([box(*AOI_BOUNDS)], crs=AOI_CRS)
    aoi_lonlat = aoi.to_crs('EPSG:4326').total_bounds
    search = catalog.search(collections=['naip'], bbox=list(aoi_lonlat))
    covering = []
    for item in search.items():
        if int(item.properties['naip:year']) != year:
            continue
        footprint = gpd.GeoSeries([shape(item.geometry)], crs='EPSG:4326')
        if footprint.to_crs(AOI_CRS).iloc[0].covers(aoi.iloc[0]):
            covering.append(item)
    if len(covering) != 1:
        raise RuntimeError(
            f'{year}: expected exactly one covering item, found '
            f'{[i.id for i in covering]}'
        )
    return covering[0]


def write_crop(item, out_path):
    """Read the AOI window from the item's COG and write a teaching crop."""
    import planetary_computer
    signed_href = planetary_computer.sign(item.assets['image'].href)
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN='EMPTY_DIR'):
        with rasterio.open(signed_href) as src:
            if src.crs.to_string() != AOI_CRS:
                raise RuntimeError(f'Unexpected source CRS {src.crs}')
            if src.count < 4:
                raise RuntimeError('Source has fewer than four bands')
            window = from_bounds(*AOI_BOUNDS, transform=src.transform)
            # Expand to whole source pixels so no resampling is needed
            col0 = math.floor(window.col_off)
            row0 = math.floor(window.row_off)
            col1 = math.ceil(window.col_off + window.width)
            row1 = math.ceil(window.row_off + window.height)
            window = Window(col0, row0, col1 - col0, row1 - row0)
            if (col0 < 0 or row0 < 0 or col1 > src.width
                    or row1 > src.height):
                raise RuntimeError('AOI window extends beyond the source')
            data = src.read([1, 2, 3, 4], window=window)
            transform = src.window_transform(window)
            source_res = src.res

    valid = np.any(data != 0, axis=0)
    profile = {
        'driver': 'GTiff', 'count': 4, 'dtype': 'uint8',
        'width': data.shape[2], 'height': data.shape[1],
        'crs': AOI_CRS, 'transform': transform,
        'compress': 'deflate', 'predictor': 2, 'tiled': True,
        'blockxsize': 256, 'blockysize': 256, 'interleave': 'pixel',
    }
    with rasterio.Env(GDAL_TIFF_INTERNAL_MASK=True):
        with rasterio.open(out_path, 'w', **profile) as dst:
            dst.write(data)
            dst.write_mask(valid.astype('uint8') * 255)
            for i, name in enumerate(BAND_NAMES, start=1):
                dst.set_band_description(i, name)
            dst.update_tags(
                source_program='USDA National Agriculture Imagery Program',
                source_host='Microsoft Planetary Computer',
                stac_collection='naip',
                source_item_id=item.id,
                naip_year=item.properties['naip:year'],
                acquisition_date=item.datetime.date().isoformat(),
                source_gsd_m=str(item.properties['gsd']),
                source_epsg=str(item.properties['proj:epsg']),
                access_date=datetime.date.today().isoformat(),
                processing='AOI window read on the source pixel grid; '
                           'no reprojection or resampling',
                license='Public domain (USDA Farm Service Agency)',
            )
    return {
        'file': out_path.name,
        'naip_year': int(item.properties['naip:year']),
        'acquisition_date': item.datetime.date().isoformat(),
        'source_item_id': item.id,
        'source_gsd_m': item.properties['gsd'],
        'source_crs': AOI_CRS,
        'output_crs': AOI_CRS,
        'output_pixel_size_m': round(abs(source_res[0]), 3),
        'width': data.shape[2],
        'height': data.shape[1],
        'bands': 'Red|Green|Blue|Near infrared',
        'crop_bounds_requested': '|'.join(f'{v:.1f}' for v in AOI_BOUNDS),
        'crop_bounds_written': '|'.join(
            f'{v:.2f}' for v in rasterio.transform.array_bounds(
                data.shape[1], data.shape[2], transform)
        ),
        'valid_pixel_fraction': round(float(valid.mean()), 4),
        'resampling': 'none (source grid window)',
        'source_host': 'Microsoft Planetary Computer',
        'license': 'Public domain (USDA FSA)',
        'access_date': datetime.date.today().isoformat(),
    }


def write_labels():
    """Write the training polygons and validation points as GeoJSON."""
    today = datetime.date.today().isoformat()
    provenance = {'imagery': LABEL_IMAGE, 'method': 'Visual interpretation',
                  'review_status': REVIEW_STATUS, 'label_date': today}
    train = gpd.GeoDataFrame(
        [{'label_id': f'T{i:02d}', 'class_id': c, 'class_name': CLASS_NAMES[c],
          'description': d, **provenance}
         for i, (c, _, d) in enumerate(TRAINING_POLYGONS, start=1)],
        geometry=[g for _, g, _ in TRAINING_POLYGONS], crs=AOI_CRS)
    valid = gpd.GeoDataFrame(
        [{'point_id': f'V{i:02d}', 'class_id': c, 'class_name': CLASS_NAMES[c],
          'description': d, **provenance}
         for i, (c, _, _, d) in enumerate(VALIDATION_POINTS, start=1)],
        geometry=[Point(x, y) for _, x, y, _ in VALIDATION_POINTS], crs=AOI_CRS)

    # Independence check before anything is written
    distance = valid.geometry.distance(train.geometry.union_all())
    if (distance < MIN_SEPARATION_M).any():
        raise RuntimeError('A validation point is too close to training data')
    aoi = box(*AOI_BOUNDS)
    if not (train.within(aoi).all() and valid.within(aoi).all()):
        raise RuntimeError('A label falls outside the teaching AOI')

    # GeoJSON is written in longitude/latitude (EPSG:4326), per RFC 7946
    for gdf, name in [(train, 'naip_training_polygons.geojson'),
                      (valid, 'naip_validation_points.geojson')]:
        gdf.to_crs('EPSG:4326').to_file(OUT_DIR / name, driver='GeoJSON')
    print(f'Wrote {len(train)} training polygons and {len(valid)} validation '
          f'points (closest point to training: {distance.min():.1f} m)')


def main():
    if '--labels' in sys.argv:
        write_labels()
        return

    import pystac_client
    catalog = pystac_client.Client.open(STAC_URL)
    rows = []
    for year in YEARS:
        item = find_covering_item(catalog, year)
        out_path = OUT_DIR / f'naip_{year}_teaching_aoi.tif'
        row = write_crop(item, out_path)
        size_mb = out_path.stat().st_size / 1024 ** 2
        print(f'{year}: {item.id} -> {out_path.name} '
              f'({row["width"]} x {row["height"]}, {size_mb:.1f} MB)')
        rows.append(row)

    manifest = pd.DataFrame(rows)
    text = manifest.to_csv(index=False).lower()
    if any(marker in text for marker in ('sig=', 'se=', 'sv=', 'sp=')):
        raise RuntimeError('Token-like text found in the manifest')
    manifest.to_csv(OUT_DIR / 'naip_source_manifest.csv', index=False)
    print('Wrote naip_source_manifest.csv')
    write_labels()


if __name__ == '__main__':
    main()
