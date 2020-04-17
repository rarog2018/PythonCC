#!python3
# c16e03rainfall - program that plots rainfall data of a location

# TODO: function that collects the rain data from a file

import csv
import matplotlib.pyplot as plt
from datetime import datetime


def main():
    # empty containers for data
    dates, rainFalls = [], []

    # collect the data from a given file
    filename = "sitka_weather_2014.csv"
    collect_rain_data(filename, dates, rainFalls)

    # Plot data.
    fig = plt.figure()
    plt.plot(dates, rainFalls, c="blue", linewidth=1)
    plt.title('Daily rainfalls in Sitka, 2014', fontsize=21)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Rainfall (In)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def collect_rain_data(filename, dates, rainFalls):
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
                todaysRainFall = float(row[19])

            # if not print error message
            except ValueError:
                print(currentDate, 'missing data')

            # if correct, append the data
            else:
                dates.append(currentDate)
                rainFalls.append(todaysRainFall)


main()
