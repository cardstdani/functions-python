import math
from matplotlib import pyplot as plt

xSin = [0]
ySin = [math.sin(0)]

maxNumber = 20
pointsPerUnit = 100

for i in range(maxNumber * pointsPerUnit):
    xSin.append(xSin[i] + (1 / pointsPerUnit))
    ySin.append(math.sin(xSin[i + 1]))

plt.plot(xSin, ySin)
plt.legend(["Sin"])
plt.grid(color='#1d1d1b', linestyle='-', linewidth=0.5)
plt.show()
