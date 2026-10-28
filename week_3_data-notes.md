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


# week 4

## Operation and why
I buffered the paved roads by 500 m (dissolved into one shape), then took the **difference** between the settlement extents and that buffer, which leaves only the parts of each settlement more than 500 m from a paved road. I then extracted the buildings that fall outside the buffer (predicate: disjoint).

I chose a buffer and difference because the question has a distance in it ("more than 500 m from") and asks for what lies outside that distance, not inside it.

- **CRS:** [CONFIRM every analysis layer reads EPSG:32631 in Properties, Information, then keep this line.] EPSG:32631 (UTM zone 31N), because Alimosho lies at about 3.2°E, inside zone 31N, and the buffer distance must be in metres.
- **Paved roads:** roads whose surface column reads `paved`. Roads with an empty surface value are **not** counted as paved.

## What I expected
I did not write a prediction before the first run, which is a gap in my process. [Keep the next sentence only if you wrote it before looking at the rerun results.] For the rerun in the corrected zone, I expected the counts to stay within about 1% of the first run, because the scale difference between the two zones is under 1%.

## What I got

| Step | Layer | Features |
|---|---|---|
| 1 | Paved roads | 1,743 (of 23,019 roads, about 7.6%) |
| 2 | 500 m buffer (dissolved) | 1 |
| 3 | Settlements beyond 500 m | 3,467 |
| 4 | Buildings beyond 500 m | 126,816 (of 331,047), about 38% |

- Uncovered settlement area: 69.9508km² of 166,153km² (42.1%).
- Pattern: ## tbc

## What surprised me
- Only about 7.6% of the road features carry a `paved` value (1,743 of 23,019). Many roads have an empty surface value, so the map may overstate the gaps if some of those roads are in fact paved.
- About 38% of buildings sit beyond 500 m of a paved road, which is a large share, and it depends heavily on the point above.
- I first projected to EPSG:32632, the wrong zone for Alimosho, and noticed only because the map grid showed negative eastings. I then moved to EPSG:32631.

## What data I still need
- Surface information for the roads with empty values, or a second source (for example OSM `surface=*`) to compare against.
- A way to separate residential buildings from other uses, since the footprints do not say.
- Population per settlement, to turn area uncovered into people uncovered.
- A road network for travel distance, since straight-line distance is a simplification.

## Limitations, stated plainly
- Roads with no surface value are treated as not paved.
- Buildings include non-residential structures, so "residential area" means built-up area.

## Credits
Boundaries, roads, settlements: GRID3 Nigeria. Buildings: © OpenStreetMap contributors.
