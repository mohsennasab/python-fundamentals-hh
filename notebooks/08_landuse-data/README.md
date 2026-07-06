<p align="center">
  <img src="../../figures/Logo_pixel.png" alt="Course Logo" width="100">
</p>

# Module 8: Land Cover and Impervious Surface Data for H&H Modeling

## Overview

This module teaches you how to work with official USGS/MRLC land cover and impervious surface data (NLCD) for watershed hydrology. You will learn the difference between a categorical land cover raster and a continuous percent-impervious raster, summarize a watershed's land cover by area and percent, calculate a correct watershed-average percent impervious value, separate roads from other built surfaces, and compare land cover between two years to quantify change.

The module is built around a real data mistake that is easy to make and easy to miss: trusting a raster's declared NoData value without checking whether it applies to that specific product. You will make the mistake, see the effect it has on the result, find the correct answer in official documentation, and recalculate correctly. That habit, verify before you trust, is the module's main takeaway.

Throughout the module you will see 🤖 callout boxes with concrete AI prompts. Use them to explain unfamiliar steps, reason through the NoData investigation, or extend the workflow to your own project data.

## Learning Objectives

By the end of this module, you will be able to:

- Explain the difference between categorical and continuous rasters, and choose the correct summary method for each
- Explain the difference between land cover and land use
- Reproject a watershed boundary to match a raster's CRS, and explain why that direction is correct
- Clip an NLCD land cover raster to a watershed and summarize classes by area and percent
- Recognize a NoData handling mistake in a continuous raster and correct it using official product documentation
- Calculate an area-weighted watershed percent impervious value and an equivalent impervious area
- Use the impervious descriptor product to separate road surfaces from other built surfaces
- Compare land cover and imperviousness between two years to quantify watershed change
- Export traceable, model-ready summary tables and clipped GeoTIFFs

## Lessons

**Lesson 1: Land Cover and Impervious Surface Data for H&H Modeling**

- Mental models: land cover versus land use, and categorical versus continuous rasters
- NLCD as the official data source, MRLC access options, and why this module fetches its rasters live via a web service instead of a manual download
- Loading the watershed and fetching NLCD rasters automatically for its exact extent
- Getting the CRS reprojection direction right
- Land cover workflow: clip, count, legend, area and percent, map
- Percent impervious workflow: a wrong-but-reasonable first attempt, an investigation into NLCD's NoData convention, and the corrected calculation
- Impervious descriptor: roads versus other built surfaces
- Change analysis: land cover and percent impervious, 2001 versus 2021
- Export: traceable summary tables and clipped GeoTIFFs
- NOAA C-CAP and local data as alternatives for coastal or parcel-scale work

## Prerequisites

- Completion of Module 1 (Python fundamentals, Colab setup)
- Completion of Module 3 (vector data and coordinate reference systems)
- Completion of Module 4 (raster fundamentals: pixels, resolution, clipping, NoData)
- Module 7 (SSURGO soils) is helpful background, since its hydrologic soil group output pairs directly with this module's land cover table for curve number work, but it is not required
- Google account (for Colab access)

## Data Acquisition: Automatic, Not Manual

This notebook fetches its own NLCD rasters. There is no raster download or upload step. After you select a watershed, the notebook builds a small bounding box around it and requests exactly that area from the official MRLC Web Coverage Service (WCS), a free, no-login web service. Five small GeoTIFFs (land cover and impervious surface for 2001 and 2021, plus the impervious descriptor for 2021) are fetched and saved automatically, typically a few hundred kilobytes each.

If the live WCS request fails for any reason (a network hiccup, a brief MRLC outage), the notebook automatically falls back to a pre-clipped copy of the same product hosted in this repository's `data/` folder, so a temporary outage does not stop the lesson. You do not need to do anything differently when that happens; a message prints explaining which path was used.

**Why not the newer Annual NLCD product line?** Annual NLCD (yearly coverage from 1985 to the present) is distributed through a **requester-pays** AWS S3 bucket (`s3://usgs-landcover/annual-nlcd/...`). Requester-pays buckets reject anonymous requests entirely; every student would need their own AWS account with billing enabled just to fetch one file. That does not fit a free, no-installation course, so this module uses the standard NLCD releases (2001-2021) instead, which the MRLC WCS serves with no account and no cost.

## Data Files

| File | Description |
|------|-------------|
| `NHD__Watershed_Boundaries_HUC_12_Selected.zip` | The same Wyoming HUC-12 watershed boundaries used in Modules 3, 5, and 7. Uploaded manually, same as those modules. |
| `nlcd_2001_land_cover.tif` | Fallback copy: NLCD 2001 Land Cover, clipped to the course study area |
| `nlcd_2021_land_cover.tif` | Fallback copy: NLCD 2021 Land Cover, clipped to the course study area |
| `nlcd_2001_impervious.tif` | Fallback copy: NLCD 2001 Fractional Impervious Surface, clipped to the course study area |
| `nlcd_2021_impervious.tif` | Fallback copy: NLCD 2021 Fractional Impervious Surface, clipped to the course study area |
| `nlcd_2021_impervious_descriptor.tif` | Fallback copy: NLCD 2021 Impervious Descriptor, clipped to the course study area |

The five GeoTIFFs above exist in this repository only as an automatic fallback; you do not need to download them yourself. They were originally clipped from the official MRLC Web Coverage Service (`https://www.mrlc.gov/geoserver/wcs`), coverage IDs `mrlc_download__NLCD_2001_Land_Cover_L48`, `mrlc_download__NLCD_2021_Land_Cover_L48`, `mrlc_download__NLCD_2001_Impervious_L48`, `mrlc_download__NLCD_2021_Impervious_L48`, and `mrlc_download__NLCD_2021_Impervious_descriptor_L48`, clipped to the full extent of the 19-watershed HUC-12 selection with a small buffer. NoData values were verified against official MRLC/USGS documentation and corrected where the raw download's metadata did not match the product's actual convention (see Key Concepts below). Files are LZW-compressed GeoTIFFs.

## Getting Started

1. Open the notebook `08_01_land_cover_impervious.ipynb` in Google Colab.
2. Download `NHD__Watershed_Boundaries_HUC_12_Selected.zip` from this folder (this is the only file you need to download).
3. Run the notebook from the top.
4. Upload the watershed ZIP when prompted. The five NLCD rasters are fetched automatically; no further uploads are needed.
5. Work through each part sequentially, running all code cells. Pay close attention to Part 6, where the notebook deliberately makes a NoData mistake before correcting it.
6. Use the 🤖 prompt callouts to deepen your understanding as you go.
7. Try the practice exercises, including the AI-assisted challenge, near the end.

## Key Concepts

### Land Cover vs. Land Use

Land cover is what physically covers the ground. Land use is how people use it. H&H modeling needs land cover, since runoff and infiltration respond to the physical surface, not to zoning designation.

### Categorical vs. Continuous Rasters

| | Categorical | Continuous |
|---|---|---|
| Products in this module | Land Cover, Impervious Descriptor | Fractional Impervious Surface |
| Cell value means | A class code | A measured percentage |
| Correct summary | Count cells per class | Average, weighted by area |

### The NoData Discovery

This module's central engineering caution: the raw MRLC download declares NoData as a single generic value regardless of product. That value is correct for Land Cover (0, since no real land cover class is coded 0) but is wrong for the Fractional Impervious Surface and Impervious Descriptor products, where 0 is a legitimate reading ("0 percent impervious" or "not impervious") and the true background sentinel is **127**. Masking on the wrong value for the target watershed in this module inflates mean percent impervious from a correct 10.19% to an incorrect 45.16%, a 35 percentage point error, while barely affecting the total impervious acreage estimate. The notebook's own fetch function writes the correct NoData value into every raster it retrieves (live or fallback), so this is not a bug students need to fix; Part 6 still walks through the mistake deliberately, by intentionally masking on the wrong value the first time, so you can recognize the pattern in data you did not prepare yourself.

### Why Reproject the Vector, Not the Raster

Reprojecting a watershed boundary recalculates coordinates exactly. Reprojecting a categorical raster resamples and can reassign class codes at cell edges. Always reproject vectors to match the raster's CRS.

### NLCD's Equal-Area Projection

NLCD rasters use a Conterminous US Albers Equal-Area projection (EPSG:5070), where every cell represents the same true ground area regardless of location. This is what makes area and percentage math meaningful; a geographic (degree-based) CRS would distort area by latitude.

## Using AI Assistants

This module leans on AI assistance for reasoning through the NoData investigation and for the challenge exercise. You will find 🤖 prompt boxes covering:

- Why averaging categorical class codes does not make sense.
- Why vectors should be reprojected to match a raster's CRS, not the reverse.
- Interpreting a percent impervious result for H&H modeling, including resolution and year limitations.
- Building a reusable `summarize_land_cover(huc12_code, raster_path)` function, in the challenge exercise.

## Key Takeaways

- Categorical rasters hold codes; only count them. Continuous rasters hold quantities; average them.
- Never estimate percent impervious by counting developed land cover classes when the fractional impervious product is available.
- Verify a raster's true NoData convention against official documentation before masking; do not assume 0 always means missing, and do not assume every product shares the same convention.
- Reproject vectors to match raster CRS, never the reverse.
- Document product, version, and year on every output, especially for change analyses.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Both the live fetch and the fallback fail | Check your internet connection and rerun the fetch cell; retry after a few minutes if the course repository is briefly unreachable. |
| A raster fetch is very slow | Reduce `buffer_m`, or confirm you selected a single HUC-12, not a larger area. |
| Clipped raster is empty or tiny | Confirm the vector was reprojected to the raster's CRS before clipping; print both CRS values. |
| Land cover and impervious pixel counts do not match for the same watershed | Check the NoData value used for each product; verify against official documentation rather than assuming. |
| Percent impervious looks too high | NoData masking is likely excluding legitimate low or zero values; use 127, not 0, for the impervious and descriptor products. |
| Areas do not match a GIS calculation | Confirm the area math used the raster's native equal-area CRS (EPSG:5070), not a geographic CRS. |
| Map colors look wrong or classes are missing | Confirm the legend dictionary includes every code actually present in the clipped array. |
| Colab upload fails | Re-run the upload cell and select the watershed ZIP file. |

## Next Steps

- **Combine with Modules 4 and 7.** This module's land cover table and Module 7's hydrologic soil group table are the two real inputs to a proper composite curve number calculation, replacing the single-soil-group assumption Module 4 used for illustration.
- **On your own.** Run this workflow on a watershed from a current project and compare the percent impervious result against any as-built or GIS-based estimate you already have.
- **Coastal or parcel-scale work.** See Part 10 of the notebook for when NOAA C-CAP or local high-resolution data are the better source.

## Resources

- [MRLC Consortium](https://www.mrlc.gov/): Multi-Resolution Land Characteristics Consortium, home of NLCD
- [NLCD Class Legend and Description](https://www.mrlc.gov/data/legends/national-land-cover-database-class-legend-and-description): official land cover class codes and names
- [Impervious Descriptor documentation](https://www.mrlc.gov/data/type/impervious-descriptor): descriptor product overview
- [MRLC Data Portal](https://www.mrlc.gov/data): manual downloads of NLCD products
- [MRLC Viewer](https://www.mrlc.gov/viewer/): AOI-based download tool
- [USGS Annual NLCD](https://www.usgs.gov/centers/eros/science/annual-nlcd): the newer yearly product line, distributed via a requester-pays AWS S3 bucket
- [NOAA C-CAP](https://coast.noaa.gov/digitalcoast/data/ccapregional.html): coastal land cover alternative
- [MRLC Web Coverage Service documentation](https://www.mrlc.gov/data-services-page): the free, no-login service this notebook uses to fetch clipped rasters
