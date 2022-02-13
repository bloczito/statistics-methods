import matplotlib.pyplot as plt
from numpy import log
from random import random

n = 1000


def calculate(lambd_A, lambd_D):
    a_i = [0.0] * n
    d_i = [0.0] * n

    for i in range(n):
        a_i[i] = - (log(random()) / lambd_A)
        d_i[i] = - (log(random()) / lambd_D)

    A = [sum(a_i[0: i + 1]) for i in range(len(a_i))]
    D = [0.0] * n
    for i in range(n):
        if i == 0:
            D[i] = A[0] + d_i[0]
        else:
            D[i] = max(D[i - 1], A[i]) + d_i[i]

    d_idx = 0
    a_idx = 0

    start = 0
    end = 0

    time_t = []
    task_t = []

    tasks = 0

    while d_idx < n:
        a_time = A[a_idx] if a_idx < n else 10000
        d_time = D[d_idx]
        task_delta = 0

        if a_time <= d_time:
            end = a_time
            task_delta = 1
            a_idx += 1
        else:
            end = d_time
            task_delta = -1
            d_idx += 1

        task_t.append(tasks)
        time_t.append(end - start)
        tasks += task_delta

        start = end

    counter = sum([task * time for task, time in zip(task_t, time_t)])

    En = counter / sum(time_t)

    Ri = [D[i] - A[i] for i in range(n)]
    Er = sum(Ri) / n

    return (Er, En)


# # LAMBDA A
# lambd_a_tasks = []
# lambd_a_time = []
# A = 200
#
# for a in range(1, A + 1):
#     Er, En = calculate(a, A / 2)
#     lambd_a_tasks.append(En)
#     lambd_a_time.append(Er)
#
# plt.subplot(2, 1, 1)
# plt.title("Ilość zadań w zależności od lambda_a")
# plt.plot(range(A), lambd_a_tasks)
#
# plt.subplot(2, 1, 2)
# plt.title("Czas oczekiwania w zależności od lambda_a")
# plt.plot(range(A), lambd_a_time)
#
# plt.show()
#
#
# # LAMBDA D
# lambd_d_tasks = []
# lambd_d_time = []
# D = 200
#
# for d in range(1, D + 1):
#     Er, En = calculate(D / 2, d)
#     lambd_d_tasks.append(En)
#     lambd_d_time.append(Er)
#
# plt.subplot(2, 1, 1)
# plt.title("Ilość zadań w zależności od lambda_d")
# plt.plot(range(D), lambd_d_tasks)
#
# plt.subplot(2, 1, 2)
# plt.title("Czas oczekiwania w zależności od lambda_d")
# plt.plot(range(D), lambd_d_time)
#
# plt.show()
#

# R
r_tasks = []
r_time = []
R = 200
a = R / 2
for r in range(1, R + 1):
    Er, En = calculate(a, a / r)
    r_tasks.append(En)
    r_time.append(Er)

plt.subplot(2, 1, 1)
plt.title("Ilość zadań w zależności od lambda_a / lambda_d")
plt.plot(range(R), r_tasks)

plt.subplot(2, 1, 2)
plt.title("Czas oczekiwania w zależności od lambda_a / lambda_d")
plt.plot(range(R), r_time)

plt.show()
