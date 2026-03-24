from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

from homework9_data import mystery1


data = defaultdict(lambda: [])
for x, y in mystery1:
    data["x"].append(x)
    data["y"].append(y)

x = np.array(data["x"])
x1 = x[:, 0]  # feature x1
x2 = x[:, 1]  # feature x2
# implement a new feature x3 to make data linearly separable
# x3 = ...

axes = plt.axes(projection='3d')
colors = {True: 'green', False: 'red'}
axes.scatter3D(x1, x2, c=[colors[y] for y in data["y"]])
# axes.scatter3D(x1, x2, x3, c=[colors[y] for y in data["y"]])
plt.show()
