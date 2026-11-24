# Module 10 Data Preparation Guide

All data files in this directory (`notebooks/10_snow-data/data/`) are **public-domain U.S. government or academic open datasets** cropped to the **Minnesota River Basin (USGS WBD HUC 4 `0702`)** plus a **`0.15°` spatial buffer** (~12–17 km) so reprojection edge kernels retain full neighbor support during `bilinear` and `cubic` resampling in Lessons 2 and 3.

Every multi-band GeoTIFF is stored in **lossless DEFLATE-compressed `int16` native values** with original NoData flags preserved (`-999` for UA 800 m, `-9999` for SNODAS) and kept under **15 MB** for easy local storage, fast Google Colab `files.upload()` / `.zip` upload, Google Drive sharing across Lessons 1–3, or on-demand generation via Lesson 1 (`BUILD_FULL_SEASON = True`).

---

## Reproducing the Teaching Datasets

The entire dataset was generated from public server endpoints via:

```bash
python prepare_teaching_data.py
```

The script requires standard open-source Python packages (`requests`, `geopandas`, `rasterio`, `rioxarray`, `xarray`, `netCDF4`, `numpy`, `pandas`, `shapely`, `pyproj`) and contains **zero credentials, API keys, tokens, or local machine paths**.

---

## Upstream Data Sources

| Dataset | Upstream Source URL | Spatial Grid & Window |
|---|---|---|
| **USGS WBD HUC 4 & HUC 8** | `https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer/` (`layers 2 & 4`) | `EPSG:4326` vector polygons for `huc4 = '0702'` and `huc8 LIKE '0702%'` |
| **UA 800 m Daily SWE & Depth** | `https://climate.arizona.edu/data/UA_SWE/DailyData_800m/WY2023/` | `EPSG:4269` (`0.00833333°`), `WY2023` (`2022-11-01` to `2023-05-15`, 196 days) |
| **SNODAS Daily Masked Archives** | `https://noaadata.apps.nsidc.org/NOAA/G02158/masked/` | `EPSG:4326` (`0.00833333°`), products `1034` (SWE) and `1044` (24-hr Melt Runoff) |
| **SNODAS 2013 Grid-Shift Pair** | `.../masked/2013/09_Sep/SNODAS_20130930.tar` & `.../10_Oct/SNODAS_20131001.tar` | Pre- (`-124.73375°`, `52.87458333°`) vs. post-shift (`-124.73333333°`, `52.875°`) origin test |

---

## File Inventory

| Filename | Format | Exact Content & Physical Units | Size |
|---|---|---|---|
| `prepare_teaching_data.py` | Python script | Reproducible dataset builder & verifier (WY2023 + 2013 shift) | 26.3 KB |
| `minnesota_river_wbd_0702.gpkg` | GeoPackage | Layers `huc04` (1 polygon, `44,050.3 km²`) and `huc08` (12 subbasins) | 2.15 MB (`2,146,304` B) |
| `ua_800m_mn_river_wy2023_swe.tif` | GeoTIFF | 196 bands (`2022-11-01`..`2023-05-15`), `int16`, mm SWE, `nodata=-999` | 7.24 MB (`7,236,537` B) |
| `ua_800m_mn_river_wy2023_depth.tif` | GeoTIFF | 196 bands, `int16`, mm snow depth, `nodata=-999` | 14.54 MB (`14,542,821` B) |
| `ua_800m_mn_river_wy2023_manifest.csv` | CSV | 196 daily rows with UA filename, maturity status (`stable`), URL | 16.9 KB (`17,263` B) |
| `ua_800m_mn_river_wy2023_basin_summary.csv` | CSV | Daily HUC-4 reference time series in `EPSG:5070` (800 m `bilinear`) | 12.5 KB (`12,758` B) |
| `ua_800m_mn_river_wy2023_subbasin_summary.csv` | CSV | Daily 12-HUC-8 subbasin UA reference table (`2,352` rows) | 147.3 KB (`150,849` B) |
| `snodas_mn_river_wy2023_swe.tif` | GeoTIFF | 196 bands (`1034`), `int16`, `scale=1.0 mm`, `nodata=-9999` | 12.16 MB (`12,162,127` B) |
| `snodas_mn_river_wy2023_melt.tif` | GeoTIFF | 196 bands (`1044`), `int16`, `scale=0.01 mm/day`, `nodata=-9999` | 7.12 MB (`7,123,484` B) |
| `snodas_mn_river_wy2023_manifest.csv` | CSV | 196 daily `.tar` archive filenames & source dates | 37.8 KB (`38,757` B) |
| `snodas_20130930_swe_subset.tif` | GeoTIFF | Pre-Oct 1, 2013 SWE subset (`EPSG:4326`, `-124.73375°` origin family) | 10.9 KB (`11,205` B) |
| `snodas_20131001_swe_subset.tif` | GeoTIFF | Post-Oct 1, 2013 SWE subset (`EPSG:4326`, `-124.73333333°` origin family) | 8.2 KB (`8,384` B) |
| `snodas_2013_shift_headers.csv` | CSV | Bounds & header float truncation comparison for `2013-09-30` vs `2013-10-01` | 0.7 KB (`731` B) |
