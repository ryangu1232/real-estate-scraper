#this code takes in the xls files and puts it together and organizes it so that they are in order
import pandas as pd
import numpy as np

data1 = pd.read_csv('')
data2 = pd.read_csv('')


output4 = pd.merge(data1, data2, how='outer')


output4.to_csv('merge.csv')


df = pd.read_csv('merge.csv')

df = df.sort_values(by='Cost', ascending=False)

df.to_csv('mergecost.csv')

"""
print(df)
print(df.describe())
cf = pd.read_csv('nike-ebay.xls')
print(cf.describe())

df_mean_cost = df['Cost'].mean()
cf_mean_cost = cf['Cost'].mean()

# Print the results
if df_mean_cost > cf_mean_cost:
    print("On average, items in df cost more than items in cf")
else:
    print("On average, items in cf cost more than items in df")

price_limit = float(input("Enter a price limit: "))

filtered_df = df[df['Cost'] < price_limit]

filtered_df.to_csv('filtered_data.csv', index=False)

print(filtered_df)
"""