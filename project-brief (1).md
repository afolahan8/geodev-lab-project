# My project brief

## The question
Which residential areas in Alimosho LGA are located more than 500 metres from a paved road, and where are the major accessibility gaps?

## Why it matters
Alimosho is Lagos State's largest and most populous LGA, and road access shapes daily life across it — commuting, emergency response, deliveries, ride-hailing reach. A local planner, a resident, or a business deciding where to operate could use this to see which residential pockets are cut off from the paved road network and where investment in road upgrades would help most.

## The data I need
- Roads with highway and surface tags — OSM via QuickOSM (or HDX Nigeria roads extract, clipped to Alimosho, if QuickOSM times out on the full LGA) — extracted for the Alimosho extent
- Residential building footprints or settlement extent — OSM (building=*) or GRID3 settlement extents — size TBD
- LGA boundary for Alimosho, to clip everything to the study area — GRID3 — https://data.grid3.org — GeoPackage — size TBD

## Where each dataset comes from
- Roads: OpenStreetMap, extracted via QuickOSM in QGIS, key `highway`, checking the `surface` tag on each feature to separate paved from unpaved. Given Alimosho's size, this may need to be queried one tag/section at a time, or pulled from the HDX Nigeria roads themed extract and clipped afterwards.
- Buildings/settlement extent: OpenStreetMap `building=*` tag via QuickOSM, or GRID3 settlement extents if OSM building coverage is too sparse.
- Boundary: GRID3 NGA Operational Wards or LGA boundaries, data.grid3.org — need to confirm Lagos State ward coverage; fall back to the LGA boundary layer if not covered.

## What I would build
A map showing residential areas more than 500 m from a paved road across all of Alimosho, with the accessibility gaps highlighted, and a note on how much of the road network actually has a usable surface tag (since that tag is often incomplete in OSM).

## Known limitations, stated up front
- An earlier idea for this project was electricity access in the same area. No open, downloadable electricity grid dataset exists for Ikeja Electric's service area, so that question was dropped.
- A related, earlier-considered question — which wards are more than 2 km from a health facility — is parked for later, not abandoned.
- The study area was widened from Ayobo-Ipaja alone to the whole of Alimosho LGA for versatility. Alimosho is Lagos's largest and most populous LGA, so expect larger file sizes and possible QuickOSM timeouts; may need to query in parts or use a pre-clipped HDX extract instead.
- Surface tagging in OSM is often incomplete (in the pack's own worked example, only ~18% of roads carried a surface tag). Week 1's job is to check how bad this is for Alimosho specifically, since it decides whether "paved vs unpaved" can be answered reliably at all, or only for a subset of roads.
