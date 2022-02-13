from math import tan, pi
from random import random
import matplotlib.pyplot as plt

from helpers import calculate_variance, calculate_mean


def get_random_number(y0, c):
    x = random()
    return c * tan(pi * (x - 1 / 2)) + y0


def calculate_value(x, y0, c):
    denominator = pi * c * (1 + ((x - y0) / c) ** 2)
    return 1 / denominator


N = 1000
y0 = 1
c = 1
x_range = 7

x_axis = []
y_axis = []

for i in range(N):
    x = get_random_number(y0, c)
    x_axis.append(x)

x_axis.sort()
for x in x_axis:
    y_axis.append(calculate_value(x, y0, c))

plt.hist(x_axis, bins=20, density=True, color="lightgreen", range=(-x_range + y0, x_range + y0))
plt.plot(x_axis, y_axis)
plt.xlim([-x_range + y0, x_range + y0])
plt.show()

avg_value = calculate_mean(x_axis)
variance = calculate_variance(x_axis, avg_value)

print("Wartość średnia:", avg_value)
print("Wariancja: ", variance)