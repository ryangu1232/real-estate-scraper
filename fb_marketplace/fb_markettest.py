from splinter import Browser
from bs4 import BeautifulSoup as soup
import re
import pandas as pd
import time
import matplotlib.pyplot as plt
import csv

def write_word_to_csv(word):
    with open('words.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([word])

browser = Browser("chrome")

#make the search parameters
location = "sanfrancisco"
min_price = 0
max_price = 50000
days_listed = 30
type_of_lease = "sublease"
base_url = f"https://www.facebook.com/marketplace/{location}/search/?"

#displays the full url
url = f"{base_url}minPrice={min_price}&maxPrice={max_price}&daysSinceListed={days_listed}&query=sublease&exact=false"

browser.visit(url)

# Define the number of times to scroll the page
scroll_count = 10

# Define the delay (in seconds) between each scroll
scroll_delay = 0.1

# Loop to perform scrolling
for _ in range(scroll_count):
    # Execute JavaScript to scroll to the bottom of the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Pause for a moment to allow the content to load
    time.sleep(scroll_delay)

# Parse the HTML
html = browser.html

# Create a BeautifulSoup object from the scraped HTML
market_soup = soup(html, 'html.parser')

#puts the html data into a csv file for me to look at and visualize better [NOT USING RIGHT NOW]
#write_word_to_csv(market_soup)

# Check if HTML was scraped correctly
#browser.quit()

# Extract all the necessary info and insert into lists, below is a template for it
"""titles_div = market_soup.find_all('span', class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6")
titles_list = [title.text.strip() for title in titles_div]"""
#finds the description element [DONE]
description_div = market_soup.find_all('span', class_= "x1lliihq x6ikm8r x10wlt62 x1n2onr6")
description_list = [description.text.strip() for description in description_div]
#finds the prices [DONE]
prices_div = market_soup.find_all('span', class_="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x1lkfr7t x1lbecb7 x1s688f xzsf02u")
prices_list = [price.text.strip() for price in prices_div]
#finds the urls [NOT DONE]
"""urls_div = market_soup.find_all('a', class_="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv x1fey0fg")
urls_list = [url.get('href') for url in urls_div]"""
#finds the locations [NOT DONE]
"""location_div = market_soup.find_all('a', class_= "x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft")
location_list = [location.text.strip() for location in location_div]"""
#finds the class [PARTLY DONE]
imglink_div = market_soup.find_all('span', class_="xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3")
#imglink_list = [imglink.text.strip() for imglink in imglink_div]

imglink_list = []
for imglink in imglink_div:
    imgurl = imglink.find('img')["src"]
    imglink_list.append(imgurl)

print(imglink_list)

# Create a regular expression pattern to match city and state entries like "City, State"
pattern = re.compile(r'(\w+(?:-\w+)?, [A-Z]{2})')


#Goal: To be able to clean up the lists
"""
# Initialize an empty list to store adjusted mileage entries
price_list2 = []

# Iterate through the original mileage entries
for item in prices_list:
    # Append the current mileage entry to the adjusted list
    price_list2.append(item)
    
    # Check if the current mileage entry matches the pattern and there are at least two entries in the adjusted list
    if pattern.match(item) and len(price_list2) >= 2 and pattern.match(price_list2[-2]):
        # If the conditions are met, insert "0K km" in between the two consecutive city and state entries
        price_list2.insert(-1, '0K km')
print(price_list2)

# Extracted mileage list (separate from location and extract numeric values only)
# Define regular expressions to extract numeric mileage values in "K km" and "K miles" format
mileage_pattern_km = r'(\d+)K km'
mileage_pattern_miles = r'(\d+)K miles'

# Initialize an empty list to store cleaned mileage values
mileage_clean = []

# Iterate through the adjusted mileage entries
for item in price_list2:
    # Try to find a match for the "K km" format
    match_mileage_km = re.search(mileage_pattern_km, item)
    
    # Try to find a match for the "K miles" format
    match_mileage_miles = re.search(mileage_pattern_miles, item)
    
    # Check if either of the formats is found
    if match_mileage_km or match_mileage_miles:
        # If "K km" format is found, convert it to meters and append to the cleaned list
        if match_mileage_km:
            mileage_clean.append(int(match_mileage_km.group(1)) * 1000)
        # If "K miles" format is found, convert it to meters and append to the cleaned list
        else:
            mileage_clean.append(int(match_mileage_miles.group(1)) * 1600)


# Add all values to a list of dictionaries
vehicles_list = []

for i, item in enumerate(description_list):
    houses_dict = {}
    
    title_split = description_list[i].split()
    
    houses_dict["Description"] = title_split[0]
    houses_dict["Price"] = int(re.sub(r'[^\d.]', '', prices_list[i]))
    vehicles_list.append(houses_dict)
    
print(vehicles_list)

vehicles_df = pd.DataFrame(vehicles_list)

# Set the display option to ensure that all characters in a column are shown
pd.set_option('display.max_colwidth', None)

vehicles_df.tail()"""



#creates the table
df = pd.DataFrame({'Name' : description_list[2:], 'Price' : prices_list}) 
df.to_csv('listings.csv', index=False, encoding='utf-8')
df.to_excel("excel_listings.xlsx", index = False)  




