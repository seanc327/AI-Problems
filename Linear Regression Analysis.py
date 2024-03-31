import matplotlib.pyplot as plt, numpy as np

x_axis = np.array([72, 50, 81, 74, 94, 86, 59, 83, 65, 33, 88, 81])
y_axis = np.array([84, 63, 77, 78, 90, 75, 49, 79, 77, 52, 74, 90])

m, b = np.polyfit(x_axis, y_axis, 1)

plt.scatter(x_axis, y_axis)
plt.xlabel("y axis")
plt.ylabel("x axis")
plt.plot(x_axis, m * x_axis + b)
plt.show()

print("y =", m, "* x +", b)
