<p align="center">
  <img src="../../figures/Logo_pixel.png" alt="Course Logo" width="100">
</p>

# Module 4: Raster Data Analysis

## Overview

This module introduces raster (gridded) data analysis — essential for understanding **how** water moves across terrain and **what** the land surface looks like within your watersheds. You'll work with real Digital Elevation Models (DEMs) and National Land Cover Database (NLCD) data to calculate terrain statistics, generate slope maps, and assign curve numbers. Combined with the vector skills from Module 3, this completes your spatial analysis toolkit for H&H modeling.

## Learning Objectives

By the end of this module, you will be able to:

- Load and explore raster data (GeoTIFF format) using rasterio
- Understand raster properties: resolution, bands, NoData values, and coordinate systems
- Clip rasters to watershed boundaries for focused analysis
- Calculate elevation statistics and create elevation bands
- Generate slope maps from DEMs
- Classify and quantify land cover using NLCD data
- Assign SCS Curve Numbers based on land cover for runoff estimation
- Create professional multi-panel analysis dashboards
- Use AI assistants to understand and extend raster analysis workflows

## Lessons

**Lesson 1: Raster Data Analysis for H&H Modeling**
- Mental models: raster data as "smart grids" vs. vector "smart drawings"
- Loading and exploring DEMs and NLCD land cover data
- Aligning coordinate reference systems across raster and vector data
- Clipping rasters to watershed boundaries using rasterio.mask
- Elevation analysis: statistics, histograms, and elevation bands
- Land cover classification and area calculations
- Slope calculation using numpy gradient
- SCS Curve Number assignment and composite CN calculation
- Professional integrated visualization dashboard

## Prerequisites

- Completion of Module 1 (Python fundamentals, Colab setup)
- Completion of Module 3 (Vector data, coordinate systems, spatial operations)
- Google account (for Colab access)
- Basic understanding of DataFrames, numpy arrays, and spatial concepts
- No prior raster analysis or remote sensing experience required

## Data Files

This module uses real datasets from Wyoming, continuing the watershed analysis from Module 3:

| File | Description |
|------|-------------|
| `USGS_13_n42w105_2021061_DEM.tif` | USGS 1/3 arc-second Digital Elevation Model (~10m resolution) |
| `NLCD2024.tif` | National Land Cover Database classification raster (30m resolution) |
| `NHD__Watershed_Boundaries_HUC_12_Selected.zip` | HUC-12 watershed boundaries for clipping (same as Module 3) |

## Getting Started

1. Open the notebook `Module4_RasterData.ipynb` in Google Colab
2. Download the data files from the course GitHub repository
3. Upload all three files to Colab when prompted
4. Work through each section sequentially, running all code cells
5. Use the provided AI prompts when you need help understanding or modifying code
6. Complete the practice exercises at the end to reinforce your learning

## Key Concepts

### Resolution
The size of each pixel determines the level of detail:
- **10m DEM**: Each pixel covers a 10m x 10m area on the ground
- **30m NLCD**: Each pixel covers a 30m x 30m area
- Trade-off: higher resolution means more detail but larger file sizes

### Bands
Layers of information in a raster file:
- **DEM**: Single band (elevation values in meters)
- **NLCD**: Single band (integer land cover class codes)
- **Satellite imagery**: Multiple bands (RGB, infrared, etc.)

### NoData Values
Pixels with no measurement (outside the study area or missing data). Must be masked before calculating statistics to avoid incorrect results.

### Vector + Raster Integration
The core workflow in this module:
1. Load vector boundary (watershed polygon from Module 3)
2. Load raster data (DEM, land cover)
3. Align coordinate systems
4. Clip raster to vector boundary
5. Analyze the clipped raster

## Using AI Assistants

This module introduces several new libraries (rasterio, numpy masked arrays, rasterstats). If a code block looks unfamiliar, ask your AI assistant:

- "Can you explain what `rasterio.mask.mask()` does step by step?"
- "Why do we need to mask NoData values before calculating statistics?"
- "How does `np.gradient()` calculate slope from elevation data?"

The raster functions have some unfamiliar syntax, but the concepts map directly to things you already know from working with GIS.

## Practice Exercises

The lesson includes 5 exercises:

1. **Multi-Watershed Raster Analysis** - Compare elevation and land cover across multiple watersheds
2. **Aspect Analysis** - Calculate and classify terrain aspect (slope direction)
3. **Elevation-Land Cover Relationship** - Analyze how land cover varies with elevation
4. **Runoff Potential Map** - Combine slope and land cover to map runoff potential
5. **Debug This Snippet with AI** - Find and fix a NoData-masking bug in a mean-elevation function by pasting the buggy code into an AI assistant

## Key Takeaways

- Rasters are grids of values — each pixel holds a measurement
- Resolution matters — balance detail with processing time and file size
- CRS alignment between vector and raster data is critical before clipping
- Combining terrain analysis (elevation, slope) with land cover analysis (NLCD, curve numbers) gives you the inputs you need for H&H models
- Module 3 (vector) tells you WHERE the watershed is; Module 4 (raster) tells you WHAT'S INSIDE

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Raster clip produces empty result | Check that watershed and raster CRS match using `.crs` |
| NoData values skewing statistics | Use `np.ma.masked_where()` to mask NoData before calculations |
| Memory error with large rasters | Clip to your study area first before doing analysis |
| Slope values seem wrong | Verify pixel size matches your DEM resolution |
| NLCD colors don't match expected | Check that unique class codes match the NLCD classification dictionary |

## Next Steps

After completing this module, you'll be ready for:
- **Module 5**: USGS data retrieval (automated gauge discovery and data download)

With Modules 3 and 4 complete, you have a full spatial analysis toolkit — vector boundaries plus raster surfaces — ready to support watershed characterization, model parameter estimation, and screening-level risk assessment.

## Resources

- [Rasterio Documentation](https://rasterio.readthedocs.io/) - Official rasterio reference
- [NLCD Data](https://www.mrlc.gov/) - Multi-Resolution Land Characteristics Consortium
- [USGS National Map](https://apps.nationalmap.gov/downloader/) - Download DEMs
- [SCS Curve Number Tables](https://www.nrcs.usda.gov/) - NRCS TR-55 reference
- [NumPy Documentation](https://numpy.org/doc/) - Array operations reference
