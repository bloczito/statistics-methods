from random import choices
import numpy as np
from copy import deepcopy



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

for _ in range(1000):
    P_old = P
    P = np.matmul(P_old, P_S)
    p_t.append(P)

    if np.abs(P[0][0] - P_old[0][0]) < e: break



N = 10**4

for i in range(3):
    x_t = [0, 0, 0]
    x = i
    for j in range(N):
        x = choices([0, 1, 2], weights=[P_S[x][0], P_S[x][1], P_S[x][2]])[0]
        x_t[x] += 1
    print(f"x = {x})")
    print(f"M   = {np.divide(x_t, N)}")
    print(f"P_N = {P[x]}")