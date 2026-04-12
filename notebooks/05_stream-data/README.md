# Module 5: USGS Data Retrieval

## Overview

This module teaches you how to access USGS stream gauge data programmatically — a skill that replaces hours of manual website navigation with a few lines of Python. You'll learn to find gauges near any watershed, download streamflow and stage data, process time series for model input, and export data ready for H&H modeling workflows. The workflow you build here is directly reusable on any future project.

## Learning Objectives

By the end of this module, you will be able to:

- Understand USGS data architecture (NWIS, parameter codes, data types)
- Find all USGS monitoring locations near any watershed boundary
- Retrieve instantaneous (15-minute) and daily streamflow and stage data
- Perform spatial filtering to identify gauges within your study area
- Resample data to model-appropriate time steps
- Fill data gaps using linear interpolation with appropriate limits
- Generate professional gauge catalogs and data availability summaries
- Export processed data ready for H&H modeling workflows
- Use AI assistants to troubleshoot API issues and extend workflows

## Lessons

**Lesson 1: USGS Data Retrieval for H&H Modeling**
- Mental models: how USGS organizes water data (NWIS, parameter codes, site numbers)
- Installing and using the `dataretrieval` library (maintained by USGS)
- Loading and preparing your watershed boundary
- CRS normalization and buffering for gauge discovery
- Querying USGS for monitoring locations within a bounding box
- Spatial filtering: keeping only gauges within the buffered watershed
- Ranking gauges by distance from watershed centroid
- Interactive mapping of gauges with Folium
- Retrieving discharge and stage time series
- Data processing: resampling, gap filling, quality control
- Generating gauge catalogs and metadata files

- Complete workflow summary report

## Prerequisites

- Completion of Module 1 (Python fundamentals, Colab setup)
- Completion of Module 3 (Vector data, coordinate systems, spatial operations)
- Google account (for Colab access)
- Basic understanding of DataFrames, spatial data, and time series concepts
- Internet connection (required for USGS API queries)

## Data Files

This module requires a watershed boundary file for gauge discovery. You can use:

| File | Description |
|------|-------------|
| `NHD__Watershed_Boundaries_HUC_12_Selected.zip` | HUC-12 watershed boundaries (same as Modules 3-4) |

You can also upload your own watershed boundary as a Shapefile (ZIP) or GeoJSON.

## Getting Started

1. Open the notebook `Module5_USGSDataRetrieval.ipynb` in Google Colab
2. Download the watershed boundary file from the course GitHub repository (or use your own)
3. Upload the file to Colab when prompted
4. Work through each section sequentially, running all code cells
5. Use the provided AI prompts when you need help understanding or modifying code
6. Complete the practice exercises at the end to reinforce your learning

## Key Concepts

### USGS Parameter Codes
Five-digit codes that identify what's being measured:

| Code | Parameter | Units | H&H Use |
|------|-----------|-------|----------|
| 00060 | Discharge (Flow) | cfs | Model calibration |
| 00065 | Gage Height (Stage) | ft | Boundary conditions |
| 00010 | Water Temperature | C | Water quality |
| 00055 | Stream Velocity | ft/s | Hydraulic analysis |

### Data Types
- **IV (Instantaneous Values)**: 15-minute data for real-time monitoring and event analysis
- **DV (Daily Values)**: Daily statistics for long-term trend analysis

### Spatial Filtering Strategy
1. Get watershed bounding box (rectangle)
2. Query USGS for all gauges in the box
3. Apply polygon filter to keep only gauges within the buffered watershed
4. Rank by distance from watershed centroid

### Data Gaps
Missing data is normal in gauge records (equipment failure, ice, maintenance). The module teaches:
- Identifying gaps by checking time step consistency
- Filling short gaps (up to 6 hours) with linear interpolation
- Flagging longer gaps for manual review

## Using AI Assistants

The `dataretrieval` library has its own conventions for querying USGS data. If something doesn't work as expected, ask your AI assistant:

- "What does `nwis.get_iv()` do and what parameters does it take?"
- "I got an empty DataFrame back from my USGS query. What might be wrong?"
- "How do I change this to retrieve daily values instead of instantaneous?"

The USGS API can be finicky sometimes (network timeouts, empty results for certain areas). Your AI assistant can usually help you troubleshoot quickly.

## Practice Exercises

The lesson includes 4 exercises:

1. **Multi-Gauge Analysis** - Retrieve and compare flow data from the top 3 gauges
2. **Extended Time Period** - Download 10 years of daily data and analyze long-term trends
3. **Water Temperature Analysis** - Retrieve and analyze temperature data with seasonal patterns
4. **Automated Report Generation** - Build a function that generates a complete report for any watershed

## Key Takeaways

- USGS NWIS has 15,000+ active gauges with free, public data — always check what's available
- Parameter codes are universal: 00060 = discharge, 00065 = stage, everywhere in USGS
- Bounding box queries get you close; polygon filtering gets you exact results
- Data gaps are normal — plan for them, fill what you can, flag what you can't
- The script you write once saves hours every time you use it on a new project

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No gauges found in search area | Increase the buffer distance or check that your watershed CRS is correct |
| Empty DataFrame from USGS query | Verify parameter codes, check date range, ensure site has data for that period |
| Timeout or connection error | USGS servers can be slow; try again or reduce the date range |
| Stage data missing when flow exists | Not all gauges measure both; check data availability first |
| Resampled data has many NaN values | Expected for gaps; use `interpolate(limit=N)` for short gaps only |

## Next Steps

After completing this module, you'll be ready for:
- **Module 6**: Precipitation frequency analysis with NOAA Atlas 14

With Modules 2-5 complete, you can pull real gauge data, process time series, and generate model-ready exports — all programmatically.

## Resources

- [USGS dataretrieval Documentation](https://doi-usgs.github.io/dataretrieval-python/) - Official Python library docs
- [USGS Water Services](https://waterservices.usgs.gov/) - API documentation
- [USGS NWIS](https://waterdata.usgs.gov/nwis) - Web interface for gauge data
- [USGS Parameter Codes](https://help.waterdata.usgs.gov/parameter_cd?group_cd=PHY) - Full parameter code list
