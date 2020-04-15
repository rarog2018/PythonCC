#!python3
import matplotlib.pyplot as plt
import die

MAX_R = 50000

# create two 6 side dice
die1 = die.Die()
die2 = die.Die()

# values for x axis - all possible results
x_values = sorted(list(set(
    [n + m for n in range(1, die1.num_sides+1) for m in range(1, die2.num_sides+1)])))
# results of rolling the dices MAX_R times
results = [die1.roll() + die2.roll() for n in range(MAX_R)]
# values for y axis, number of occurrences of each possible value
y_values = [results.count(value) for value in x_values]

# setup the chart
plt.title("Results of rolling two D6 dice %s times." % MAX_R, fontsize=20)
plt.xlabel("Result", fontsize=15)
plt.ylabel("Frequency of result", fontsize=15)
plt.tick_params(axis="both", labelsize=14)

plt.scatter(x_values, y_values, c="red", edgecolors="black", s=300)
plt.savefig("dice_plot3.png", bbox_inches="tight")
