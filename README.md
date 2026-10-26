# Is there a barrow in Barrow?

**Read the post and explore the map:** https://tristan-hotham.github.io/barrow-in-barrow/

**Archived data and code:** [doi:10.5281/zenodo.23676162](https://doi.org/10.5281/zenodo.23676162)

Old English *beorg* meant a mound or a rounded hill and gives us the word barrow. This project tests 129 English places named from *beorg* against 6,100 scheduled burial mounds. Would the names lead you to the barrows?

## Headline results (barrows within 2 km, against local expectation)

| Element | Meaning | Places | Observed | Expected | Ratio | 95% interval |
|---|---|---:|---:|---:|---:|---|
| hlāw | mound, hill | 88 | 47 | 30.9 | 1.52 | 0.88–2.30 |
| burh | fortification | 356 | 273 | 207.0 | 1.32 | 0.89–1.84 |
| beorg / berg | mound, hill | 129 | 123 | 101.6 | 1.21 | 0.82–1.64 |
| hōh | hill-spur | 150 | 69 | 59.7 | 1.16 | 0.53–1.91 |
| dūn | hill | 396 | 260 | 232.9 | 1.12 | 0.86–1.40 |
| hyll | hill | 218 | 145 | 156.4 | 0.93 | 0.60–1.31 |
| bearu | grove | 43 | 33 | 53.5 | 0.62 | 0.19–1.10 |
| haugr (Old Norse) | mound, hill | 26 | 3 | 15.1 | 0.20 | 0.00–0.50 |

- *Beorg* places have about as many barrows nearby as places named after ordinary hills. So the word mostly meant "hill".
- KEPN glosses 12 *beorg* names as "burial-mound". Nine of them have no scheduled barrow within 2 km.
- Of the places called Barrow-something in KEPN, eight come from *bearu*, "grove", and only four from *beorg*.

## Method

1. Places come from the Key to English Place-Names (KEPN), using every place listed under each element. Each place is a single point.
2. Barrows are Historic England scheduled monuments whose names include barrow, tumulus, burial mound, round cairn or bowl cairn.
3. For each place I counted barrows within 1, 2 and 3 km. The expected count is the number within 30 km scaled by area, which controls for regional clustering.
4. Results are pooled per element as total observed divided by total expected. Intervals come from 2,000 bootstrap resamples of places.

Scheduled monuments are survivors. Ploughed-out barrows are missing, so this tests the names against surviving, protected mounds.

## Files

| Path | What it is |
|---|---|
| `analysis.py` | Counts and ratios. It needs the KEPN exports in `data/raw/` (see below). |
| `build_data.py` | Builds the JSON for the web page and `results/places_scored.csv`. |
| `data/raw/scheduled_barrows.csv` | NHLE scheduled monuments matching the barrow terms: list entry, name, easting, northing (EPSG:27700). Downloaded 26 October 2026. |
| `results/summary.csv` | Ratios by element at 1, 2 and 3 km, with intervals. |
| `results/places_scored.csv` | Each place with its element, coordinates, burial-mound gloss flag and barrow counts. Etymologies are not included; see KEPN. |
| `data/*.json`, `index.html` | The web page. |

To rerun, export KEPN's Advanced Search results for the elements berg, hlāw, haugr, bearu, dūn, hyll, hōh and burh as CSV. Save them as `data/raw/kepn_<element>.csv` with diacritics removed (for example `kepn_hlaw.csv`).

## Sources and licences

- **Place-names:** Key to English Place-Names, Institute for Name-Studies, University of Nottingham, https://kepn.nottingham.ac.uk/. Only names, elements and coordinates are reused.
- **Scheduled monuments:** National Heritage List for England © Historic England, Open Government Licence v3. Contains Ordnance Survey data © Crown copyright and database right.
- **Lidar (web map):** Environment Agency, OGL v3. **Base map:** © Esri.

Code is MIT licensed.

AI use: written with drafting, data and coding help from Claude (Anthropic).

Tristan Hotham, independent researcher, 2026.
