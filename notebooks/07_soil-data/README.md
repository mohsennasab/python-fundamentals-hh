# Module 7: Soil Data for H&H Modeling with NRCS SSURGO

## Overview

This module teaches you how to pull official NRCS soil survey data (SSURGO) directly into Python, using the NRCS Soil Data Access (SDA) API. You will retrieve the soil properties that matter for hydrologic modeling, hydrologic soil group, saturated hydraulic conductivity (Ksat), soil texture, and available water capacity, for a single point and for an entire watershed. This module also doubles as an introduction to how a web API works, since the queries are written as raw requests rather than through a wrapper library.

Throughout the module you will see 🤖 callout boxes with concrete AI prompts. Use them to explain unfamiliar queries, debug a failed request, or extend the workflow to your own project data.

## Learning Objectives

By the end of this module, you will be able to:

- Explain how SSURGO organizes soil data into map units, components, and horizons, and why that structure matters for hydrology
- Explain what a web API request and response look like, and the difference between GET and POST
- Query the NRCS Soil Data Access API for a single point using WKT geometry
- Query soil properties across an entire watershed and aggregate them by component percentage and horizon depth
- Recognize and correct a common coordinate-axis-order problem in spatial web services
- Visualize hydrologic soil groups across a watershed
- Export traceable, model-ready soil summary tables
- Export the clipped SSURGO map unit polygons as a GeoPackage and a zipped shapefile for GIS use

## Lessons

**Lesson 1: Soil Data for H&H Modeling with NRCS SSURGO**

- Mental models: SSURGO as a filing cabinet of map units, components, and horizons
- How a web API works: requests, responses, JSON, status codes
- The Soil Data Access (SDA) service and why it fits a Colab-based workflow
- Point query: soil properties at a single location, with a real one-to-many result
- Watershed query: depth-weighted and component-weighted Ksat, plus dominant hydrologic soil group
- Visualization: mapping hydrologic soil group across a watershed, including a real coordinate axis-order gotcha
- Export: traceable, unit-labeled summary tables, plus the AOI soil polygons as GeoPackage and zipped shapefile
- SSURGO Portal and gNATSGO, introduced conceptually as alternatives for offline or large-area work

## Prerequisites

- Completion of Module 1 (Python fundamentals, Colab setup)
- Completion of Module 3 (vector data, coordinate reference systems, GeoPandas)
- Module 5 (API-based data retrieval) is helpful background, but this module explains API concepts from scratch
- Google account (for Colab access)

## Data Files

| File | Description |
|------|-------------|
| `NHD__Watershed_Boundaries_HUC_12_Selected.zip` | The same Wyoming HUC-12 watershed boundaries used in Module 3 |
| `sda_fallback_point_response.csv` | A saved point-query result, for reference if the live API is unavailable |
| `sda_fallback_watershed_response.csv` | A saved watershed-query summary result, for reference if the live API is unavailable |

All soil data in this module is retrieved live from the NRCS Soil Data Access API. The fallback CSVs are provided so you can inspect what a completed query result looks like if the live service is temporarily down.

## Getting Started

1. Open the notebook `07_01_soil_data_ssurgo.ipynb` in Google Colab.
2. Download `NHD__Watershed_Boundaries_HUC_12_Selected.zip` from this folder.
3. Run the notebook from the top. The early cells demonstrate a raw API request before anything else happens.
4. Upload the watershed ZIP file when prompted.
5. Work through each part sequentially, running all code cells.
6. Use the 🤖 prompt callouts to deepen your understanding as you go.
7. Try the practice exercises, including the AI-assisted challenge exercise, near the end.

## Key Concepts

### The SSURGO Hierarchy

| Level | Key | Analogy |
|---|---|---|
| Map unit | `mukey` | A drawer in a filing cabinet |
| Component | `cokey` | A folder inside the drawer |
| Horizon | `chkey` | A page inside the folder |

A point or a watershed intersects one or more map units. Each map unit can contain several components, weighted by `comppct_r`. Each component can contain several horizons at different depths, where properties like Ksat are actually recorded.

### Request and Response

An API request has an endpoint (a URL), a payload (in this module, a SQL query), and a method (POST, since the query can be long). The response comes back as JSON, with a status code indicating success (200) or failure (400, 500, and others).

### Aggregation Methods Used in This Module

- **Depth-weighted Ksat**: combines multiple horizons within a component, weighted by how thick each horizon is within a 0 to 100 cm window.
- **Component-weighted Ksat**: combines multiple components within a map unit, weighted by `comppct_r`.
- **Dominant-condition hydrologic soil group**: retrieved directly from NRCS's own `muaggatt` table, which has already computed the map-unit-level dominant condition.

### Unit Conversions

SSURGO stores Ksat in micrometers per second (µm/s). This module converts to inches per hour (multiply by 0.14173) and centimeters per hour (multiply by 0.36) for engineering use.

## Using AI Assistants

This module leans on AI assistance for two things: understanding queries written in raw SQL, and debugging failed API requests. You will find 🤖 prompt boxes covering:

- The difference between GET and POST requests.
- How `mukey`, `cokey`, and `chkey` connect map units, components, and horizons.
- How to interpret and use Ksat values responsibly in HEC-HMS parameterization.
- Building a reusable `get_soil_at_point(lat, lon)` function, in the challenge exercise.

## Key Takeaways

- Never report a SSURGO-derived value without stating how it was aggregated: dominant component, percentage-weighted, depth-weighted, or a combination.
- Ksat is a defensible starting point for infiltration modeling, not a calibrated final parameter.
- An inner join across map unit, component, and horizon tables can silently drop minor components that lack horizon data. Track and report how much of each map unit's area is actually represented.
- Coordinate axis order is a real, recurring source of bugs in geospatial web services. Always check bounds against something you already trust.
- SSURGO is survey-scale data, appropriate for screening-level work, not a substitute for site investigation on a design-level project.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Query returns an empty table | Confirm the point or watershed falls inside a mapped SSURGO area; check the SQL string for typos in table or column names. |
| Point query returns the wrong map unit | Check WKT coordinate order: `POINT(longitude latitude)`, not `POINT(latitude longitude)`. |
| Watershed query fails or times out | Increase the simplification tolerance on the watershed polygon before converting to WKT. |
| Component percentages do not sum to 100 | Expected when minor components without horizon data are dropped by an inner join; report `pct_represented` alongside any weighted value. |
| Map does not align with the watershed boundary | The WFS spatial service returns coordinates in (latitude, longitude) order; swap x and y before setting the CRS. |
| API request returns a non-200 status code | Print `response.status_code` and `response.text`; retry, or use the fallback CSVs in this folder. |

## Next Steps

- **Combine with Module 4.** Curve numbers require both land cover and hydrologic soil group. Module 4 covered the land cover half of that calculation; this module covers the soil half.
- **On your own.** Run this workflow on a watershed from a current project and compare the results against any calibration data you already have.
- **Large-area work.** If a project spans multiple counties or states, revisit the gNATSGO discussion near the end of the notebook.

## Resources

- [NRCS Soil Data Access](https://sdmdataaccess.sc.egov.usda.gov/) — API-based tabular and spatial soil data queries
- [Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/) — official interactive access to SSURGO data and standard downloads
- [SSURGO Portal](https://www.nrcs.usda.gov/resources/data-and-reports/ssurgo-portal) — desktop tool for building a local GeoPackage/SQLite SSURGO database
- [gNATSGO Soil Database](https://www.nrcs.usda.gov/resources/data-and-reports/gridded-national-soil-survey-geographic-database-gnatsgo) — seamless national raster soil database
- [SSURGO/STATSGO2 Metadata](https://sdmdataaccess.sc.egov.usda.gov/documents/TableColumnDescriptionsReport.pdf) — table names, field names, and definitions
