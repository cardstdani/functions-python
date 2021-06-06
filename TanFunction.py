import math
from matplotlib import pyplot as plt

xTan = [0]
yTan = [math.tan(0)]

maxNumber = 7
pointsPerUnit = 100

for i in range(maxNumber * pointsPerUnit):
    xTan.append(xTan[i] + (1 / pointsPerUnit))
    yTan.append(math.tan(xTan[i + 1]))

plt.plot(xTan, yTan)
plt.legend(["Tan"])
plt.grid(color='#1d1d1b', linestyle='-', linewidth=0.5)
plt.show()
