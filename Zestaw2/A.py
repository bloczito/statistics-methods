import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

N = 1000

P_S = np.array([
    [0.64, 0.32, 0.04],
    [0.4,  0.5,  0.1],
    [0.25, 0.5,  0.25]]
)

p_t = []
p_t.append(P_S)

P = deepcopy(P_S)
P_old = deepcopy(P_S)



e = 1e-5

for _ in range(N):
    P_old = P
    P = np.matmul(P_old, P_S)
    p_t.append(P)

    if np.abs(P[0][0] - P_old[0][0]) < e: break


x_axis = np.linspace(0, len(p_t), len(p_t))
y_axis = [x[0][0] for x in p_t]


for i in range(3):
    for j in range(3):
        plt.plot(x_axis, [x[i][j] for x in p_t])

plt.legend(['[0][0]', '[0][1]', '[0][2]', '[1][0]', '[1][1]', '[1][2]', '[2][0]', '[2][1]', '[2][2]'])
# plt.plot(x_axis, y_axis)
# plt.plot(x_axis, [p_t[-1][0][0] for _ in p_t])
plt.show()