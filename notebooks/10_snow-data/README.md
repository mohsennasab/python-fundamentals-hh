# Module 10: Snow Data for Hydrologic and Hydraulic (H&H) Modeling

Level: Intermediate / Applied Hydrology and Hydraulics
Estimated Time: 4 to 5 hours across three notebooks (~1.5 hours per lesson)
Prerequisites: Modules 1 to 6 (`pandas`, `matplotlib`) and Modules 7 to 9 geospatial basics (`geopandas`, `rasterio`, Coordinate Reference Systems)
Study Area: Minnesota River Basin (USGS WBD HUC 4 `0702`, 44,050.3 km²) and its 12 HUC-8 subbasins (`07020001` to `07020012`) during WY2023 (`2022-11-01` to `2023-05-15`, 196 days)

---

## Overview

Module 10 covers downloading, inspecting, reprojecting, checking, analyzing, and mapping two CONUS gridded snow datasets: University of Arizona (UA) 800 m Daily SWE and Snow Depth (`DailyData_800m`) and NOAA/NOHRSC SNODAS 1 km Data Products (`G02158`).

Lesson 1 connects directly to USGS WBD REST endpoints, UA Apache directory indexes (`NetCDF4` CF variables with `float64` full-span coordinate math), and NSIDC raw big-endian `.dat.gz` and `.txt.gz` SNODAS archives (`>i2` pure Python without `osgeo.gdal`), saving cropped native-CRS GeoTIFF stacks with a `0.15°` geographic margin. Lessons 2 and 3 project those grids onto equal-area `EPSG:5070` (NAD83 / Conus Albers), produce watershed maps and time series, quantify snowmelt runoff, and cross-check `SNODAS - UA`.

---

## Lessons

| Lesson | Notebook | Google Colab | Key Concepts and Outputs |
|---|---|---|---|
| 10.1 | [`10_01_downloading_snow_data.ipynb`](10_01_downloading_snow_data.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/10_snow-data/10_01_downloading_snow_data.ipynb) | Live downloads from USGS WBD (`0702`), UA Apache index (`stable > provisional > early`), `float64` full-span NetCDF spacing fix preventing `float32` 1-col drift, `12:00 UTC` vs `06:00 UTC` timestamps, NSIDC `G02158_missing_files.txt` errata, pure-Python SNODAS `.tar` (`>i2` + `.txt`) reader, buffered `int16` GeoTIFF builders with optional 196-day builder |
| 10.2 | [`10_02_ua_snow_analysis_mapping.ipynb`](10_02_ua_snow_analysis_mapping.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/10_snow-data/10_02_ua_snow_analysis_mapping.ipynb) | UA `DailyData_800m` properties, `-999` water-mask handling, `EPSG:4269` pixel anisotropy across `0702`, buffer then `EPSG:5070` (`800 m`) reprojection then polygon mask, resampling tests (`nearest`, `bilinear`, `cubic`, `average`), 196-day HUC-4 and 12-HUC-8 SWE, depth, density, and volume summaries, Arial figures |
| 10.3 | [`10_03_snodas_snow_analysis_mapping.ipynb`](10_03_snodas_snow_analysis_mapping.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mohsennasab/python-fundamentals-hh/blob/main/notebooks/10_snow-data/10_03_snodas_snow_analysis_mapping.ipynb) | NOAA/NOHRSC SNODAS (`G02158`) `06:00 UTC` snapshot vs `06:00-06:00 UTC` melt flux, `2013-10-01` 5% grid shift alignment onto `EPSG:5070` (`1,000 m`), historical anomaly timeline (`2014 to 2019` Zero Repair Mask, outages), `100x` scale factors (`1034` vs `1044`), `1044` snow-free `-9999` land masking, `SNODAS - UA` comparison |

### File Locations and Data Loading in Google Colab

None of the notebooks download course files from GitHub.

- In Google Colab, the working folder is `/content/`. Click the **Files** folder icon on the left sidebar to browse `/content/data/` (input files) and `/content/module10_outputs/` (generated GeoTIFFs, CSVs, figures, and `.zip` archives).
- Start fresh in Lesson 1 ([`10_01_downloading_snow_data.ipynb`](10_01_downloading_snow_data.ipynb)) with zero pre-uploaded files to fetch WBD boundaries and live UA + SNODAS data from upstream servers. Set `USE_GOOGLE_DRIVE = True` across Lessons 1 to 3 to persist shared data in `/content/drive/MyDrive/module10_snow_data/`, or set `BUILD_FULL_SEASON = True` in Lesson 1 to build all 196 daily bands live.
- Each notebook includes an optional cell before the Practice sections that displays every saved file path, packages outputs into a `.zip` file (`lesson1_snow_data.zip`, `lesson2_ua_outputs.zip`, `lesson3_snodas_outputs.zip`), and downloads that `.zip` when `DOWNLOAD_OUTPUTS_ZIP = True`.
- Locally, keep the `data/` folder next to the notebooks (`./data/`), and all three lessons locate every file automatically.
- Running Lesson 2 or 3 standalone in Google Colab triggers one `files.upload()` prompt if files are absent in `/content/data/` or Google Drive, accepting individual files or a `.zip` archive.

---

## Learning Objectives

By completing Module 10, students will be able to:

1. Explain product inputs, time conventions, and limitations for UA 800 m (WY1982 to present, `12:00 UTC` PRISM day, SW-US lidar snow-depth ANN ratios) and SNODAS 1 km (Sep 30, 2003 to present, `06:00 UTC` snapshot and `06:00-06:00 UTC` 24-hour fluxes).
2. Automate live snow downloads safely in Lesson 1 by ranking UA status tiers (`stable > provisional > early`), computing NetCDF pixel spacing in `float64` across full coordinate vectors, checking NSIDC's `G02158_missing_files.txt` errata, and decoding raw SNODAS `.dat.gz` and `.txt.gz` files in Python (`tarfile`, `gzip`, `numpy`, `rasterio`) without `osgeo.gdal`.
3. Reproject `EPSG:4269` (NAD83) and `EPSG:4326` (WGS84) grids onto snapped equal-area `EPSG:5070` grids (`800 m` for UA, `1,000 m` for SNODAS), handling the `2013-10-01` SNODAS grid shift.
4. Choose `nearest`, `bilinear`, `cubic`, or `average` resampling using spring melt tests showing where `cubic` overshoot creates negative SWE and melt pixels along snow edges.
5. Diagnose and fix silent snow-data bugs in the Practice Debugging exercises (`provisional`/`stable` duplicates, `float32` grid drift and byte order, `-999` mask bleed and zero-snow filtering, geographic volume bias, missing-day `.fillna(0.0)` spikes, and `100x` scaling errors).
6. Export 300 dpi Arial watershed maps, dual-axis SWE/snow-depth/melt hydrographs, and multi-dataset comparison graphics.

---

## Verified WY2023 Minnesota River Basin (`0702`) Results

Across WY2023 (`2022-11-01` to `2023-05-15`, 196 days) over the `44,050.3 km²` Minnesota River HUC-4 watershed:

- UA 800 m (`EPSG:5070`, `800 m`, `bilinear`): Peak basin-mean SWE is `123.7 mm` (`4.87 in`, `5.450 km³` / `4,418 kAF`) on `2023-04-01`, with `478 mm` (`18.8 in`) mean snow depth. Highest HUC-8 subbasin Peak SWE is `Lower Minnesota (07020012)` at `171 mm` (`661 kAF`), and lowest is `Pomme De Terre (07020002)` at `94 mm` (`174 kAF`).
- SNODAS 1 km (`EPSG:5070`, `1,000 m`, `bilinear`): Peak basin-mean SWE is `117.4 mm` (`4.62 in`, `4,193 kAF`) on `2023-03-12`, peak 24-hour Snowmelt Runoff (`1044`) is `30.3 mm/day` on `2023-04-12`, and seasonal cumulative melt runoff is `125.7 mm`.
- Cross-Dataset Agreement (`EPSG:5070`, `1,000 m` common grid): 196-day HUC-4 basin-mean SWE correlation is `r = 0.9725`, snow-season mean bias (`SNODAS - UA`) is `+3.15 mm`, and `RMSE` is `11.00 mm`.

---

## Supporting Course Data (`data/`)

All GeoTIFF stacks are cropped to Minnesota River HUC 4 (`0702`) with a `0.15°` reprojection buffer and kept below 15 MB. See [`data/DATA_PREPARATION.md`](data/DATA_PREPARATION.md) for source URLs, byte sizes, and regeneration details in [`data/prepare_teaching_data.py`](data/prepare_teaching_data.py).

| File | Description | Size |
|---|---|---|
| `minnesota_river_wbd_0702.gpkg` | USGS WBD HUC-4 (`0702`) and 12 HUC-8 subbasins | 2.15 MB |
| `ua_800m_mn_river_wy2023_swe.tif` | 196-band UA 800 m SWE (`int16`, mm, `-999` NoData) | 7.24 MB |
| `ua_800m_mn_river_wy2023_depth.tif` | 196-band UA 800 m Snow Depth (`int16`, mm, `-999` NoData) | 14.54 MB |
| `ua_800m_mn_river_wy2023_manifest.csv` | Daily UA release status (`stable`), dates, and filenames | 16.9 KB |
| `ua_800m_mn_river_wy2023_basin_summary.csv` | Daily HUC-4 UA SWE, depth, and volume reference | 12.5 KB |
| `ua_800m_mn_river_wy2023_subbasin_summary.csv` | Daily 12 HUC-8 UA SWE and volume reference | 147.3 KB |
| `snodas_mn_river_wy2023_swe.tif` | 196-band SNODAS SWE `1034` (`int16`, mm, `-9999` NoData) | 12.16 MB |
| `snodas_mn_river_wy2023_melt.tif` | 196-band SNODAS Melt Runoff `1044` (`int16`, `0.01 mm/d`, `-9999` NoData) | 7.12 MB |
| `snodas_mn_river_wy2023_manifest.csv` | Daily SNODAS archive filenames and timestamps | 37.8 KB |
| `snodas_20130930_swe_subset.tif` | Pre-shift (`2013-09-30`) SNODAS subset across HUC `0702` | 10.9 KB |
| `snodas_20131001_swe_subset.tif` | Post-shift (`2013-10-01`) SNODAS subset across HUC `0702` | 8.2 KB |
| `snodas_2013_shift_headers.csv` | Parsed CONUS origin metadata comparing pre/post Oct 1, 2013 | 0.7 KB |

---

## Data Sources and Citations

- University of Arizona Snow Data (`DailyData_800m` and `NSIDC-0719`): Broxton, P., Zeng, X., and Dawson, N. (2019), `NSIDC-0719`, NASA NSIDC DAAC, [DOI: 10.5067/0GGPB220EX6A](https://doi.org/10.5067/0GGPB220EX6A), [User Guide PDF](https://nsidc.org/sites/default/files/nsidc-0719-v001-userguide.pdf). Zeng, X., Broxton, P., and Dawson, N. (2018), *Geophysical Research Letters*, 45(23). Broxton, P. D., Moeser, C. D., and Xiong, Z. (2024), served at [climate.arizona.edu/data/UA_SWE/DailyData_800m/](https://climate.arizona.edu/data/UA_SWE/DailyData_800m/) and documented in [Readme.txt](https://climate.arizona.edu/data/UA_SWE/Readme.txt).
- NOAA / NSIDC SNODAS (`G02158`): National Operational Hydrologic Remote Sensing Center (2004), [DOI: 10.7265/N5TB14TC](https://doi.org/10.7265/N5TB14TC), [Landing Page](https://nsidc.org/data/g02158/versions/1), [User Guide PDF](https://nsidc.org/sites/default/files/g02158-v001-userguide_2_1.pdf). Barrett, A. (2003), [NSIDC Special Report 11 PDF](https://nsidc.org/sites/default/files/nsidc_special_report_11.pdf). Archive and errata: [G02158/masked/](https://noaadata.apps.nsidc.org/NOAA/G02158/masked/), [G02158_missing_files.txt](https://noaadata.apps.nsidc.org/NOAA/G02158/G02158_missing_files.txt), [SNODAS_Zero_Repair_Mask.tif](https://noaadata.apps.nsidc.org/NOAA/G02158/ancillary/SNODAS_Zero_Repair_Mask.tif), and [NOHRSC NSA](https://www.nohrsc.noaa.gov/nsa/).
- Watershed Boundaries: U.S. Geological Survey Watershed Boundary Dataset (WBD), [usgs.gov/national-hydrography/watershed-boundary-dataset](https://www.usgs.gov/national-hydrography/watershed-boundary-dataset)
