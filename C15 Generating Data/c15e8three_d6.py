import pygal
from die import Die

MAX_R = 50000
# SNUM = 8

# Create three D6 dices
die1 = Die()
die2 = Die()
die3 = Die()

# Make some rolls, and store results in a list.
# list comprehension added
results = [die1.roll() + die2.roll() + die3.roll() for r in range(MAX_R)]

# Analyze the results.
max_result = die1.num_sides + die2.num_sides + die3.num_sides
# list comprehension added
frequencies = [results.count(value) for value in range(3, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice %s times." % MAX_R
# list comprehension added
hist.x_labels = [str(n) for n in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('./dices_visual12.svg')
