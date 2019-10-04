import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import unicodedata

all_polls_df = pd.DataFrame()  # Will loop and concat each state polls df (and national) to this
base_url = 'https://projects.fivethirtyeight.com'

# Identifying url for each page containing individual state poll results (as well as the page containing national poll results)
response = requests.get('https://projects.fivethirtyeight.com/2020-primaries/democratic/alabama/')
soup = BeautifulSoup(response.text,'html.parser')

states = soup.find_all('option')  # Also includes the National option element
for state in states[1:]:  # Skipping the 1st of 2 National option elements)
    state_url = state['value']

    # State (& National) URL
    url = base_url + state_url
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    state_name = soup.find('option', selected=True).text

    # Extracting table column headings
    table_header = soup.find('thead')
    cols = table_header.find_all('th')
    columns = [col.get_text() for col in cols[1:]]  # Skipping first element (empty)
    columns.insert(3, 'Voter_Type')
    columns.insert(4, 'Pollster_Grade')


    # Extracting row data
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr', class_='visible-row')

    all_rows = []
    for row in rows:
        row_data = []
        date = row.find('div', class_='date-wrapper').get_text()
        pollster_name = row.find('div', class_='pollster-container').find_all('a')[-1].get_text()
        sample_size = row.find('td', class_='sample').get_text()
        voter_type = row.find('td', class_='sample-type').get_text()
        pollster_grade = row.find('div', class_='gradeText')
        poll_results = row.find_all('td', class_='hide-mobile value')
        
        # Extracting values for: date, pollster, sample size, voter type (which don't contain any missing values)
        no_missing_list = []
        non_poll_values = [date, pollster_name, sample_size, voter_type]
        for non in non_poll_values:
            no_missing_list.append(non)

        # Pollster grade 
        grade_list = []
        try:
            value = pollster_grade.get_text()
        except:
            value = None
        grade_list.append(value)
        
        
        # Extracting poll results (for each candidate)
        poll_list = []
        for poll in poll_results:
            try:
                value = poll.get_text()
            except:
                value = None
            poll_list.append(value)

        row_data += (no_missing_list + grade_list + poll_list)
        all_rows.append(row_data)

    # Creating state DF
    df = pd.DataFrame(all_rows)
    df.columns = columns[:-1]
    df['Region'] = np.full(len(df), state_name)  # Named it "Region" instead of "State" b/c national polls included as well

    all_polls_df = pd.concat([all_polls_df, df], sort=False)

##########################################################################################################################
# *Cleaning Scraped Data

scraped_data = all_polls_df.copy()
scraped_data.Dates = [unicodedata.normalize("NFKD", string) if '\xa0' in string else string for string in scraped_data.Dates]

# Creating Poll End Date Column (to sort records)
end_dates = []
for date in scraped_data.Dates:
    if '-' not in date:
        end_dates.append(date)
        continue
    else:
        dates = date.split('-')
        try:
            int(dates[1][0])  # i.e. begins & ends in the same month
            beg_month = dates[0][:3]
            end_day_year = dates[1]
            end_dates.append(beg_month + ' ' + end_day_year)
        except:
            end_dates.append(dates[1])  # i.e. ends in the following month

scraped_data['Poll_End_Date'] = pd.to_datetime(end_dates)
scraped_data = scraped_data.sort_values('Poll_End_Date', ascending=False).reset_index(drop=True)    

# Keeping active candidates only
active_cols = ['Dates', 'Region', 'Pollster', 'Sample', 'Voter_Type', 'Pollster_Grade', 'Biden', 'Sanders', 'Harris', 
               'Warren', 'Buttigieg', 'Booker', 'Yang', 'Williamson', "O'Rourke", 'Delaney', 'Castro',
               'Gabbard', 'Klobuchar', 'Steyer', 'Poll_End_Date']
scraped_data = scraped_data[active_cols]
scraped_data = scraped_data.replace({'':-10}).fillna(-10)  # Temp replacement for missing values (in order to convert poll values to integers)
scraped_data['Pollster_Grade'] = scraped_data['Pollster_Grade'].replace({-10:'Missing'})

cand_cols = active_cols[6:-1]
scraped_data[cand_cols] = scraped_data[cand_cols].astype(str)

# Removing '%' from poll results & converting to integers (missing values are now indicated by -1 instead of -10)
for col in cand_cols:
    scraped_data[col] = scraped_data[col].apply(lambda x:x[:-1]).astype(int)

scraped_data = scraped_data.sort_values(['Poll_End_Date', 'Pollster'], ascending=[False, True])
scraped_data.to_csv('scraped_polls.csv', index=False)