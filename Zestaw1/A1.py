from random import random
from math import sqrt, log, pi, exp
import matplotlib.pyplot as plt

from helpers import calculate_variance, calculate_mean

def generateRandom(mean, stdDev):
    x = y = s = 0

    while s == 0 or s >= 1:
        x = random() * 2 - 1
        y = random() * 2 - 1
        s = x ** 2 + y ** 2

    s = sqrt(-2 * log(s) / s)

    return mean + stdDev * x * s


N = 1000

x_axis = []
y_axis = []
for i in range(N):
    x_axis.append(generateRandom(0, 1))

x_axis.sort()

for x in x_axis:
    y_axis.append((1/sqrt(2 * pi)) * exp(-(x*x)/2))

plt.hist(x_axis, bins=20, density=True, color="lightgreen")
plt.plot(x_axis, y_axis)
plt.show()

avg_value = calculate_mean(x_axis)
variance = calculate_variance(x_axis, avg_value)

print("Wartość średnia:", avg_value)
print("Wariancja: ", variance)
