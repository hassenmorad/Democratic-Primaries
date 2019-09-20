# Analyzing Democratic Primary Polls

This repository contains files collected & created while analyzing Democratic primary poll data. These are key questions I sought to answer in the articles below: 
- Was calling landline numbers was the main method of reaching voters?
- Did DNC approved polls differ from other polls in any significant ways? 

#### [Addressing the "Landline Only" Polling Myth]()
#### [Are DNC Approved Polls Chosen Fairly?]()

## Workflow Summary:
1. Collection- I scraped data from [FiveThirtyEight's](https://projects.fivethirtyeight.com/2020-primaries/democratic/) collection of primary poll data (**polls_scraping_cleaning.py**)
2. Cleaning- I removed duplicate records and added data on each poll's data collection methods (this work was done manually in Excel- **national_polls_duplicates_removed** & **state_polls_duplicates_removed**)
3. Visualization- Initially I created charts using Altair, but decided later to create the same charts using Data Wrapper (which apeared in the articles).
