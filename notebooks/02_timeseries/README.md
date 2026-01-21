# Module 2: Time Series Analysis

## Overview

This module teaches the essential time series skills that hydrologic and hydraulic (H&H) professionals use daily. You'll learn to work with real USGS streamflow data, from loading and cleaning to visualization and statistical analysis. These skills transfer directly to other time series data including precipitation, stage, groundwater levels, and water quality measurements.

## Learning Objectives

By the end of this module, you will be able to:

- Load CSV data and convert date columns to proper datetime format
- Use datetime indexes for efficient time-based filtering and slicing
- Handle missing values appropriately for hydrologic data
- Resample data between time steps (daily → monthly → annual)
- Calculate rolling statistics for trend analysis
- Create professional visualizations (hydrographs, flow duration curves, seasonal box plots)
- Compute summary statistics and percentiles commonly used in H&H reports
- Use AI assistants effectively to explain, debug, and extend your code

## Lessons

**Lesson 1: Time Series Basics**
- Mental models: connecting time series concepts to what you already know from Excel
- Loading and cleaning USGS daily discharge data
- Datetime parsing and indexing (the foundation of time series analysis)
- Time-based slicing: filtering data by year, month, or date range
- Unit conversion (cfs ↔ cms)
- Resampling: aggregating daily data to monthly or annual summaries
- Rolling averages for smoothing and trend detection
- Visualization patterns for H&H reports (hydrographs, box plots, flow duration curves)
- Summary statistics and percentiles
- Using AI assistants as a pair programmer throughout the workflow

## Prerequisites

- Completion of Module 1 (Python fundamentals, Colab setup)
- Google account (for Colab access)
- Basic understanding of variables, functions, and data types in Python
- No prior experience with pandas or time series analysis required

## Data Files

This module uses real USGS data that you can continue using in your own projects:

| File | Description |
|------|-------------|
| `Mississippi_River_at_St__Paul__MN_-_USGS-05331000_Discharge_daily.csv` | ~25 years of daily discharge data from the Mississippi River at St. Paul, MN (USGS Station 05331000) |

## Getting Started

1. Open the notebook `02_01_TimeSeries_Basics.ipynb` in Google Colab
2. Download the data file from the course GitHub repository
3. Work through each section sequentially, running all code cells
4. Use the provided AI prompts when you need help understanding or modifying code
5. Complete the practice exercises at the end to reinforce your learning

## Key Concepts

### Datetime Index
The most important concept in this module. Setting a datetime column as your DataFrame's index enables:
- Easy time-based filtering (`df.loc['2020']` returns all 2020 data)
- Resampling between time steps
- Automatic date formatting on plot axes

### Resampling vs. Rolling
- **Resampling** reduces data to fewer points (daily → monthly = fewer rows)
- **Rolling** keeps the same number of rows but smooths values using a moving window

### Flow Duration Curve
A fundamental hydrologic tool showing what percentage of time each flow is exceeded. Key percentiles:
- Q10 = Flow exceeded 10% of time (high flow conditions)
- Q50 = Median flow
- Q90 = Flow exceeded 90% of time (low flow conditions)

## Using AI Assistants

This module includes **🤖 AI Assistant Prompts** throughout. These are ready-to-use templates you can copy into any AI assistant (ChatGPT, Claude, Gemini, etc.) to:

- Get line-by-line explanations of code you don't understand
- Debug errors with context-specific help
- Modify code for your own datasets and projects

**Using AI is a professional skill, not a shortcut.** The goal is to understand what the code does, not to memorize syntax.

## Practice Exercises

The lesson includes 5 exercises ranging from basic to challenging:

1. **Parse and Index** - Reinforce the data loading workflow
2. **Monthly Plot** - Create a plot with multiple series
3. **Unit Conversion** - Work with percentiles in different units
4. **Rolling Statistics** - Apply rolling calculations and find extremes
5. **FDC Function (Challenge)** - Create a reusable function with AI assistance

## Key Takeaways

- Always convert date columns to datetime and set as index before analysis
- Use `.info()` to audit your data before diving into analysis
- Resampling and rolling operations are your main tools for changing time scales
- Flow duration curves, seasonal box plots, and hydrographs are the core H&H visualizations
- AI assistants are valuable learning partners—use the provided prompts liberally

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Date column still shows as "object" type | Run `df['date'] = pd.to_datetime(df['date'])` |
| Time slicing doesn't work | Make sure the date column is set as the index |
| Import error | Copy the error and ask your AI assistant for Colab-specific help |
| Plot doesn't display | Add `plt.show()` at the end of your plotting code |

## Next Steps

After completing this module, you'll be ready for:
- **Module 3**: Vector Data Analysis


## Resources

- [pandas Documentation](https://pandas.pydata.org/docs/) - Official pandas reference
- [matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html) - Plot examples
- [USGS Water Data](https://waterdata.usgs.gov/nwis) - Download data for other gages
- Course discussion forum for H&H-specific questions
