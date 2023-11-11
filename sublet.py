import requests
from bs4 import BeautifulSoup

url = "https://sublet.com/new-york-city?relation=2"

# Send an HTTP request to the URL
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())

boxes = soup.findAll('div', class_="col-12 font") 
for box in boxes[1:]:
    print(box.text)


prices = soup.findAll('div', class_="col-12 font")
for price in prices[1:]:
    price = price.find_all(string=True,recursive=False)
    print(price)


# types = soup.findAll('a', class_="float-right supply-details-link text-black")
# for type in types[1:]:
#     type = type.get_text()
    # print(type)

# price = soup.find('span', class_="js-currency float-left text-black")
# print(price.text)

