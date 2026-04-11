# Module 6: Precipitation Frequency Analysis

## Overview

This module focuses on generating design storms for hydrologic and hydraulic modeling using NOAA Atlas 14 precipitation frequency data. You'll learn to access Atlas 14 data programmatically, apply temporal distributions to create hyetographs, batch-process multiple return periods, and export formatted inputs for HEC-HMS and HEC-RAS. Instead of building one storm at a time, you'll automate the entire workflow.

## Learning Objectives

By the end of this module, you will be able to:

- Access NOAA Atlas 14 precipitation frequency data via API (with manual fallback)
- Understand precipitation frequency concepts (AEP, ARI, duration, depth)
- Upload and apply custom temporal distributions (MSE 6, SCS Type II, etc.)
- Generate design storm hyetographs at any time interval
- Batch-process multiple AEP events (10-year through 500-year) in a single run
- Create professional summary tables for engineering reports
- Build comparative hyetograph visualizations
- Export design storms in HEC-HMS compatible format
- Package all outputs into a project archive for delivery

## Lessons

**Lesson 1: Design Storm Generation with NOAA Atlas 14**
- Mental models: design storm concepts for H&H (AEP, ARI, depth, duration, hyetograph)
- NOAA Atlas 14 API access with production-reliable implementation
- Manual data entry fallback when API is unavailable
- Loading and visualizing temporal distributions (cumulative and incremental)
- Design storm hyetograph generation function
- Batch processing multiple AEP events
- Comparative visualization of design storms
- Professional summary tables (storm characteristics, peak intensities)
- HEC-HMS export formatting
- Project archiving and download

## Prerequisites

- Completion of Module 1 (Python fundamentals, Colab setup)
- Google account (for Colab access)
- Basic understanding of variables, functions, and pandas DataFrames
- Familiarity with H&H design storm concepts is helpful but not required

## Data Files

This module uses one data file and optionally accesses NOAA Atlas 14 via API:

| File | Description |
|------|-------------|
| `Rainfall Depth vs. Time Table.csv` | MSE 6 24-hour temporal distribution (cumulative depth fractions over time) |

The NOAA Atlas 14 precipitation depths are retrieved via API for any location in the US, with a manual entry option if the API is unavailable.

## Getting Started

1. Open the notebook `Module6_PrecipitationData.ipynb` in Google Colab
2. Download the temporal distribution CSV from the course GitHub repository
3. Run the notebook — it will first try the NOAA API, then offer manual entry if needed
4. Upload the temporal distribution file when prompted
5. Work through each section sequentially, running all code cells
6. Complete the practice exercises at the end to reinforce your learning

## Key Concepts

### AEP vs. ARI
Two ways to express the same probability:

| AEP (%) | ARI (years) | Common Use |
|---------|-------------|------------|
| 50% | 2-year | Frequent event |
| 10% | 10-year | Minor flooding, drainage design |
| 4% | 25-year | Moderate flooding |
| 2% | 50-year | Major flooding |
| 1% | 100-year | Base flood (FEMA) |
| 0.2% | 500-year | Critical infrastructure |

Conversion: `AEP (%) = 100 / ARI (years)`

### The Design Storm Workflow
1. **NOAA Atlas 14** — Get total precipitation depth for your AEP and duration
2. **Temporal Distribution** — Apply a pattern (MSE 6, SCS Type II, etc.) to spread that depth over time
3. **Hyetograph** — Create a time series at your desired interval (6-min, 15-min, 1-hr)
4. **Model Input** — Export to HEC-HMS or HEC-RAS format

### Temporal Distributions
Define **when** rainfall occurs within the storm duration:
- **SCS Type II**: Standard for most of the US, peak near the middle
- **MSE 6**: Minnesota-specific 24-hour distribution
- **SCS Type IA/III**: Regional variants for coastal/maritime climates

### NOAA Atlas 14
The authoritative source for precipitation frequency estimates in the US:
- Statistical analysis of 50+ years of rainfall records
- Covers durations from 5 minutes to 60 days
- Return periods from 1-year to 1000-year
- Free public access via web interface and API

## Using AI Assistants

This module involves API calls, data parsing, and some math-heavy hyetograph generation. If any of the code feels complex, ask your AI assistant:

- "Can you explain how this function converts Atlas 14 depths into a hyetograph?"
- "The NOAA API call failed — here's the error. What should I try?"
- "I want to use SCS Type II instead of MSE 6. What would I need to change?"

The functions in this module are longer than what you've seen in earlier modules, but they follow the same patterns: take inputs, do calculations, return results.

## Key Takeaways

- Always document your Atlas 14 source, region, and retrieval date
- Verify the temporal distribution is appropriate for your project region
- Check that time intervals match what your model expects
- Create summary tables for every project — they're always needed for reports
- Archive all inputs and outputs together so the analysis is reproducible

## Troubleshooting

| Issue | Solution |
|-------|----------|
| NOAA API connection error | Check network/VPN; use manual data entry as fallback |
| Wrong precipitation depths | Verify lat/lon coordinates and that you selected the correct duration row |
| Hyetograph doesn't sum to total depth | Check the temporal distribution file sums to 1.0 |
| Peak intensity seems too high/low | Verify the time interval setting matches your expectations |
| HEC-HMS can't read the export | Check the column format (DateTime, Precipitation) matches HMS requirements |

## Next Steps

This is the final module in the current course. With all six modules complete, you can:

- Set up Python and work in Google Colab (Module 1)
- Analyze time series data (Module 2)
- Perform spatial analysis with vector data (Module 3)
- Analyze rasters — DEMs, land cover, slope, curve numbers (Module 4)
- Pull real USGS gauge data automatically (Module 5)
- Generate design storms from NOAA Atlas 14 (Module 6)

Check the course repository for new modules as they're added, and consider contributing your own workflows.

## Resources

- [NOAA Atlas 14 (PFDS)](https://hdsc.nws.noaa.gov/pfds/) - Precipitation Frequency Data Server
- [NRCS TR-55](https://www.nrcs.usda.gov/) - SCS curve number and design storm methods
- [HEC-HMS User's Manual](https://www.hec.usace.army.mil/software/hec-hms/) - HMS precipitation input requirements
- [NOAA HDSC](https://www.weather.gov/owp/hdsc) - Hydrometeorological Design Studies Center
