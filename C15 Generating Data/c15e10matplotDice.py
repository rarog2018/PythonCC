#!python3
import matplotlib.pyplot as plt
import die

MAX_R = 50000

# create a 6 side die
die1 = die.Die()

# values for x axis - number on each side of the die
x_values = [n for n in range(1, die1.num_sides+1)]
# results of rolling the die MAX_R times
results = [die1.roll() for n in range(MAX_R)]
# values for y axis, number of occurrences of each value on the die
y_values = [results.count(value) for value in x_values]

# setup the chart
plt.title("Results of rolling D6 die %s times." % MAX_R, fontsize=20)
plt.xlabel("Result", fontsize=15)
plt.ylabel("Frequency of result", fontsize=15)
plt.tick_params(axis="both", labelsize=14)
# plt.axis([0, die1.num_sides, 0, max(y_values) + 1000])

plt.scatter(x_values, y_values, c="violet", edgecolors="red", s=300)
plt.savefig("die_plot1.png", bbox_inches="tight")
