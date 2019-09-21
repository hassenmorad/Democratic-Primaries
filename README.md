# Analyzing Democratic Primary Polls

This repository contains files collected & created while analyzing Democratic primary poll data. These are key questions I sought to answer in the articles below: 
- Was calling landline numbers the main method of reaching voters?
- Did DNC approved polls differ from other polls in any significant ways?
- How do candidates compare w/ regards to momentum in key metrics?

#### [Addressing the "Landline Only" Polling Myth]()
#### Are DNC Approved Polls Chosen Fairly? (coming soon)

## Workflow Summary:
1. Collection
    - I scraped data from [FiveThirtyEight's](https://projects.fivethirtyeight.com/2020-primaries/democratic/) collection of primary poll data (**polls_scraping_cleaning.py**)
2. Cleaning (in excel)
    - I removed duplicate records (e.g. if FiveThirtyEight included multiple records for the same poll, I only included the record containing results for likely voters- LV). 
    - I also added columns on each poll's method(s) of reaching voters, based on what was explained in it's methodology section (I reached out to pollsters for data if they were missing- about 1/2 responded). The resulting files are: **national_polls_duplicates_removed.csv** & **state_polls_duplicates_removed.csv**
3. Visualization- Initially I created charts using Altair, but decided later to create the same charts using Data Wrapper (which apeared in the articles).
