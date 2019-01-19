#Plots cubic numbers
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4 ,5]
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c='purple', edgecolor='none', s=50)

# Set chart title and label axes
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
