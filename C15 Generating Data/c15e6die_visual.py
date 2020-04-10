import pygal
from die import Die

MAX_R = 1000

# Create two D6 dices
die = Die()

# Make some rolls, and store results in a list.
# assign the result of die.roll() to 'x', repeat 1000 times
results = [die.roll() for x in range(MAX_R)]

# Analyze the results.
# assign the result of count() to value for every side of the dice
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 %s times." % MAX_R
# change n to string and assign it to n for every side of the dice
hist.x_labels = [str(n) for n in range(1, die.num_sides+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('./die_visual7.svg')
