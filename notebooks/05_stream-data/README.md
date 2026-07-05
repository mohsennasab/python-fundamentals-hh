<p align="center">
  <img src="../../figures/Logo_pixel.png" alt="Course Logo" width="100">
</p>

# Module 5: USGS Data Retrieval

## Overview

This module teaches you how to access USGS stream gauge data programmatically — a skill that replaces hours of manual website navigation with a few lines of Python. You'll load a real **HUC-8 watershed**, find every USGS gauge in or around it, retrieve streamflow and stage data through the official USGS Python library, demonstrate how to fill gaps in instantaneous records, and export everything as a tidy gauge catalog plus per-gauge CSV/JSON files. The workflow you build here is directly reusable on any future project.

The demo gauge for this module is **USGS-05331000, Mississippi River at St. Paul, MN**, a long-record station with both discharge and stage data. The study watershed is the **Mississippi River - Twin Cities** basin (HUC-8 `07010206`), pulled from the Minnesota DNR watershed suite.

## Learning Objectives

By the end of this module, you will be able to:

- Understand USGS data architecture (NWIS, parameter codes, instantaneous vs. daily values)
- Load a multi-layer shapefile suite and select a single HUC-8 watershed by its code
- Use that watershed to discover every USGS gauge inside or near it
- Apply CRS handling and a search buffer for accurate spatial filtering
- Rank gauges by distance from the watershed centroid and promote a known target gauge to the top of the list
- Use the USGS series catalog to drive retrieval so missing data types are reported, not silently skipped
- Retrieve discharge and stage as either instantaneous (15-min) or daily values
- Visualize the watershed, buffer, and gauges on a map with an OpenStreetMap basemap
- Demonstrate gap-fill behavior with linear interpolation by punching artificial gaps into a 15-day window
- Generate professional gauge catalogs, GeoJSON outputs, and per-gauge CSV/JSON files
- Use AI assistants effectively to extend, debug, and adapt the workflow to other gauges and basins

## Lessons

**Lesson 1: USGS Data Retrieval for H&H Modeling**

- Mental models: how USGS organizes water data (NWIS, parameter codes, site numbers)
- Installing and using the `dataretrieval` library (maintained by USGS)
- Loading the HUC-8 "major" watersheds layer from the Minnesota DNR shapefile suite
- Filtering to the single HUC-8 watershed (`07010206`) that contains the demo gauge
- CRS handling and buffering for gauge discovery
- Querying USGS for monitoring locations within a bounding box
- Spatial filtering: keeping only gauges within the buffered watershed
- Ranking gauges by distance, promoting USGS-05331000 as the demo gauge
- Mapping the watershed, buffer, and gauges with an OpenStreetMap basemap
- Series-catalog-driven retrieval of discharge and stage data (with graceful fallback when a parameter is missing)
- Visualization with empty-panel suppression: missing data types are reported, not plotted as empty
- Quality control in three steps: one year of instantaneous data, zoom into a 15-day window, then add and fill artificial gaps
- Generating gauge catalogs and per-gauge output files ready for HEC-RAS / HEC-HMS

## Prerequisites

- Completion of Module 1 (Python fundamentals, Colab setup)
- Completion of Module 3 (Vector data, coordinate systems, spatial operations)
- Google account (for Colab access)
- Basic understanding of DataFrames, spatial data, and time series concepts
- Internet connection (required for USGS API queries and the OpenStreetMap basemap)

## Data Files

This module uses the Minnesota DNR watershed suite:

| File | Description |
|------|-------------|
| `dnr_huc8_watersheds.zip` | The Minnesota DNR HUC-8 "major" watersheds layer (`dnr_watersheds_dnr_level_04_huc_08_majors.shp`), all 80 basins. The notebook reads this layer and filters it to HUC-8 `07010206`, the Mississippi River - Twin Cities basin that contains USGS-05331000. This is a trimmed extract of the full DNR watershed suite, kept small enough to ship in the repository. |

The HUC-8 layer arrives already in a projected CRS (UTM Zone 15N, EPSG:26915), which is what we want for area and distance calculations.

## Getting Started

1. Open the notebook `Module5_USGSDataRetrieval.ipynb` in Google Colab.
2. Download `dnr_huc8_watersheds.zip` from the course GitHub repository.
3. Upload the file to Colab when prompted.
4. Work through each section sequentially, running all code cells.
5. Use the AI prompt boxes (marked with 🤖 in the markdown cells) to deepen your understanding as you go.
6. Complete the practice exercises at the end to reinforce your learning.

## Key Concepts

### HUC-8 Watersheds

A Hydrologic Unit Code (HUC) is the standard USGS scheme for dividing the country into nested drainage basins. HUC-8 ("subbasin" level, eight digits) is a common working unit for finding the gauges that drain an area. Minnesota's DNR publishes its watersheds with a `HUC_8` code and a readable `major_name`, so selecting a study basin is as simple as filtering on one column.

### USGS Parameter Codes

Five-digit codes that identify what's being measured:

| Code | Parameter | Units | H&H Use |
|------|-----------|-------|---------|
| 00060 | Discharge (Flow) | cfs | Model calibration |
| 00065 | Gage Height (Stage) | ft | Boundary conditions |
| 00010 | Water Temperature | °C | Water quality |
| 00055 | Stream Velocity | ft/s | Hydraulic analysis |

### Data Types

- **IV (Instantaneous Values):** ~15-minute data for real-time monitoring and event analysis. This is where data gaps actually show up.
- **DV (Daily Values):** USGS-published daily statistics for long-term trend analysis. USGS smooths out short gaps before publishing daily values.

### Spatial Filtering Strategy

1. Get the watershed bounding box (rectangle).
2. Query USGS for all gauges in that box.
3. Apply a polygon filter to keep only gauges within the buffered watershed.
4. Rank by distance from the watershed centroid.
5. Promote a known target gauge to the top if it is present.

### Series-Catalog-Driven Retrieval

Instead of guessing at date ranges, the module asks USGS what each gauge actually has (via `nwis.get_info(..., seriesCatalogOutput=True)`) and then uses that period of record (capped to the last 10 years) when calling `get_dv()` or `get_iv()`. If a gauge does not have a requested parameter, the retrieval cells skip it and say so, and the visualization cell only draws panels for the data types that were actually returned.

### Gap-Fill Demonstration with Artificial Gaps

Real instantaneous windows are not always gappy. To make the gap-fill behavior reliably visible in the lesson, Part 8 punches three artificial gaps (4, 6, and 12 hours) into a copy of a 15-day hourly window and runs `interpolate(method='linear', limit=6)` on the result. The plot shows:

- the full original series (light gray) for reference
- the version with artificial gaps (steel blue)
- points filled by interpolation (red dots)
- regions left as NaN because the gap was longer than the limit (red translucent bands)

This makes the limit behavior obvious in one figure.

## Using AI Assistants

This module is sprinkled with 🤖 prompt boxes in the markdown cells. They are starting points for asking your AI assistant about the cell you just ran:

- *"What does `nwis.get_iv()` do and what parameters does it take?"*
- *"What other basemap sources does contextily support, and how do I switch to a satellite basemap?"*
- *"When should I use `.mean()` vs `.max()` vs `.sum()` when resampling discharge?"*
- *"What other interpolation methods does pandas `Series.interpolate` support?"*

Use them, modify them, and write your own. The USGS API and the `dataretrieval` library both have quirks; an AI assistant is the fastest way to work past them.

## Practice Exercises

The notebook includes five exercises that map directly onto the content:

1. **Compare three gauges in the watershed** — retrieve daily discharge for the top three gauges in `sites_in_buffer`, plot them together, and print a comparison table.
2. **Apply the gap-fill demo to stage data** — repeat the year-to-15-day-to-artificial-gap workflow for stage (parameter 00065) instead of discharge.
3. **Use a different HUC-8 watershed** — pick a different `HUC_8` code from the 80 basins already loaded in `watersheds`, then re-run gauge discovery and ranking on the new basin.
4. **Write a `gauge_report(site_no)` function** — wrap the discovery-to-summary flow into a reusable function that returns a small dictionary report for any USGS gauge.
5. **Debug This Snippet with AI** — find and fix a common pandas resampling bug (`.sum()` vs `.mean()`) in an hourly-to-daily conversion by pasting the buggy code into an AI assistant.

## Key Takeaways

- USGS NWIS has 15,000+ active gauges with free, public data; the series catalog tells you what each one has before you ask for it.
- A HUC-8 watershed is a natural unit for gauge discovery, and selecting one is just a filter on the `HUC_8` column.
- Parameter codes are universal: `00060` = discharge, `00065` = stage, `00010` = temperature.
- Bounding box queries get you close; polygon filtering on the buffered watershed gets you exact results.
- Daily values are pre-smoothed by USGS; if you want to see and handle real gaps, you have to work with the instantaneous record.
- Linear interpolation with a `limit` parameter is the standard short-gap fill; anything longer should be reviewed or filled from a nearby gauge.
- The script you write once saves hours every time you use it on a new project.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| HUC-8 code not found | Check the available codes with `watersheds[['HUC_8', 'major_name']]`; make sure you compare as text (leading zeros matter). |
| No gauges found in search area | Increase the buffer distance or confirm the watershed loaded in a projected CRS. |
| Empty DataFrame from a USGS query | Verify the parameter code, check the date range, and make sure the gauge has data for that period (the series catalog cell will tell you). |
| Timeout or connection error | USGS servers can be slow; try again, reduce the date range, or use daily values instead of instantaneous. |
| Stage data missing when flow exists | Not all gauges measure both; the retrieval cells will say so explicitly. |
| Basemap doesn't load | The `contextily` basemap needs internet access to fetch tiles. The plot still renders without it. |
| Gap-fill demo shows no real gaps | Real gaps in a clean 15-day window are sometimes absent; the artificial-gap cell always shows the limit behavior regardless. |

## Next Steps

After completing this module, you'll be ready for:

- **Module 6:** Precipitation frequency analysis with NOAA Atlas 14.

With Modules 2 through 5 complete, you can pull real gauge data, process time series, and generate model-ready exports, all programmatically.

## Resources

- [USGS `dataretrieval` Documentation](https://doi-usgs.github.io/dataretrieval-python/) — official Python library docs
- [USGS Water Services](https://waterservices.usgs.gov/) — API documentation
- [USGS NWIS](https://waterdata.usgs.gov/nwis) — web interface for gauge data
- [USGS Parameter Codes](https://help.waterdata.usgs.gov/parameter_cd?group_cd=PHY) — full parameter code list
- [USGS-05331000 monitoring location](https://waterdata.usgs.gov/monitoring-location/USGS-05331000/) — the demo gauge used in this module
- [Minnesota DNR Watersheds](https://gisdata.mn.gov/dataset/geos-dnr-watersheds) — source of the HUC-8 watershed suite
- [contextily](https://contextily.readthedocs.io/) — basemap library used for the static maps
