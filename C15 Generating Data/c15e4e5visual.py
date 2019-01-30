import matplotlib.pyplot as plt

from c15e4e5modified_random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk, and plot the points.
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	# Set the size of the plotting window.
	plt.figure(figsize=(10, 6))
	
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Purples,
	edgecolor='none', s=2)
	
	# Emphasize the first and last points.
	plt.scatter(0, 0, c='green', edgecolors='none', s=40)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
	s=40)

	# Remove the axes.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.savefig('c15e4last_variation.png', bbox_inches='tight')
	plt.show()
	
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break

