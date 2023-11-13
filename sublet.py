import requests
from bs4 import BeautifulSoup

url = "https://sublet.com/new-york-city?relation=2"

# Send an HTTP request to the URL
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

# Find all listings
listings = soup.findAll('div', class_="col-12 font") 

for listing in listings[1:]:
    # Extract the text and split it into components
    parts = listing.text.split('\n')

    # Clean the parts to remove extra whitespace
    cleaned_parts = [part.strip() for part in parts if part.strip()]

    # Format the output (assuming the first element is the price and the second is the type)
    if len(cleaned_parts) >= 2:
        price = cleaned_parts[0]
        type_of_space = cleaned_parts[1]
        print(f"{type_of_space}, {price}")
