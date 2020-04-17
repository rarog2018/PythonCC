#!python3
# c16e02comparisons: program plots two data sets on the same chart for comparison

# TODO: function that will process the data for each file
# TODO: function that will fill the chart
# TODO: Chart that will show the processed data

import csv
from matplotlib import pyplot as plt
from datetime import datetime


def main():
    # empty containers for data
    datesDV, highsDV, lowsDV = [], [], []
    datesS, highsS, lowsS = [], [], []

    # process the first file
    filename = 'death_valley_2014.csv'
    processCSVFile(filename, datesDV, highsDV, lowsDV)

    # process the second file
    filename = 'sitka_weather_2014.csv'
    processCSVFile(filename, datesS, highsS, lowsS)

    # Plot data.
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # data from the first file
    fillChart(datesDV, highsDV, lowsDV, 0.2)

    # data from the second file
    fillChart(datesS, highsS, lowsS, 0.6)

    # Format plot.
    title = "Daily high and low temperatures - 2014\nDeath Valley and Sitka"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def processCSVFile(filename, dates, highs, lows):
    # open the file
    with open(filename) as f:
        # read the contents of the file
        reader = csv.reader(f)
        headerRow = next(reader)   # store the headers

        # continue processing the file
        for row in reader:
            # assign values to the variables, with checking if they are correct
            try:
                # Get the dates, high and low temperatures from the file.
                currentDate = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])

            # if not print error message
            except ValueError:
                print(currentDate, 'missing data')

            # if correct, append the data
            else:
                dates.append(currentDate)
                highs.append(high)
                lows.append(low)


def fillChart(dates, highs, lows, al):
    plt.plot(dates, highs, c='red', alpha=al)
    plt.plot(dates, lows, c='blue', alpha=al)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


main()
