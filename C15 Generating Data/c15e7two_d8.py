import pygal
from die import Die

MAX_R = 100000
SNUM = 8

# Create two D8 dices
die1 = Die(SNUM)
die2 = Die(SNUM)

# Make some rolls, and store results in a list.
# list comprehension added
results = [die1.roll() + die2.roll() for r in range(MAX_R)]

# Analyze the results.
max_result = die1.num_sides + die2.num_sides
# list comprehension added
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D%s dice %s times." % (SNUM, MAX_R)
# list comprehension added
hist.x_labels = [str(n) for n in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add(('D%s + D%s' % (SNUM, SNUM)), frequencies)
hist.render_to_file('./dice_visual11.svg')
