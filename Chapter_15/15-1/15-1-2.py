import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.title("Cube Values")
plt.xlabel("Value")
plt.ylabel("Cube of Value")

plt.scatter(x_values, y_values, s=5)
plt.show()
