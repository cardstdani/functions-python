import math
from matplotlib import pyplot as plt

xCos = [0]
yCos = [math.cos(0)]

maxNumber = 20
pointsPerUnit = 100

for i in range(maxNumber * pointsPerUnit):
    xCos.append(xCos[i] + (1 / pointsPerUnit))
    yCos.append(math.cos(xCos[i + 1]))

plt.plot(xCos, yCos)
plt.legend(["Cos"])
plt.grid(color='#1d1d1b', linestyle='-', linewidth=0.5)
plt.show()
