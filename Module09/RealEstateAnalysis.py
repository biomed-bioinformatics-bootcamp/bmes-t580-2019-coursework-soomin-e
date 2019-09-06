# Library Imports
import pandas as pd



# Main File
#Header
print('----------------------')
print(' Real Estate App')
print('----------------------')
print()

print('loading CSV file..............finished')
print()

house_df = pd.read_csv('houseData.csv')
headersName = []

print('Headers: ', end='')
for col in house_df.columns:
    print(col+', ', end='')
print()
print()

expensive = house_df.loc[house_df['price'].idxmax(), :]
cheap = house_df.loc[house_df['price'].idxmin(), :]

print('Most expensive house: %s beds, %s baths, house for $%s in %s' % (expensive.beds, expensive.baths, expensive.price, expensive.city))
print()
print('Least expensive house: %s beds, %s baths, house for $%s in %s' % (cheap.beds, cheap.baths, cheap.price, cheap.city))
print()

price = house_df.loc[:, 'price']
beds = house_df.loc[:, 'beds']
baths = house_df.loc[:, 'baths']

avgPrice = sum(price)/len(price)
avgBeds = sum(beds)/len(price)
avgBaths = sum(baths)/len(baths)

print('Average House: $%i, %.1f beds, %.1f baths' % (avgPrice, avgBeds, avgBaths))
print()

#2 Beds
beds2_df = house_df.loc[house_df['beds'] == 2]

price2 = beds2_df.loc[:, 'price']
beds2 = beds2_df.loc[:, 'beds']
baths2 = beds2_df.loc[:, 'baths']

avgPrice = sum(price2)/len(price2)
avgBeds = sum(beds2)/len(price2)
avgBaths = sum(baths2)/len(baths2)

print('Average 2-Bedroom House: $%i, %.1f beds, %.1f baths' % (avgPrice, avgBeds, avgBaths))