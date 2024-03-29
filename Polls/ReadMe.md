# Analyzing Democratic Primary Polls:
Issues Explored:
- Are poll participants reached primarily through landline numbers? ([Article](https://medium.com/@hassen.morad/addressing-the-landline-only-polling-myth-473dbb6d46bd))
- Are the DNC's polling criteria fair? ([Article](https://medium.com/@hassen.morad/shedding-light-on-dnc-approved-polls-773947e464e3))

## Workflow Summary:
1. Collection
    - I scraped data from [FiveThirtyEight's](https://projects.fivethirtyeight.com/2020-primaries/democratic/) collection of primary poll data (**polls_scraping_cleaning.py**)
2. Cleaning (in excel)
    - I removed duplicate records (e.g. if FiveThirtyEight included multiple records for the same poll, I only included one record based on the following ranking: LV, RV, V, A); I kept all records of the same poll if it was conducted in different states. 
    - I also added columns on each poll's method(s) of reaching voters, based on what was explained in it's methodology section (I reached out to pollsters for data if they were missing- about 1/2 responded). The resulting file is: **scraped_polls_duplicates_removed.csv**
    - I updated the list of polls periodically (**Updating Polls.ipynb**)
3. Visualization- Initially I created charts using Altair, but decided later to create the same charts using Datawrapper (which apeared in the articles).
