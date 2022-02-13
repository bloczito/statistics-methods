from random import random, choices

import matplotlib.pyplot as plt
from numpy import log, arange, power, exp, mean
from typing import List
from scipy.special import factorial

lamb = 1
N = 10000
# Ts = [1]
Ts = [1, 10, 20, 90]


def my_exp() -> float:
    return -log(random())


def get_y_axis(x_axis: List[float], a: float) -> List[float]:
    return power(T * a, x_axis) * exp(-T * a) / factorial(x_axis, exact=True)


for T_idx, T in enumerate(Ts):
    group1: List[float] = []
    group2: List[float] = []
    group3: List[float] = []

    for i in range(N):
        time = 0.0
        sig1 = sig2 = sig3 = 0.0

        while time < T:
            time += my_exp()
            group = choices([1, 2, 3], weights=[0.2, 0.5, 0.3])[0]

            if time <= T * 0.2:
                sig1 += 1
            elif T * 0.2 <= time <= T * 0.7:
                sig2 += 1
            elif T * 0.7 <= time <= T:
                sig3 += 1

        group1.append(sig1)
        group2.append(sig2)
        group3.append(sig3)

    plt.subplot(3, 1, 1)
    plt.title(f"T = {T}, gr = 1")
    x_axis = arange(0, max(group1) + 1, 1.0)
    y_axis = get_y_axis(x_axis, 0.2)
    plt.hist(group1, density=True, stacked=True)
    plt.plot(x_axis, y_axis)

    plt.subplot(3, 1, 2)
    plt.title(f"T = {T}, gr = 2")
    x_axis = arange(0, max(group2) + 1, 1.0)
    y_axis = get_y_axis(x_axis, 0.5)
    plt.hist(group2, density=True, stacked=True)
    plt.plot(x_axis, y_axis)

    plt.subplot(3, 1, 3)
    plt.title(f"T = {T}, gr = 3")
    x_axis = arange(0, max(group3) + 1, 1.0)
    y_axis = get_y_axis(x_axis, 0.3)
    plt.hist(group3, density=True, stacked=True)
    plt.plot(x_axis, y_axis)

    plt.show()

    print(f"T = {T}, gr = 1   |   {mean(group1)} == {T * 0.2}")
    print(f"T = {T}, gr = 2   |   {mean(group2)} == {T * 0.5}")
    print(f"T = {T}, gr = 3   |   {mean(group3)} == {T * 0.3}")
    print()

