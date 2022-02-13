from numpy import log
from random import random
from matplotlib import pyplot as plt

N = 100
lambd_a = 10
lambd_d = 10
lambd_d_2 = 6


def get_time(lambd):
    return - (log(random()) / lambd)


a = [get_time(lambd_a) for _ in range(N)]
d = [get_time(lambd_d) for _ in range(N)]
d2 = [1 / lambd_d_2 for _ in range(N)]
A = [sum(a[0: i + 1]) for i in range(len(a))]
D = [0.0] * N
D2 = [0.0] * N

for i in range(N):
    if i == 0:
        D[i] = A[i] + d[i]
    else:
        D[i] = max(D[i - 1], A[i]) + d[i]

    if i == 0:
        D2[i] = D[i] + d2[i]
    else:
        D2[i] = max(D2[i - 1], D[i]) + d2[i]


max_time = max(D2) + 1
time = 0.0

timestamps1 = [0]
timestamps2 = [0]
timestamps = [0]
task1_t = [0]
task2_t = [0]
task_t = [0]
a_idx = 0
d_idx = 0
d2_idx = 0

while time <= max_time:
    task_delta_1 = 0
    task_delta_2 = 0

    if a_idx < len(A) and A[a_idx] <= time:
        a_idx += 1
        task_delta_1 += 1

    if d_idx < len(D) and D[d_idx] <= time:
        d_idx += 1
        task_delta_1 -= 1
        task_delta_2 += 1

    if d2_idx < len(D2) and D2[d2_idx] <= time:
        d2_idx += 1
        task_delta_2 -= 1

    if task_delta_1 != 0:
        task1_t.append(task1_t[-1] + task_delta_1)
        timestamps1.append(time)

    if task_delta_2 != 0:
        task2_t.append(task2_t[-1] + task_delta_2)
        timestamps2.append(time)

    if task_delta_1 + task_delta_2 != 0:
        task_t.append(task_t[-1] + task_delta_1 + task_delta_2)
        timestamps.append(time)

    time += 0.01


plt.plot(timestamps1, task1_t)
plt.plot(timestamps2, task2_t)
plt.plot(timestamps, task_t)
plt.legend(["Serwer 1", "Serwer 2", "Suma"])
plt.show()

plt.scatter(A, [D2[i] - A[i] for i in range(N)])
plt.show()

plt.scatter(D2, range(100))
plt.show()
