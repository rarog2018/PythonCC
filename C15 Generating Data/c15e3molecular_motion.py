import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
	# Make a random walk, and plot the points.
	rw = RandomWalk()
	rw.fill_walk()
	
	# Set the size of the plotting window.
	plt.figure(figsize=(12, 6))
	
	point_numbers = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values, c='purple', linewidth=1.2)
	
	# Emphasize the first and last points.
	plt.scatter(0, 0, c='green', edgecolors='none', s=60)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
	s=60)

	# Remove the axes.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	break
