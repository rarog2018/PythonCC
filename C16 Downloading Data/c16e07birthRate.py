#!python3
# plots the birth rate of each country on the world map

import csv
from c16e05allCountries import get_country_code
from pygal.maps.world import World


def main():
    # collect the data from a given file and store it in a dictionary
    birthRate = collect_birth_rate_data("birth_rate.csv")

    # Create a map and fill it with data
    wm = World()
    wm.title = "Countries birth rate, 2018"
    wm.add("birth rates", birthRate)

    wm.render_to_file('world_birth_rate.svg')


def collect_birth_rate_data(filename):
    brDict = {}
    # Load the data from the csv file
    with open(filename) as brF:
        reader = csv.reader(brF)
        # skip first 4 rows, because they do not contain important data
        for i in range(4):
            next(reader)

        # store header information
        headerRow = next(reader)
        '''for index, columnHeader in enumerate(headerRow):
            print(index, columnHeader)'''

        # now we know that "Country Name" is at index 0, Country Code at 1, data
        # from year 2018 is at the index 62, year 1960 at index 4

        # build a dictionary
        for row in reader:
            # get the country name
            countryName = row[0]
            # get the birth rate value for 2018 year
            try:
                brValue = float(row[62])
            except:
                continue

            # get the country code
            code = get_country_code(countryName)
            # if code is not None, add the data to the dictionary
            if code:
                brDict[code] = brValue

    return brDict


main()
