## Week 3

## CRS chosen and why

- **Chosen:** EPSG:32631 (WGS 84 / UTM zone 31N).
- **Why:** Alimosho lies at about 3.2°E, inside UTM zone 31N (0° to 6°E). The question uses a 500 m threshold, so measurements must be in metres. EPSG:4326 measures in degrees, which makes buffer distances and areas meaningless.
- All source layers arrived in EPSG:4326.
- **Area check:** Alimosho in the projected layer = [184.5180438316502] km²,****

## What I reprojected and what I clipped

| Layer                   | Source                                              | Clipped to                             | Reprojected to |
| ----------------------- | --------------------------------------------------- | -------------------------------------- | -------------- |
| Boundary (`study_area`) | GRID3 NGA_LGA_Boundaries, `lganame` = Alimosho      | n/a (selected from the national layer) | EPSG:32631     |
| Roads                   | GRID3_NGA_roads                                     | Alimosho boundary                      | EPSG:32631     |
| Buildings               | HOT OSM Nigeria buildings (MultiPolygon layer only) | Alimosho boundary                      | EPSG:32631     |
| Settlements             | GRID3_NGA_settlement_extents                        | Alimosho boundary                      | EPSG:32631     |

- Only the MultiPolygon buildings layer was used. The point (2,879), line (12) and geometry collection (1) layers are not footprints.
- Roads were clipped onto the alimosho boundary layer that has been reprojected, same nas the buildings and settlements layer
- Raw downloads in `data/raw/` were not edited.

### The five quality checks

| #    | Check                            | Roads (23,019 lines)                                                                                                                                                                                                    | Buildings (331,047 polygons)                                                                                                                     |
| :--- | :------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Coordinate system                | EPSG:32631                                                                                                                                                                                                              | EPSG:32631                                                                                                                                       |
| 2    | Null or empty values             | The surface column holds "paved", "unpaved" and empty values. Paved: [A], Unpaved: [B], Empty: [C] ([C + 23,019 = 100%]). Empty values are blank text, not nulls, and are treated as "surface unknown", not as unpaved. | No attributes are needed for the analysis. Geometry only. Null or empty geometries: [number, expected 0].                                        |
| 3    | Duplicate Features               | Delete duplicate geometries removed [N] of 23,019. [Fixed / none found.]                                                                                                                                                | Delete duplicate geometries removed [N] of 331,047. [Fixed / none found.]                                                                        |
| 4    | Geometry validity                | Check validity. [N] invalid. [Fixed with Fix geometries / none geometries / none found.]                                                                                                                                | Check validity. [N] invalid. [Fixed with Fix geometries / none found.]                                                                           |
| 5    | Coverage of the whole study area | Roads extend across the study area. Checked on satellite imagery in [areas]. Street names are mostly missing, which does not affect this analysis. Gaps: [none seen / where].                                           | Footprints match the imagery closely in [area checked]. [Add a count, for example "11 on my street, 11 in the data".] Gaps: [none seen / where]. |  | Footprints match the imagery closely in [area checked]. [Add a count, for example "11 on my street, 11 in the data".] Gaps: [none seen / where]. |

### Other observations
- **Positional accuracy:** Roads appear to align with visible roads and no systematic offset was noticed. Visual check only.
- **Fitness for purpose:** Roads can answer the paved-road question where the surface is known. Roads with an empty surface will be reported separately instead of guessed. Buildings show where structures are but not whether they are residential, so "residential area" is represented by built-up area, which includes some non-residential buildings.

## Problems found, and what I did

| Problem                                                        | Decision                                                                |
| -------------------------------------------------------------- | ----------------------------------------------------------------------- |
| The national roads file (about 2 GB) was too slow to work with | Extracted Alimosho only and removed the national layer from the project |
| Save error from typing a relative file path                    | Used the browse button to save to the full path                         |
| Some road surface values are empty                             | Flagged. Treated as unknown, not unpaved                                |
| Buildings do not distinguish residential from other uses       | Flagged. Results describe built-up areas                                |
| Road names are missing                                         | Not fixed, because names are not used in the analysis                   |

## Where the analysis-ready file lives

- `data/processed/alimosho_analysis_ready.gpkg` (113 MB), containing `study_area`, `roads` and `buildings`, all in EPSG:32631.
- **GitHub note:**  Geopackage analysis file is held locally because of size.
