"""
Created on: Thu 26 May 2020
Author: Preeti 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# WIKIPEDIA Bright STARS DATA URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

#make empty list of scraped_data



# Define Data Scrapping Method
def scrape():
               
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # VERY IMP: The class "wikitable" and <tr> data is at the time of creation of this code. 
        # This may be updated in future as page is maintained by Wikipedia. 
        # Understand the page structure as discussed in the class & perform Web Scraping from scratch.

        # Find <table>
        bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        
        # Find <tbody>
        table_body = bright_star_table.find('tbody')

        # Find <tr>
        table_rows = table_body.find_all('tr')

        # Get data from <td>
        for row in table_rows:
            table_cols = row.find_all('td')
            # print(table_cols)
            
            

            for col_data in table_cols:
                # Print Only colums textual data using ".text" property
                # print(col_data.text)

                # Remove Extra white spaces using strip() method
                data = col_data.text.strip()
                # print(data)

                

            # Append data to star_data list
            


       
# Calling Method    
scrape()

################################################################

# IMPORT DATA to CSV


print(stars_data)


# Define Header


# Define pandas DataFrame   


#Convert to CSV

