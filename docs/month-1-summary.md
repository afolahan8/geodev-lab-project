# Month 1 summary

## Question
Which residential areas in Alimosho LGA, Lagos State, are more than 500 metres from a paved road, and where are the major accessibility gaps?

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
- Pattern:

## What surprised me
- Only about 7.6% of the road features carry a `paved` value (1,743 of 23,019). Many roads have an empty surface value, so the map may overstate the gaps if some of those roads are in fact paved.
- About 38% of buildings sit beyond 500 m of a paved road, which is a large share, and it depends heavily on the point above.
- I first projected to EPSG:32632, the wrong zone for Alimosho, and noticed only because the map grid showed negative eastings. I then moved to EPSG:32631.

## What data I still need
- Surface information for the roads with empty values, or a second source (for example OSM `surface=*`) to compare against.
- A way to separate residential buildings from other uses, since the footprints do not say.
- Population per settlement, to turn area uncovered into people uncovered.
- A road network for travel distance, since straight-line distance is a simplification.
- The definition of the GRID3 `ma_class` field, which I have not used.

## Limitations, stated plainly
- Roads with no surface value are treated as not paved.
- Buildings include non-residential structures, so "residential area" means built-up area.

## Credits
Boundaries, roads, settlements: GRID3 Nigeria. Buildings: © OpenStreetMap contributors.
