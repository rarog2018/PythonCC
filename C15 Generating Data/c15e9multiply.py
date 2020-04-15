import pygal
from die import Die

MAX_R = 50000
# SNUM = 8

# Create three D6 dices
die1 = Die()
die2 = Die()

# Make some rolls, and store results in a list.
results = [die1.roll() * die2.roll() for r in range(MAX_R)]

# Analyze the results.
max_result = die1.num_sides * die2.num_sides

# list of possible results
# this looks overly complicated, I'm doing it only as an exercise which was suggested
# in exercise 15-6
possibleResults = sorted(list(set([x * y for x in range(1, die1.num_sides+1)
                                   for y in range(1, die2.num_sides+1)])))

# count how many times each result appeared
frequencies = [results.count(value) for value in possibleResults]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice %s times." % MAX_R
# create label from values in possibleResults
hist.x_labels = [str(n) for n in possibleResults]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('./dices_visual15.svg')
