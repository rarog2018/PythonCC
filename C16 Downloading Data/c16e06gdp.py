#!python3
# c16e05gdp - plots the GDP of each country on the world map

import json
from pygal.maps.world import World
from c16e05allCountries import get_country_code
from pygal.style import CleanStyle

# Load the data into a list
filename = 'gdp_json.json'
with open(filename) as f:
    gdpData = json.load(f)  # list of dictionaries

# Build a dictionary of gdp data (with country codes, so they can be plotted on a map)
ccGdp = {}
for gdpDict in gdpData:
    # pick only data from the most recent available year
    if gdpDict['Year'] == 2016:
        # get the country name from the dictionary
        countryName = gdpDict['Country Name']
        # store the value of the gdp, no need to know decimals
        gdpValue = int(float(gdpDict['Value']))
        # use the function from previous exercise to get the country code
        code = get_country_code(countryName)
        # if code is not None, add the data to the dictionary
        # print(countryName + ": " + '{:,}'.format(gdpValue))
        if code:
            ccGdp[code] = gdpValue

# to distinguish the countries from each other, we will have to put them in
# separate dictionaries to plot them separately
ccGdp1, ccGdp2, ccGdp3 = {}, {}, {}

# showing results in milliards is IMO better to see the real difference
# between the countries
for code, val in ccGdp.items():
    if val < 500000000000:
        ccGdp1[code] = round(val / 1000000000)
    elif val < 5000000000000:
        ccGdp2[code] = round(val / 1000000000)
    else:
        ccGdp3[code] = round(val / 1000000000)


'''print("over 5,000 mld countries: " + str(len(ccGdp3)))
print("500 - 5,000 mld countries: " + str(len(ccGdp2)))
print("below 500 mld countries: " + str(len(ccGdp1)))'''

# Create a map and fill it with data
wm = World(style=CleanStyle)
wm.title = "Countries GDP, 2016"
wm.add('over 5,000 mld', ccGdp3)
wm.add("500 - 5,000 mld", ccGdp2)
wm.add("below 500 mld", ccGdp1)

wm.render_to_file('world_gdp.svg')
