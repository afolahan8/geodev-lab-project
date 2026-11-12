# My GeoDev Lab Africa project
# Paved road accessibility in Alimosho LGA, Lagos State

A GeoDev Lab Africa project (Cohort One), built over twelve months. This repository holds Month 1: the question, the data, the preparation and the first analysis.

## The question
Which residential areas in Alimosho Local Government Area, Lagos State, are more than 500 metres from a paved road, and where are the major accessibility gaps?

Which residential areas in Alimosho Local Government Area, Lagos State,
are more than 500 metres from a paved road, and where are the major accessibility gaps?

Built over twelve months with GeoDev Lab Africa, Cohort One.

See `Project-brief.md` for the full brief.

 ## Month 1
 
## Result so far
About 38% of buildings in Alimosho LGA (126,816 of 331,047) are more than 500 m from a road recorded as paved. [Add one sentence on where the gaps are, for example "They are concentrated along the southern edge and the western strip".] [Add the settled-area figure: X km² of Y km² of settlements, Z%.]

**Read this with its caveat:** only about 7.6% of road features (1,743 of 23,019) carry a `paved` value. Roads with no surface information are not counted as paved, so the figures may overstate the gaps. Distances are straight-line, not travel distance.

<img width="3507" height="2480" alt="Settlements more than 500 m from a paved road, Alimosho LGA, Lagos State" src="https://github.com/user-attachments/assets/743b56cd-c49d-405e-8eea-6d033d8546b0" />


## Where to find each week's work

| Week | What | Where |
|---|---|---|
| 1 | Project brief, with a source link for every dataset | [project-brief.md](project-brief.md) |
| 2 | Data notes: what I downloaded | [week_2_data-notes.md](docsweek_2_data_notes.md) (Part 1) |
| 3 | Prepared data and the five quality checks | [week_3_data-notes.md](docs/week_3_data-notes.md) (Part 2) and [data/](data/README.md) |
| 4 | Analysis, map and summary | [month-1-summary.md](month-1-summary.md) and [the map](maps/alimosho_settlements_beyond_500m.png) |

## Method in one paragraph
Paved roads were buffered by 500 m (dissolved), and the buffer was subtracted from the settlement extents to leave the parts more than 500 m away. Buildings outside the buffer were then extracted. All analysis layers were reprojected to EPSG:32631 (UTM zone 31N) so distances are in metres.

## Data and credits
- Boundary, roads and settlement extents: GRID3 Nigeria.
- Buildings: HOT OSM Nigeria export, © OpenStreetMap contributors.

Full source links, versions and dates are in [project-brief.md](project-brief.md) and [data-notes.md](week_2_data_notes.md).

   ## Month 2: development environment and early Python

   **Week 5:** set up Python, VS Code and the terminal. hello.py runs. [hello.py](scripts/hello.py) runs. ([screenshot](screenshots/week_5.png))
   
   **Week 6:** set up the project with uv and added pandas. [check.py](check.py) prints the pandas version. ([pyproject.toml](pyproject.toml), [uv.lock](uv.lock), [screenshot](screenshots/week_6.png))

   **Week 7:**  Python basics on practice data. [analyse.py](analyse.py) reads [wards.csv](states.csv). ([screenshot](screenshots/week_7.png)), converts each area and classifies each ward, then displays the results.

   **Week 8:**  [inspect_data.py](scripts/inspect_data.py) summarises speed_estimate and length in my Alimosho paved roads data, [paved_roads.csv](docs/paved_roads.csv). ([screenshot](screenshots/week_8.png) and [screenshot](screenshots/week8.png))

   **Week 9:** [summary.py](week_9_summary.py) is the capstone: it runs read_rows, clean_values, summarise_values and summarise_all on my Month 1 paved roads data. ([screenshot](screenshots/week_9.png))

## Month 2 reflection

The idea that finally clicked this month was that a function has to use the inputs it is given: my Week 8 function ignored its filename and column arguments and summarised the same column twice, and fixing that showed me why Week 9's small functions with one job each are easier to trust. What is still fuzzy is how pyproject.toml, uv.lock and the virtual environment fit together, because I can run uv add and uv run but I struggled to work out what went wrong when the project would not build. My capstone shows that all 1,743 of my paved roads have both a length (averaging about 123 m, up to about 1,094 m) and a speed estimate (from 5 to 80 km/h, averaging about 49), so unlike the surface column, which was empty for most roads, these fields are complete for the paved roads I analysed. That makes them a good base for upgrading my Month 1 straight-line distance question to a travel-time one.
