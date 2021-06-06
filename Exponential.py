import math
from matplotlib import pyplot as plt

x = [0]
y = [0**exponent]

maxNumber = 10
pointsPerUnit = 100
exponent = 3

for i in range(maxNumber * pointsPerUnit):
    x.append(x[i] + (1 / pointsPerUnit))
    y.append(x[i + 1]**exponent)

plt.plot(x, y)
plt.grid(color='#1d1d1b', linestyle='-', linewidth=0.5)
plt.show()
