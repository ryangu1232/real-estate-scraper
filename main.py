import requests
import string
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row[0])  # Assuming each row contains a single word
    return data

# Specify the CSV file to read
csv_filename = 'words.csv'

# Read the data from the CSV file and store it in a variable
words = read_csv_file(csv_filename)

# Convert the list of words into a string without quotes and brackets
words_string = ', '.join(words)

# Print the resulting string
print(words_string)
location = input("Please enter your location")
search_term = input("Input the search term")

facebook_url = f"https://www.facebook.com/marketplace/{location}/search/?query={search_term}"
response = requests.get(facebook_url)

soup = BeautifulSoup(response.text, "html.parser")

tagsname = soup.findAll(class_="title__condition__container")
tagscost = soup.findAll(class_="p--t--1 fw--bold")
listing_sizes = soup.findAll(class_="tile__details__pipe__size")
likes = soup.findAll(class_="social-action-bar__like")
tagsimage = soup.findAll(class_="img__container img__container--square")

yeezy_gaplistingimg = []
for tag in tagsimage[1:]:
    img_tag = tag.find('img')
    if img_tag:
        img_url = img_tag.get('src')
        yeezy_gaplistingimg.append(img_url)
        print(img_url)
    else:
        yeezy_gaplistingimg.append('')
        print('No image available')

yeezy_gaplisting = []
for i in range(1, len(tagsname)):
    title = " ".join(str(tagsname[i].text).split())
    yeezy_gaplisting.append([title])

yeezy_gaplistingsize = []
for i in range(1, len(tagsname)):
    if len(listing_sizes) > i:
        size = " ".join(str(listing_sizes[i].text).split())
    else:
        size = ''
    yeezy_gaplistingsize.append([size])

yeezy_gaplistingcost = []
for i in range(1, len(tagsname)):
    price_text = " ".join(str(tagscost[i].text).split())
    price = float(''.join(filter(str.isdigit, price_text))) 
    yeezy_gaplistingcost.append([price])

yeezy_gaplistinglikes = []
for i in range(1, len(tagsname)):
    likes2 = " ".join(str(likes[i].text).split())
    yeezy_gaplistinglikes.append([likes2])


df = pd.DataFrame(np.column_stack([yeezy_gaplisting, yeezy_gaplistingcost, yeezy_gaplistingsize, yeezy_gaplistinglikes, yeezy_gaplistingimg]), columns=['Item', 'Cost', 'size', 'Likes', 'ImgLink'])
df.to_csv(words_string + '-poshmark.xls')


print(df.describe())
counts = df['Item'].value_counts()

# Drop rows with missing values in the 'Cost' column
df = df.dropna(subset=['Cost'])

# Convert 'Cost' column to numeric
df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')

# Convert 'Likes' column to numeric
df['Likes'] = pd.to_numeric(df['Likes'], errors='coerce')

# Create boxplot
fig, ax = plt.subplots()
plt.boxplot([df[df['Likes'] > 5]['Cost'].values,
             df[df['Likes'] <= 5]['Cost'].values],
            labels=['More than 5 Likes', 'Less than or equal to 5 Likes'])

plt.title('Cost Distribution by Number of Likes')
plt.xlabel('Likes')
plt.ylabel('Cost')

fig.savefig('likes_cost_boxplot.png')


corr_coef = df['Cost'].corr(df['Likes'], method='spearman')
print(f"Correlation coefficient between 'Cost' and 'Likes': {corr_coef:.2f}")
#correlaiton coefficient
