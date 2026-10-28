## Title

[OC] Is there a barrow in Barrow? The 129 English places named from Old English beorg, "mound", have about as many burial mounds nearby as places named after ordinary hills (Key to English Place-Names and 6,100 scheduled barrows from Historic England)

## Body (optional)

Old English beorg meant a mound or a rounded hill, and gives us the word barrow. I counted the scheduled burial mounds within 2 km of each of the 129 beorg places and compared that with what the local density of barrows would predict. Beorg places have 1.21 times the expected number, close to places named dūn, "hill" (1.12×), and hyll (0.93×), so the word mostly meant "hill". Only 27% of beorg places have any barrow within 2 km, and 9 of the 12 names glossed as "burial mound" have none, including Barrow in Rutland. Old Norse haugr, also "mound", does worse still: 3 barrows where 15 were expected. And eight places called Barrow come from bearu, "grove", not beorg.

Caveat: scheduled monuments are survivors, so barrows that have been ploughed out are missing, and the intervals are wide.

Interactive version: https://tristan-hotham.github.io/barrow-in-barrow/

## Source comment

Source: place-names, elements and coordinates from the Key to English Place-Names (Institute for Name-Studies, University of Nottingham, https://kepn.nottingham.ac.uk/), using every place listed under beorg, hlāw, haugr, bearu, dūn, hyll, hōh and burh. Burial mounds are the 6,100 scheduled monuments in the National Heritage List for England whose names include barrow, tumulus, burial mound, round cairn or bowl cairn, downloaded 26 October 2026 (© Historic England, Open Government Licence v3; contains Ordnance Survey data © Crown copyright and database right). The expected count for each place is the number of barrows within 30 km scaled by area; ratios are pooled per element, with 95% intervals from 2,000 bootstrap resamples of places. Outline of England from Office for National Statistics boundaries (Open Government Licence v3). Lidar on the interactive page: Environment Agency, Open Government Licence v3; base map © Esri.

Tools: Python (pandas, NumPy, GeoPandas, pyproj, matplotlib).

Interactive: https://tristan-hotham.github.io/barrow-in-barrow/
Blog post: https://blog.tristanhotham.com/2026/10/26/is-there-a-barrow-in-barrow/
Data and code: https://doi.org/10.5281/zenodo.23676162
