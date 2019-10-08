# Mapping U.S. Race Demographics

This repository contains files collected & created while mapping U.S. race demographics. These data are the foundation for  multiple analyses. 

The first question I'm exploring is how different racial groups vary in supporting Democratic presidential candidates. I'll present the data 
The most straightforward way to measure a candidate's popularity among a racial group is to look at polling breakdowns. Another means of gauging this is by analyzing financial contributions to a campaign. Total quarterly fundraising figures are a decent indicator of overall appeal; I was curious to extract a few more layers of insight. First, I wanted to recreate [this map](https://blog.mapbox.com/how-the-nyt-mapped-every-dollar-24ae4873ec78) by the New York Times with more recent donation data. I also wanted to measure candidate support among different racial groups based on their donations.

Methodology for Measuring Support:
- Areas w/ over 40% of people from a certain race- total number of donations to candidate and/or total donation amount
- Zip codes are probably too granular- need to determine county

## Workflow Summary:
1. Collection
    - [**Demographics**](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk): 2017 American Community Survey (ACS) data on the percentage of population comprising various racial groups.
    - [**Zip Code Cities**](https://simplemaps.com/data/us-zips): Contains city name for each zip code, which I needed since ACS data didn't include city names.
    - **Zip Code Boundaries Shapefile**(https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html): for mapping in Mapbox.
    - **Campaign Donation Data**: FEC records of individual donations to Democratic presidential campaigns.
2. Cleaning:
    - 
3. Visualization- Mapped in Mapbox. Tutorial on steps taken is forthcoming.
