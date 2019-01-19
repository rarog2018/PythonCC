#Plots cubic numbers 
import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, edgecolor='none', s=20)

plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 5100, 0, 5100**3])

plt.show()
