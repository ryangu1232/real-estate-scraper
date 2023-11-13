import requests
from bs4 import BeautifulSoup
import csv

url = "https://sublet.com/new-york-city?relation=2"

# Send an HTTP request to the URL
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

# Find all listings
listings = soup.findAll('div', class_="details-section font14")

# Open a CSV file to write the data
with open('subletbath&rooms_listings.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['Bedrooms', 'Bathrooms', 'Type of Space', 'Price'])

    for listing in listings:
        # Find the bed and bath information
        bed_bath_info = listing.find('div', class_='col-12')

        if bed_bath_info:
            beds_info = bed_bath_info.find('span')
            # if beds_info: 
            #     print("1")
            # else: 
            #     print("2")
            #     beds_info = bed_bath_info.find('i', class_='fas fa-bed')
            baths_info = bed_bath_info.find('span', title=lambda x: x and 'bath' in x)
            beds = beds_info.get_text(strip=True) #if beds_info else 'N/A'
            baths = baths_info.get_text(strip=True) #if baths_info else 'N/A'


        # Write the data to the CSV file
        writer.writerow([beds, baths])


#print("Data written to sublet_listings.csv")
