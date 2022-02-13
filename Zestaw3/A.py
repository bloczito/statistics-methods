from random import random

from numpy import log, power, exp, array, arange
from scipy.special import factorial
from matplotlib import pyplot as plt

Ts = [1, 10, 20, 90]

lamb = 1
N = 20000



def exponential(lamb) -> float:
    return -log(random()) /lamb


for T_idx, T in enumerate(Ts):
    values = []
    for i in range(N):
        t = 0
        sig = 0
        while t < T:
            t += exponential(lamb)
            if t < T:
                sig += 1

        values.append(sig)

    plt.subplot(2, 2, T_idx + 1)
    plt.hist(values, density=True, stacked=True)

    x_axis = arange(0.0, max(values) + 1, 1.0)
    y_axis = power(lamb*T, x_axis) * exp(-lamb*T)/factorial(x_axis,exact=True)
    plt.plot(x_axis, y_axis)
    plt.title(f"T = {T}")

    print(f"T = {T},  Mean = {sum(values) / len(values)},  lambda * t = {lamb * T}")
    # print(values)
plt.show()
