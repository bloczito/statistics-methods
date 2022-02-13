from random import choices
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np

X = 100
N = 10000

p_log_in = 0.2
# p_log_out = 0.5

x_t = [0 for _ in range(X)]
logged_users = [False for _ in range(X)]
prev = [False for _ in range(X)]
convergence = [[] for _ in range(5)]


def decide(is_logged, x):
    p_log_out = 1 - (0.008 * x + 0.1)
    if is_logged:
        return choices([True, False], weights=[1 - p_log_out, p_log_out])[0]
    else:
        return choices([True, False], weights=[p_log_in, 1 - p_log_in])[0]


for i in range(N):
    logged_counter = 0
    for x in range(X):
        logged = decide(logged_users[x], sum(logged_users))
        logged_users[x] = logged

        if logged: logged_counter += 1

        if 25 <= x < 30:
            convergence[x - 25].append(x_t[x] / (i + 1))

    prev = deepcopy(logged_users)

    x_t[logged_counter] += 1
print(x_t)
# x_axis = np.linspace(0, N, N)

# fig, axs = plt.subplots(5, 1)
# for i in range(len(convergence)):
#     axs[i].plot(x_axis, convergence[i])
# fig.show()

x_axis = np.linspace(0, X, X)
plt.plot(x_axis, x_t)
plt.show()