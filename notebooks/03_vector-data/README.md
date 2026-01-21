# Module 3: Vector Data Analysis

## Overview

This module introduces the spatial analysis skills that hydrologic and hydraulic (H&H) professionals need to understand **where** things are and how they interact spatially. You'll learn to work with real-world vector data including watersheds, building footprints, streams, and infrastructure. These skills are essential for flood risk assessment, watershed analysis, infrastructure screening, and any H&H work requiring geographic context.

## Learning Objectives

By the end of this module, you will be able to:

- Load and work with vector data formats (GeoJSON and Shapefiles)
- Understand coordinate reference systems (CRS) and ensure spatial data alignment
- Visualize spatial data with both static maps and interactive web maps
- Perform spatial operations (clip, buffer, intersect, spatial join)
- Calculate geometric properties (area, distance, length)
- Answer engineering questions like "What's at risk?" and "What's in this watershed?"
- Create professional maps with legends, labels, and appropriate styling
- Use AI assistants to understand and extend spatial analysis workflows

## Lessons

**Lesson 1: Introduction to Vector Data**
- Mental models: understanding spatial data as "smart drawings" with attributes
- Vector data types: points, lines, and polygons for H&H applications
- Loading GeoJSON and Shapefile formats
- Coordinate reference systems (CRS) and projection management
- Basic visualization with matplotlib and interactive maps with Folium
- Spatial operations: clip, buffer, and overlay
- Real-world analysis: identifying buildings at risk in watersheds
- Professional cartography: creating publication-ready maps

## Prerequisites

- Completion of Module 1 (Python fundamentals, Colab setup)
- Completion of Module 2 (Time series analysis with pandas)
- Google account (for Colab access)
- Basic understanding of DataFrames and data filtering
- No prior GIS or spatial analysis experience required

## Data Files

This module uses real spatial datasets from Wyoming that demonstrate typical H&H workflows:

| File | Description |
|------|-------------|
| `Wyoming_building_footprint_Selected.geojson` | Building footprint polygons representing infrastructure at risk |
| `NHD__Watershed_Boundaries_HUC_12_Selected.zip` | HUC-12 watershed boundary polygons from the National Hydrography Dataset |

## Getting Started

1. Open the notebook `03_01_Introduction_to_Vector_Data.ipynb` in Google Colab
2. Download the data files from the course GitHub repository
3. Upload the files to Colab when prompted
4. Work through each section sequentially, running all code cells
5. Use the provided AI prompts when you need help understanding or modifying code
6. Complete the practice exercises at the end to reinforce your learning

## Key Concepts

### Vector Data Types
The three fundamental spatial data types used in H&H engineering:
- **Points**: Gauge stations, outfalls, wells, sampling locations
- **Lines**: Streams, pipes, channels, flowpaths
- **Polygons**: Watersheds, buildings, flood zones, land parcels

### Coordinate Reference Systems (CRS)
The most important concept for accurate spatial analysis. All spatial datasets must be in the same CRS to perform operations correctly:
- **Geographic CRS** (EPSG:4326): Latitude/longitude coordinates, used for web mapping
- **Projected CRS** (e.g., EPSG:32613): Meter-based coordinates for accurate area/distance calculations
- Always check CRS with `.crs` and align with `.to_crs()` before analysis

### Spatial Operations
Geographic equivalents of data filtering and joining:
- **Clip**: Extract features within a boundary (e.g., buildings in a watershed)
- **Buffer**: Create zones around features (e.g., 100m around a stream)
- **Overlay**: Combine layers (intersect, union, difference)
- **Spatial Join**: Join attributes based on location

### GeoJSON vs Shapefile
Two common spatial data formats:
- **GeoJSON**: Single human-readable text file, web-friendly, good for smaller datasets
- **Shapefile**: Multiple files (.shp, .dbf, .shx, .prj) that must stay together, industry standard, efficient for large data

## Using AI Assistants

This module includes **🤖 AI Assistant Prompts** throughout. As you learn spatial analysis, use your AI assistant to:

- Explain complex spatial operations step by step
- Debug coordinate system issues
- Understand geometry manipulations
- Create custom spatial analysis workflows for your projects
- Optimize code for performance

**Sample prompts included in the lesson:**
- "Can you explain what this code cell is doing, line by line?"
- "Why do we reproject the data to EPSG:4326 before using Folium?"
- "What would happen if I removed or changed this line of code?"

## Practice Exercises

The lesson includes 4 exercises ranging from basic to advanced:

1. **Watershed Area Ranking** - Calculate and sort watershed areas
2. **Multi-Watershed Analysis** - Analyze building counts across multiple watersheds
3. **Buffer Analysis** - Create buffers and find spatial intersections
4. **Professional Map** - Create publication-ready cartography

## Key Takeaways

- Vector data combines geometry (where) with attributes (what) in a single structure
- Coordinate reference systems must be aligned before any spatial operation
- GeoPandas extends pandas with spatial capabilities - familiar syntax, spatial power
- Spatial operations are geographic filters answering "where" questions
- Start with simple visualizations, build to complex analysis
- Interactive maps (Folium) are excellent for exploration and stakeholder communication

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "CRS mismatch" error | Use `.to_crs()` to align all datasets to the same coordinate system |
| Shapefile won't load | Ensure all component files (.shp, .dbf, .shx, .prj) are uploaded together as a ZIP |
| Map doesn't display | Check that geometries are valid with `.is_valid` |
| Area calculations seem wrong | Verify you're using a projected CRS (meters), not geographic (degrees) |
| Interactive map not rendering | Ensure data is reprojected to EPSG:4326 before creating Folium map |

## Next Steps

After completing this module, you'll be ready for:
- **Module 4**: Raster data analysis (DEMs, precipitation grids, slope)

The combination of vector (Module 3) and raster (Module 4) data provides a complete spatial toolkit for H&H engineering.

## Engineering Applications

Skills from this module directly apply to:
- Flood risk screening (structures in floodplains)
- Watershed characterization (land use, impervious area)
- Infrastructure inventory (pipes, culverts, outfalls within project areas)
- Impact assessment (development footprint in sensitive areas)
- Site selection (optimal locations based on multiple spatial criteria)
- Regulatory compliance (setbacks, buffers, protected areas)

## Resources

- [GeoPandas Documentation](https://geopandas.org/) - Official GeoPandas reference
- [Shapely User Manual](https://shapely.readthedocs.io/) - Geometric operations
- [Folium Documentation](https://python-visualization.github.io/folium/) - Interactive maps
- [EPSG.io](https://epsg.io/) - Coordinate system reference
- [USGS National Map](https://www.usgs.gov/programs/national-geospatial-program/national-map) - Download watershed and hydrography data
- Course discussion forum for H&H-specific spatial questions

## Your Spatial Analysis Toolkit

Essential operations you'll use in every spatial analysis:

```python
# Load data
gdf = gpd.read_file('data.geojson')

# Check and align coordinate systems
gdf.crs                          # View current CRS
gdf = gdf.to_crs('EPSG:32613')  # Project to UTM Zone 13N

# Spatial operations
gpd.clip(buildings, watershed)   # Clip features by boundary
gdf.buffer(100)                  # Create 100m buffer
gpd.overlay(gdf1, gdf2, 'intersection')  # Intersect layers

# Calculate properties
gdf.geometry.area                # Area (in CRS units)
gdf.geometry.length              # Length for lines
gdf.geometry.centroid            # Center points

# Visualization
gdf.plot()                       # Quick static map
gdf.explore()                    # Quick interactive map
```

Keep exploring, keep mapping! 🗺️
