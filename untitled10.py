# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:57:48 2023

@author: KINGSLEY NNAEMEKA EZEJA
"""


import pandas as pd
import matplotlib.pyplot as plt
df_gdp = pd.read_csv('GDP_per_capita_table (4).csv')
print(df_gdp)

# establish list of years
gdp_year = ['2017', '2018', '2019', '2020', '2021']

# Data for each country
belgium = [44198, 47549, 46599, 45189, 51768]
france = [38781, 41593, 40579, 39037, 43519]
germany = [44653, 47974, 46795, 46253, 50802]
italy = [32407, 34622, 33673, 31835, 35551]
poland = [13865, 15468, 15732, 15742, 17841]
spain = [28170, 30365, 29554, 27056, 30116]


#  graph with multiple lines
plt.figure()

# Add lines for each country
plt.plot(gdp_year, belgium, label='Belgium', color='r')
plt.plot(gdp_year, france, label='France')
plt.plot(gdp_year, germany, label='Germany')
plt.plot(gdp_year, italy, label='Italy')
plt.plot(gdp_year, poland, label='Poland')
plt.plot(gdp_year, spain, label='Spain')

# Set labels and title
plt.xlabel('Year')
plt.ylabel('GDP per capita (USD)')
plt.xlim()
plt.title('GDP per capita[2017 to 2021]')

# Add legend
plt.legend(loc='upper right')
plt.show()

#  visualisation methods.
# Box plot

data = {
    'Belgium': [44198, 47549, 46599, 45189, 51768],
    'France': [38781, 41593, 40579, 39037, 43519],
    'Germany': [44653, 47974, 46795, 46253, 50802],
    'Italy': [32407, 34622, 33673, 31835, 35551],
    'Poland': [13865, 15468, 15732, 15742, 17841],
    'Spain': [28170, 30365, 29554, 27056, 30116]
}

fig, gdp = plt.subplots()

gdp.boxplot(data.values())
gdp.set_xticklabels(data.keys())

plt.show()

# PIE
# Choose the two years and the countries whose GDP you want to compare
Year1 = 2017
Year2 = 2021
Country1 = "Belgium"
Country2 = "France"

# establish a dictionary with the GDP data for the selected years and countries
data = {Country1: [44198, 47549, 46599, 45189, 51768],
        Country2: [38781, 41593, 40579, 39037, 43519]}
GDP1 = data[Country1][Year2-Year1]
GDP2 = data[Country2][Year2-Year1]

# establish the pie-chart
labels = [Country1, Country2]
Values = [GDP1, GDP2]
colors = ["#FFC107", "#9C27B0"]
explode = (0.1, 0)
plt.pie(Values, labels=labels, colors=colors,
        explode=explode, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title("GDP comparison between " + str(Year1) + " and " + str(Year2))
plt.show()
