# Mapping U.S. Race Demographics
(project currently underway)
This repository contains files collected & created while analyzing presidential campaign contributions. 
It is built on a previous **[project mapping U.S. race demographics](https://github.com/hassenmorad/Race-Demographics)**.

A common way to measure a candidate's support among different demographics is to look at breakdowns in poll results. 
Perhaps a more concrete indication of support can be found in its financial contributions.
I decided to explore this question by recreating this [map published by the New York Times](https://blog.mapbox.com/how-the-nyt-mapped-every-dollar-24ae4873ec78)
with more recent donation data. Along with examining regional support, I added the layer of racial demographics to see if any interesting patterns emerged.

Methodology for Measuring Support:
- Areas w/ over 40% of people from a certain race- total number of donations to candidate and/or total donation amount
- Zip codes are probably too granular- need to determine county

## Workflow Summary:
1. Collection
    - [**Demographics**](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk): 2017 American Community Survey (ACS) data on the percentage of population comprising various racial groups.
    - [**Zip Code Cities**](https://simplemaps.com/data/us-zips): Contains city name for each zip code, which I needed since ACS data didn't include city names.
    - [**Zip Code Boundaries Shapefile**](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html): for mapping in Mapbox.
    - **Campaign Donation Data**: FEC records of individual donations to Democratic presidential campaigns.
2. Cleaning
    - Jupyter Notebook
3. Visualization
    - Mapped in Mapbox. Tutorial on steps taken is forthcoming.
