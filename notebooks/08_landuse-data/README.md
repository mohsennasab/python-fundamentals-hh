# Module 8: Annual NLCD Land Cover and Impervious Surface

## Overview

This intermediate module teaches water resources engineers how to retrieve and analyze Annual National Land Cover Database data for watershed hydrology. The lesson uses free, anonymous USGS web services. Students do not need an AWS account, billing information, or an API key.

The workflow separates three products that answer different questions:

- Annual NLCD Land Cover is categorical and is summarized by class area.
- Annual NLCD Fractional Impervious Surface is continuous from 0 to 100 percent and is summarized by area weighting.
- Annual NLCD Impervious Descriptor is categorical and separates roads from urban or other built surfaces.

The example compares 2001 with 2025 using Annual NLCD Collection 1.2. Both years come from one consistent annual product series.

## Learning Objectives

After completing the lesson, students will be able to:

- Explain the difference between categorical and continuous rasters.
- Discover the years available from the Annual NLCD service.
- Retrieve watershed-sized Annual NLCD GeoTIFFs without a paid account.
- Validate WCS responses as real rasters before using them.
- Check CRS, resolution, affine transform, NoData, value range, grid alignment, and valid area.
- Summarize land cover by area and percent.
- Calculate watershed-average fractional imperviousness and equivalent impervious area.
- Summarize descriptor classes using impervious-area weighting.
- Compare two Annual NLCD years without mixing product families.
- Export traceable tables and clipped rasters.

## Lesson

**Lesson 1: Annual NLCD Land Cover and Impervious Surface**

- Mental models for land cover, land use, categorical rasters, and continuous rasters
- Annual NLCD Collection 1.2 source, citation, and limitations
- Free year-specific access through the USGS EROS Web Coverage Service
- Local-first course fallbacks for reliable classroom use
- Native 30 meter EPSG:5070 grid alignment
- Response validation and tiled downloads
- Current land cover summary
- Fractional impervious NoData investigation
- Impervious descriptor summary weighted by impervious area
- Annual change analysis from 2001 to 2025
- Traceable CSV and GeoTIFF exports

## Data Source

Annual NLCD Collection 1.2 provides six annual raster products for the conterminous United States from 1985 through 2025:

1. Land Cover
2. Land Cover Change
3. Land Cover Confidence
4. Fractional Impervious Surface
5. Impervious Descriptor
6. Spectral Change Day of Year

The products use 30 meter cells in EPSG:5070. The lesson uses Land Cover, Fractional Impervious Surface, and Impervious Descriptor.

Official citation:

> U.S. Geological Survey, 2024, Annual National Land Cover Database Collection 1 Science Products: U.S. Geological Survey data release, https://doi.org/10.5066/P94UXNTS.

Annual NLCD is public-domain USGS data. The notebook requests small watershed-sized GeoTIFFs from the time-enabled USGS EROS WCS that supports the official MRLC services.

## Free Retrieval Method

1. Use WCS 2.0.1 `DescribeCoverage` to discover the available years.
2. Use WCS 1.0.0 `GetCoverage` with a `TIME` value for raster retrieval.
3. Request data in native EPSG:5070.
4. Snap bounds to the source grid, whose cell edges follow `15 + 30n`.
5. Split large requests into tiles of no more than 1,024 cells per side.
6. Open every response in memory with Rasterio.
7. Verify band count, CRS, shape, 30 meter resolution, NoData, and product value range.
8. Assemble tiles using their georeferencing.

The notebook uses sources in this order:

1. A validated local file, when the repository has been cloned.
2. The live anonymous USGS WCS.
3. The validated copy in the course GitHub repository.

This order keeps local course runs fast while allowing other CONUS watersheds and years to be retrieved directly from USGS.

## Data Files

| File | Description |
|---|---|
| `NHD__Watershed_Boundaries_HUC_12_Selected.zip` | Nineteen course HUC-12 watershed boundaries |
| `annual_nlcd_2001_land_cover.tif` | Annual NLCD 2001 Land Cover fallback |
| `annual_nlcd_2025_land_cover.tif` | Annual NLCD 2025 Land Cover fallback |
| `annual_nlcd_2001_impervious.tif` | Annual NLCD 2001 Fractional Impervious Surface fallback |
| `annual_nlcd_2025_impervious.tif` | Annual NLCD 2025 Fractional Impervious Surface fallback |
| `annual_nlcd_2025_impervious_descriptor.tif` | Annual NLCD 2025 Impervious Descriptor fallback |

The five raster fallbacks cover the full extent of the 19-watershed course file plus a 500 meter buffer. They were requested from the official USGS WCS, aligned to the native grid, validated, and saved as compressed GeoTIFFs.

## NoData and Valid Values

Annual NLCD Collection 1.2 uses 250 as the background value for the three products in this lesson.

| Product | Valid values | Background |
|---|---|---|
| Land Cover | Modified Anderson class codes 11 through 95 | 250 |
| Fractional Impervious Surface | 0 through 100 percent | 250 |
| Impervious Descriptor | 0 non-urban, 1 roads, 2 urban | 250 |

Zero is a valid fractional impervious value. Excluding zero removes rural and undeveloped cells from the denominator and can severely overstate mean watershed imperviousness.

## Engineering QA/QC

The lesson checks:

- Watershed CRS before requesting data.
- Live year availability.
- Raster band count, CRS, dimensions, and resolution.
- Annual NLCD NoData and allowed value ranges.
- Raster coverage of the requested bounds.
- Land cover and impervious grid alignment.
- Descriptor and impervious grid alignment.
- Valid raster area against polygon area.
- Valid area consistency between analysis years.
- Descriptor-weighted impervious area against the watershed total.

These checks occur before engineering interpretation.

## Engineering Limitations

- Thirty-meter data support watershed and regional screening, not parcel-scale design.
- Annual NLCD fractional imperviousness is not directly connected impervious area.
- Land cover and descriptor codes must never be averaged.
- Raster cells near watershed boundaries approximate the polygon using a cell-center rule.
- Product version and year must be documented because annual releases can extend and revise the time series.
- Local impervious layers, road inventories, building footprints, imagery, and field information may be needed for design work.

## Getting Started

1. Open `08_01_land_cover_impervious.ipynb` in Google Colab.
2. Download `NHD__Watershed_Boundaries_HUC_12_Selected.zip` from this module's `data` folder.
3. Run the notebook from the top.
4. Upload the watershed ZIP when prompted.
5. Review the printed source message for each raster.
6. Confirm the grid and valid-area QA/QC checks pass before interpreting results.

## Outputs

The lesson creates:

- `watershed_land_cover_summary.csv`
- `watershed_impervious_summary.csv`
- `watershed_impervious_descriptor_summary.csv`
- `clipped_annual_nlcd_land_cover_2025.tif`
- `clipped_annual_nlcd_impervious_2025.tif`

Each table records the watershed, year, collection version, DOI, access date, and processing notes.

## Troubleshooting

| Issue | What to Check |
|---|---|
| Year discovery is unavailable | The notebook uses the Collection 1.2 fallback list and continues |
| WCS returns XML | Review the printed response error and rerun the fetch cell |
| Raster download is slow | Confirm one HUC-12 is selected and review tile count |
| Local fallback is rejected | Confirm it covers the selected bounds and passes validation |
| Percent impervious is too high | Confirm 0 was retained and only 250 was excluded |
| Products do not align | Rerun all requests with the same bounds and inspect transforms |
| Descriptor totals differ | Check combined masks, NoData, and affine cell area |
| Clip is empty | Confirm the watershed is in CONUS and has a valid CRS |

## Official Resources

- [Annual NLCD Product Suite](https://www.usgs.gov/centers/eros/science/nlcd-product-suite)
- [Annual NLCD Collection 1.2 Data Release](https://www.usgs.gov/data/annual-national-land-cover-database-nlcd-collection-1-products)
- [Annual NLCD Collection 1.2 User Guide](https://www.mrlc.gov/sites/default/files/docs/LSDS-2103%20Annual%20National%20Land%20Cover%20Database%20%28NLCD%29%20Collection%201%20Science%20Product%20User%20Guide%20-v1.2%202026_04_21.pdf)
- [MRLC Data Services](https://www.mrlc.gov/data-services-page)
- [Fractional Impervious Surface](https://www.mrlc.gov/data/type/fractional-impervious-surface)
- [Impervious Descriptor](https://www.mrlc.gov/data/type/impervious-descriptor)
- [NOAA C-CAP](https://coast.noaa.gov/digitalcoast/data/ccapregional.html)
