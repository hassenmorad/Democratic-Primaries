# Analyzing Democratic Primary Polls

This repository contains files collected & created while analyzing Democratic primary poll data. These are key questions I sought to answer in the articles below: 
- Was calling landline numbers was the main method of reaching voters?
- Did DNC approved polls differ from other polls in any significant ways? 

#### [Addressing the "Landline Only" Polling Myth]()
#### [Are DNC Approved Polls Chosen Fairly?]()

## Workflow Summary:
1. Collection- I scraped data from [FiveThirtyEight's](https://projects.fivethirtyeight.com/2020-primaries/democratic/) collection of primary poll data (**polls_scraping_cleaning.py**)
2. Cleaning- I removed duplicate records (e.g. if FiveThirtyEight included a record for Likely Voters (LV) and another for Registered Voters (RV) from the same poll, I only included the record containing results for RV). I also added data on each poll's data collection methods. Both of these steps were done manually in Excel, resulting in these two files: **national_polls_duplicates_removed.csv** & **state_polls_duplicates_removed.csv**
3. Visualization- Initially I created charts using Altair, but decided later to create the same charts using Data Wrapper (which apeared in the articles).
