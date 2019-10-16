# Analyzing Democratic Primary Data

This repository contains files collected & created while analyzing Democratic presidential primary data (all files related to polls are in the [Polls](https://github.com/hassenmorad/Democratic-Primaries/tree/master/Polls) folder). These are some key questions I explored in the articles below: 
- Was calling landline numbers the main method of reaching voters?
- Are DNC polling criteria fair (analyzing DNC-approved polls)?
- Does mapping candidate donations reveal any patterns of support from certain racial groups or regions?
- How do candidates compare w/ regards to momentum in key metrics?

#### [Addressing the "Landline Only" Polling Myth](https://medium.com/@hassen.morad/addressing-the-landline-only-polling-myth-473dbb6d46bd?source=friends_link&sk=b4f11605e33fff99f8d1b93cf0ec27ea)
#### [Shedding Light on DNC-Approved Polls](https://medium.com/@hassen.morad/shedding-light-on-dnc-approved-polls-773947e464e3)
#### Campaign Donations Mapping Analysis (in progress)
#### Democratic Candidates Momentum Tracker (coming soon)

--------------------------------------------------------------------
## Workflow Summary (for poll data):
1. Collection
    - I scraped data from [FiveThirtyEight's](https://projects.fivethirtyeight.com/2020-primaries/democratic/) collection of primary poll data (**polls_scraping_cleaning.py**)
2. Cleaning (in excel)
    - I removed duplicate records (e.g. if FiveThirtyEight included multiple records for the same poll, I only included one record based on the following ranking: LV, RV, V, A); I kept all records of the same poll if it was conducted in different states. 
    - I also added columns on each poll's method(s) of reaching voters, based on what was explained in it's methodology section (I reached out to pollsters for data if they were missing- about 1/2 responded). The resulting file is: **scraped_polls_duplicates_removed.csv**
3. Visualization- Initially I created charts using Altair, but decided later to create the same charts using Data Wrapper (which apeared in the articles).
