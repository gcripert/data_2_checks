import requests

import pandas as pd

pd.set_option('display.max_columns', None)

pd.set_option('display.width', None)

pd.set_option('display.max_colwidth', None)


# pulling in data from API

r = requests.get('https://fruityvice.com/api/fruit/all')
x = r.json()
df = pd.DataFrame(x)
print (df)


# descriptive statistic one: average sugar content

average_sugar = df['nutritions'].apply(lambda s: s['sugar']).mean()

print (average_sugar)


# descriptive statistic two: unique family types

num_unique_family = df['family'].unique().size

print (num_unique_family)


# using mask to select fruits under fifty calories

mask = df['nutritions'].apply(lambda c: c['calories']<50)

fruits_under_50_cals = df[mask]

print (fruits_under_50_cals)


# selecting and printing second and third columns

second_and_third_columns = df.iloc[:, [1,2]]

print (second_and_third_columns)


# selecting and printing first four rows

first_four_rows = df.iloc[0:4, :]

print (first_four_rows)

