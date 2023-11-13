import requests
from bs4 import BeautifulSoup
import csv

url = "https://sublet.com/new-york-city?relation=2"

# Send an HTTP request to the URL
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

# Find all listings
listings = soup.findAll('div', class_="col-12 font")

bathsnrooms = soup.findAll('div', class_="col-12")

# Open a CSV file to write the data
with open('sublet_listings.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['Details', 'Type of Space', 'Price'])

    for listing in listings[1:]:
        # Extract the text and split it into components
        parts = listing.text.split('\n')

        # Clean the parts to remove extra whitespace
        cleaned_parts = [part.strip() for part in parts if part.strip()]


        # Format the output and write to CSV
        if len(cleaned_parts) >= 2:
            price = cleaned_parts[0]
            type_of_space = cleaned_parts[1]
            writer.writerow([type_of_space, price])

print("Data written to sublet_listings.csv")
