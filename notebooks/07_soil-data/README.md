<p align="center">
  <img src="../../figures/Logo_pixel.png" alt="Course Logo" width="100">
</p>

# Module 7: Soil Data for H&H Modeling

## Overview

This module introduces two ways to use official NRCS soil data in Python. Lesson 1 queries SSURGO polygons and relational tables through Soil Data Access. Lesson 2 uses the gridded National Soil Survey Geographic Database, called gNATSGO, through Microsoft Planetary Computer.

Both lessons use the same HUC-12 watershed. This makes it easier to compare a detailed survey workflow with a gridded workflow that is convenient for raster analysis. The lessons keep the engineering questions in view: What part of the watershed has valid data? How was a soil property aggregated? Are the units and depth interval clear? Is the result suitable for screening, or does it need field evidence and calibration?

## Learning Objectives

By the end of this module, you will be able to:

- Explain how map units, components, and horizons organize SSURGO soil data
- Query SSURGO point and watershed data with the Soil Data Access service
- Search a STAC catalog for a gNATSGO raster tile
- Sample and clip cloud-hosted soil rasters
- Join a gNATSGO `mukey` raster to its map-unit attribute table
- Calculate raster cell area from geospatial metadata
- Check spatial coverage, valid area, table joins, units, and data vintage
- Summarize hydrologic soil group by watershed area
- Interpret available water storage without treating it as Ksat
- Export traceable, model-ready soil summaries

## Lessons

### Lesson 1: Soil Data for H&H Modeling with NRCS SSURGO

Notebook: `07_01_soil_data_ssurgo.ipynb`

- Learn the SSURGO map unit, component, and horizon hierarchy
- Build raw Soil Data Access requests and inspect API responses
- Query soil properties at a point and across a watershed
- Calculate depth-weighted and component-weighted Ksat
- Review represented component percentage before using a weighted result
- Map dominant-condition hydrologic soil groups
- Export tables, a GeoPackage, and a zipped shapefile

### Lesson 2: Gridded Soil Data with gNATSGO

Notebook: `07_02_soil_data_gnatsgo.ipynb`

- Relate the gNATSGO map-unit grid to the soil tables used in Lesson 1
- Find the watershed's raster tile with the Planetary Computer STAC catalog
- Sample `mukey` and available water storage at a point
- Clip cloud-optimized GeoTIFFs to the watershed
- Compute cell area from the raster affine transform
- Check valid raster coverage and map-unit table coverage
- Summarize HSG categories by valid grid area, including dual groups
- Summarize available water storage over the 0 to 100 cm depth interval
- Record the archived dataset snapshot and current NRCS citation separately

## Prerequisites

- Completion of Module 1 for Python fundamentals and Colab setup
- Completion of Module 3 for vector data, coordinate reference systems, and GeoPandas
- Module 5 is helpful API background, but Lesson 1 explains the needed concepts
- A Google account for Colab access

## Data Files

| File | Description |
|------|-------------|
| `NHD__Watershed_Boundaries_HUC_12_Selected.zip` | The Wyoming HUC-12 watershed boundaries used in both lessons |
| `sda_fallback_point_response.csv` | A saved Lesson 1 point result for times when the live SDA service is unavailable |
| `sda_fallback_watershed_response.csv` | A saved Lesson 1 watershed result for times when the live SDA service is unavailable |

Lesson 1 retrieves live soil data from Soil Data Access and can use the local fallback CSVs. Lesson 2 reads an archived gNATSGO raster and table snapshot from Microsoft Planetary Computer. Neither lesson stores credentials or signed cloud URLs in its outputs.

## Getting Started

1. Download `NHD__Watershed_Boundaries_HUC_12_Selected.zip` from this folder.
2. Open either lesson notebook in Google Colab.
3. Run the notebook from the top and upload the watershed ZIP when prompted.
4. Read each QA/QC result before moving to the interpretation cells.
5. Complete the exercises near the end of the notebook.

Start with Lesson 1 if map units, components, and horizons are new to you. Then use Lesson 2 to see how the same map-unit key supports a raster workflow.

## Choosing a Workflow

| Question | SSURGO lesson | gNATSGO lesson |
|---|---|---|
| Data structure | Polygons and relational tables | Raster map-unit keys and related tables |
| Access method | Soil Data Access API and WFS | STAC, cloud GeoTIFFs, and Parquet |
| Best course example | Component and horizon aggregation | Grid clipping and area summaries |
| Ksat method | Depth-weighted and component-weighted calculation | Not calculated from AWS or HSG |
| Coverage check | Polygon and represented component coverage | Valid raster area and table-key coverage |
| Data vintage | Current service response | Planetary Computer July 2020 snapshot |

## Engineering Interpretation

- Always state how a soil value was aggregated and which depth interval it represents.
- Treat Ksat as a starting estimate for infiltration modeling, not a calibrated final parameter.
- Keep dual HSG groups such as `C/D` explicit until drainage conditions are confirmed.
- Do not substitute available water storage or HSG for measured or properly aggregated Ksat.
- Compare valid data area with watershed area before reporting a watershed statistic.
- Check data vintage. The Planetary Computer lesson is reproducible, but its archived snapshot is not the latest annual NRCS release.
- Soil survey data supports screening and parameter development. It does not replace project-specific field investigation.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| SDA returns an empty table | Confirm that the point or watershed is mapped and inspect the SQL table and column names |
| A point returns the wrong map unit | Use WKT order `POINT(longitude latitude)` |
| A watershed SDA query times out | Increase polygon simplification carefully and confirm that the simplified geometry remains representative |
| A SSURGO map does not align | Inspect WFS axis order and compare returned bounds with the watershed |
| No gNATSGO tile is found | Confirm the watershed CRS and its longitude and latitude bounds before the STAC search |
| gNATSGO coverage is below 98 percent | Inspect NoData, CRS, tile bounds, and clipping geometry |
| A raster map unit has no table record | Keep it visible in the QA/QC result and do not assign an attribute by assumption |
| A cloud request fails | Rerun the cell after a short wait and confirm that the notebook can reach Planetary Computer |

## Resources

- [NRCS Soil Data Access](https://sdmdataaccess.sc.egov.usda.gov/)
- [NRCS Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/)
- [NRCS SSURGO Portal](https://www.nrcs.usda.gov/resources/data-and-reports/ssurgo-portal)
- [NRCS gNATSGO](https://www.nrcs.usda.gov/resources/data-and-reports/gridded-national-soil-survey-geographic-database-gnatsgo)
- [Microsoft Planetary Computer gNATSGO rasters](https://planetarycomputer.microsoft.com/dataset/gnatsgo-rasters)
- [Planetary Computer STAC documentation](https://planetarycomputer.microsoft.com/docs/quickstarts/reading-stac/)
- [Planetary Computer tabular data documentation](https://planetarycomputer.microsoft.com/docs/quickstarts/reading-tabular-data/)

## Next Steps

Combine the HSG results with land-cover data from Module 8 when developing screening-level curve number inputs. For project work, compare the two soil workflows, document material differences, and use the most current source that fits the analysis scale.
