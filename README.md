# My GeoDev Lab Africa project
# Paved road accessibility in Alimosho LGA, Lagos State

A GeoDev Lab Africa project (Cohort One), built over twelve months. This repository holds Month 1: the question, the data, the preparation and the first analysis.

## The question
Which residential areas in Alimosho Local Government Area, Lagos State, are more than 500 metres from a paved road, and where are the major accessibility gaps?

Which residential areas in Alimosho Local Government Area, Lagos State,
are more than 500 metres from a paved road, and where are the major accessibility gaps?

Built over twelve months with GeoDev Lab Africa, Cohort One.

See `Project-brief.md` for the full brief.

## Result so far
About 38% of buildings in Alimosho LGA (126,816 of 331,047) are more than 500 m from a road recorded as paved. [Add one sentence on where the gaps are, for example "They are concentrated along the southern edge and the western strip".] [Add the settled-area figure: X km² of Y km² of settlements, Z%.]

**Read this with its caveat:** only about 7.6% of road features (1,743 of 23,019) carry a `paved` value. Roads with no surface information are not counted as paved, so the figures may overstate the gaps. Distances are straight-line, not travel distance.

<img width="3507" height="2480" alt="Settlements more than 500 m from a paved road, Alimosho LGA, Lagos State" src="https://github.com/user-attachments/assets/743b56cd-c49d-405e-8eea-6d033d8546b0" />


## Where to find each week's work

| Week | What | Where |
|---|---|---|
| 1 | Project brief, with a source link for every dataset | [project-brief.md](project-brief.md) |
| 2 | Data notes: what I downloaded | [week_2_data-notes.md](week_2_data-notes.md) (Part 1) |
| 3 | Prepared data and the five quality checks | [week_3_data-notes.md](week_3_data-notes.md) (Part 2) and [data/](data/README.md) |
| 4 | Analysis, map and summary | [month-1-summary.md](month-1-summary.md) and [the map](maps/alimosho_settlements_beyond_500m.png) |

## Method in one paragraph
Paved roads were buffered by 500 m (dissolved), and the buffer was subtracted from the settlement extents to leave the parts more than 500 m away. Buildings outside the buffer were then extracted. All analysis layers were reprojected to EPSG:32631 (UTM zone 31N) so distances are in metres.

## Data and credits
- Boundary, roads and settlement extents: GRID3 Nigeria.
- Buildings: HOT OSM Nigeria export, © OpenStreetMap contributors.

Full source links, versions and dates are in [project-brief.md](project-brief.md) and [data-notes.md](data-notes.md).
