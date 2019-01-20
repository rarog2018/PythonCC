import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Use RandomWalk class to generate this plot
mol = RandomWalk()
mol.fill_walk()
	
# Set the size of the plotting window.
plt.figure(figsize=(12, 6))
	
point_numbers = list(range(mol.num_points))
plt.plot(mol.x_values, mol.y_values, c='purple', linewidth=1.2)
	
# Emphasize the first and last points.
plt.scatter(0, 0, c='green', edgecolors='none', s=60)
plt.scatter(mol.x_values[-1], mol.y_values[-1], c='red', edgecolors='none', s=60)

# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
	
plt.show()
