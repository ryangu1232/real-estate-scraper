#this is the main folder
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# URL of the page to scrape
url = 'https://www.facebook.com/marketplace/sanfrancisco/search/?query=subleases'

# Send a request to the URL
response = requests.get(url)

# Create a list to hold all scraped data
data = []

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all listings - adjust the selector based on the actual HTML structure
    listings = soup.find_all('div', class_='listing-class') # Adjust this accordingly

    for listing in listings:
        # Extract information from each listing
        # Adjust these based on the actual structure and data of the listings
        title = listing.find('h2').text.strip() if listing.find('h2') else 'No Title'
        price = listing.find('span', class_='price-class').text.strip() if listing.find('span', class_='price-class') else 'No Price'
        description = listing.find('p', class_='description-class').text.strip() if listing.find('p', class_='description-class') else 'No Description'

        # Append the data to the list
        data.append({'Title': title, 'Price': price, 'Description': description})

else:
    print('Failed to retrieve the webpage')

# Create a DataFrame from the scraped data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_filename = 'scraped_data.xlsx'
df.to_excel(excel_filename, index=False)

print(f'Data saved to {excel_filename}')
