from __future__ import print_function

from matplotlib import pyplot as plt

import pandas as pd
print(pd.__version__)

pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({'City name': city_names, 'Population': population})

california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())

print(california_housing_dataframe.head())

california_housing_dataframe.hist('housing_median_age')
plt.figure()
california_housing_dataframe.plot()

cities = pd.DataFrame({'City name': city_names, 'Population': population})
print(type(cities['City name']))
print(cities['City name'])

print(type(cities['City name'][1]))
print(cities['City name'][1])

print(type(cities[0:2]))
print(cities[0:2])

print(population / 1000)

import numpy as np
print(np.log(population))

print(population.apply(lambda val: val > 1000000))

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities)

cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print(cities)

print(city_names.index)
print(cities.index)

print(cities.reindex([2, 0, 1]))

print('----Random permutation start----')
print(cities.reindex(np.random.permutation(cities.index)))
print(cities.reindex(np.random.permutation(cities.index)))
print(cities.reindex(np.random.permutation(cities.index)))
print('----Random permutation stop-----')

print(cities.reindex([0, 4, 1, 5, 2]))
