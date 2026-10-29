# Data notes: Alimosho road accessibility

Project: Which residential areas in Alimosho LGA, Lagos State, are more than 500 metres from a paved road?

# What I downloaded (Week 2)

Raw downloads are kept untouched in `data/raw/`. Anything I changed was saved to `data/processed/`.

| Dataset | Source and exact page link | Version and date | Downloaded | Format and size |
|---|---|---|---|---|
| LGA boundaries | GRID3 Nigeria, data.grid3.org | Operational LGA Boundaries, Sep 2025] | Oct 2026 | [GeoPackage, 5MB] |
| Roads | GRID3 Nigeria, data.grid3.org | Roads v1.0, March 2025] | Oct 2026 | [GeoPackage, 2.1GB, national] |
| Settlement extents | GRID3 Nigeria, data.grid3.org | v4.1 | Oct 2026 | [GeoPackage,  1.88GB] |
| Buildings | HOT OSM Nigeria export on HDX, https://data.humdata.org/dataset/hotosm_nga_buildings | Oct 2026 | Oct 2026 | [GeoPackage, 2.1GB, national] |

## What each one contains

**LGA boundaries (GRID3)**
- Polygons for every LGA. The name column is `lganame`. Alimosho was selected from it and saved as the study area.

**Roads (GRID3)**
- Alimosho extract: 23,019 lines.
- Columns: road surface, country, iso3, name, class, id, source id.
- The surface column holds `paved`, `unpaved` and empty values. The empty values are blank text, not nulls.
- Street names are mostly missing.

**Settlement extents (GRID3)**
- 8,313 polygon features in the Alimosho clip.
- Settlement locations also exist as 204 points (layer `point_settlement_beyond_500m`), downloaded from GRID3.

**Buildings (HOT OSM)**
- The file has four geometry layers: 2,879 points, 12 lines, 19,315,076 multipolygons and 1 geometry collection. Only the multipolygon layer (building footprints) was used.
- Alimosho extract: 331,047 footprints.
- Derived from OpenStreetMap, so coverage depends on what mappers have added.

## Problems met while downloading
- The national roads file (about 2 GB) made QGIS very slow. I extracted Alimosho only and removed the national layer from the project.
- The buildings file holds over 19 million footprints, so I zoomed to the study area before adding it, then extracted Alimosho.
