<p align="center">
  <img src="../../figures/Logo_pixel.png" alt="Course Logo" width="100">
</p>

# Module 6: Precipitation Frequency Analysis

## Overview

This module focuses on generating design storms for hydrologic and hydraulic modeling using NOAA Atlas 14 precipitation frequency data. You'll learn to access Atlas 14 data programmatically, apply temporal distributions to create hyetographs, batch-process multiple return periods, and export formatted inputs for HEC-HMS and HEC-RAS. Instead of building one storm at a time, you'll automate the entire workflow.

Throughout the module you'll see 🤖 callout boxes with concrete AI prompts. The point isn't just to read the code — it's to get comfortable pasting snippets into your AI assistant, asking specific questions, and using the answers to extend the workflow.

## Learning Objectives

By the end of this module, you will be able to:

- Access NOAA Atlas 14 precipitation frequency data programmatically through the official API
- Diagnose common API failures (VPNs, server downtime, rate limits, coverage gaps) and recover from them
- Understand precipitation frequency concepts (AEP, ARI, duration, depth)
- Upload and apply custom temporal distributions (MSE 6, SCS Type II, and others)
- Generate design storm hyetographs at any time interval
- Batch-process multiple AEP events (10-year through 500-year) in a single run
- Create professional summary tables for engineering reports
- Build comparative hyetograph visualizations
- Export design storms in HEC-HMS compatible format
- Package all outputs into a project archive for delivery
- Use an AI assistant to read, extend, and debug each piece of the workflow

## Lessons

**Lesson 1: Design Storm Generation with NOAA Atlas 14**

- Mental models: design storm concepts for H&H (AEP, ARI, depth, duration, hyetograph)
- NOAA Atlas 14 API access with a production-style implementation
- Why the API might fail (VPNs, server downtime, coverage limits, rate limits) and how to recover
- Loading and visualizing temporal distributions (cumulative and incremental)
- Design storm hyetograph generation function
- Batch processing multiple AEP events
- Comparative visualization of design storms
- Professional summary table of storm characteristics (depth, peak intensity, peak time, duration)
- HEC-HMS export formatting
- Project archiving and download
- An end-of-module "Debug This Snippet with AI" exercise that walks you through pasting buggy code into your AI assistant

## Prerequisites

- Completion of Module 1 (Python fundamentals, Colab setup)
- Google account (for Colab access)
- Basic understanding of variables, functions, and pandas DataFrames
- Familiarity with H&H design storm concepts is helpful but not required

## Data Files

This module uses one data file and pulls everything else from the NOAA API:

| File | Description |
|------|-------------|
| `Rainfall Depth vs. Time Table.csv` | MSE 6 24-hour temporal distribution (cumulative depth fractions over time) |

The NOAA Atlas 14 precipitation depths are retrieved over the network for any location in the contiguous US, Alaska, Hawaii, or US territories that the dataset covers. There is no manual fallback table baked into the notebook; if the API call fails, the module shows you why and what to try next.

## Getting Started

1. Open the notebook `Module6_PrecipitationData.ipynb` in Google Colab.
2. Download the temporal distribution CSV from the course GitHub repository.
3. Run the notebook from the top. It will try the NOAA API for your coordinates and, if the call fails, walk you through the most common reasons.
4. Upload the temporal distribution file when prompted.
5. Work through each section sequentially, running all code cells.
6. Use the 🤖 prompt callouts in the markdown cells to deepen your understanding as you go.
7. Try the "Debug This Snippet with AI" exercise near the end.

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

1. **NOAA Atlas 14** — get total precipitation depth for your AEP and duration.
2. **Temporal Distribution** — apply a pattern (MSE 6, SCS Type II, etc.) to spread that depth over time.
3. **Hyetograph** — create a time series at your desired interval (6-min, 15-min, 1-hr).
4. **Model Input** — export to HEC-HMS or HEC-RAS format.

### Temporal Distributions

Define **when** rainfall occurs within the storm duration:

- **SCS Type II:** standard for most of the US, peak near the middle.
- **MSE 6:** Minnesota-specific 24-hour distribution.
- **SCS Type IA/III:** regional variants for coastal/maritime climates.

### NOAA Atlas 14

The authoritative source for precipitation frequency estimates in the US:

- Statistical analysis of 50+ years of rainfall records.
- Covers durations from 5 minutes to 60 days.
- Return periods from 1-year to 1000-year.
- Free public access via web interface and API.

### Why the API can fail

The notebook walks through this in detail, but the short list is:

- Corporate networks and VPNs that route traffic through proxies (the AECOM VPN is a common offender).
- NOAA server downtime or maintenance windows.
- Requesting a location outside Atlas 14 coverage.
- Rate limiting from too many rapid requests.
- Transient timeouts (often resolved by a re-run a minute later).

## Using AI Assistants

This module deliberately leans on AI assistance because the workflow has long functions, API quirks, and unit-sensitive math. You'll find concrete 🤖 prompt boxes throughout the notebook covering:

- Walking through `get_atlas14_data`, `generate_design_storm`, and `generate_aep_suite` line by line.
- Adding a retry mechanism to the API call.
- Diagnosing a `ConnectionError` on a corporate VPN.
- Extending the batch function to handle multiple storm durations.
- Adapting the HEC-HMS export to HEC-RAS unsteady boundary conditions.

There is also an end-of-module **Practice: Debug This Snippet with AI** exercise. The cell contains an intentionally broken helper function that runs without crashing but returns the wrong answer. The intended workflow is: run the cell, see the gap between the buggy and correct numbers, paste the function into your AI assistant with a clear prompt, apply the fix, confirm it works. This pattern (run, observe, paste, ask, fix) is exactly what good engineers do every day.

## Key Takeaways

- Always document your Atlas 14 source, region, and retrieval date.
- Verify the temporal distribution is appropriate for your project region.
- Check that time intervals match what your model expects.
- Create summary tables for every project — they're always needed for reports.
- Archive all inputs and outputs together so the analysis is reproducible.
- Use AI deliberately: paste the actual code, state what's wrong, and ask a specific question.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| NOAA API connection error | Re-run the cell after a minute; if you're on a VPN, switch it off and try again; verify the coordinates are inside Atlas 14 coverage. |
| Wrong precipitation depths | Verify lat/lon coordinates and that you selected the correct duration row from the Atlas 14 table. |
| Hyetograph doesn't sum to total depth | Check the temporal distribution file sums to 1.0; double-check that the function multiplies cumulative fractions, not incremental ones, by the total. |
| Peak intensity seems too high/low | Verify the time interval setting matches your expectations; remember that intensity (in/hr) and incremental depth (in/interval) are not the same number. |
| HEC-HMS can't read the export | Check the column format (`DateTime`, `Precipitation_in`) matches HMS requirements; verify timestamps are at consistent intervals with no gaps. |

## Next Steps

This is the final module in the current course. With all six modules complete, you can:

- Set up Python and work in Google Colab (Module 1).
- Analyze time series data (Module 2).
- Perform spatial analysis with vector data (Module 3).
- Analyze rasters — DEMs, land cover, slope, curve numbers (Module 4).
- Pull real USGS gauge data automatically, complete with gap-fill demos (Module 5).
- Generate design storms from NOAA Atlas 14 (Module 6).

Check the course repository for new modules as they're added, and consider contributing your own workflows.

## Resources

- [NOAA Atlas 14 (PFDS)](https://hdsc.nws.noaa.gov/pfds/) — Precipitation Frequency Data Server
- [NOAA HDSC](https://www.weather.gov/owp/hdsc) — Hydrometeorological Design Studies Center
- [NRCS TR-55](https://www.nrcs.usda.gov/) — SCS curve number and design storm methods
- [HEC-HMS User's Manual](https://www.hec.usace.army.mil/software/hec-hms/) — HMS precipitation input requirements
- [HEC-RAS Documentation](https://www.hec.usace.army.mil/software/hec-ras/) — RAS unsteady precipitation boundary condition reference
