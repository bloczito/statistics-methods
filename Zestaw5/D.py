from numpy import log
from random import random
from copy import deepcopy
from matplotlib import pyplot as plt


def get_time(lambd):
    return - (log(random()) / lambd)


N = 100
lambd_a = 10
lambd_d = 6

a = [get_time(lambd_a) for _ in range(N)]
d = [1 / lambd_d for _ in range(N)]
A = [sum(a[0: i + 1]) for i in range(len(a))]
D = [0.0] * N

for i in range(N):
    if i == 0:
        D[i] = A[i] + d[i]
    else:
        D[i] = max(D[i - 1], A[i]) + d[i]


max_time = max(D) + 1
time = 0.0

timestamps = [0.0]
done_timestamps = [0.0] * N
task_t = [0]
a_idx = 0
d_idx = 0
d2_idx = 0

next_idx = 0

s1_free = True
s2_free = True

last_d1 = a[0]
last_d2 = a[1]

tasks = 0

while time <= max_time or tasks > 0:
    task_delta = 0

    if a_idx < len(A) and A[a_idx] <= time:
        a_idx += 1
        task_delta += 1
        tasks += 1

    if s1_free and next_idx < N and tasks > 0:
        d_idx = next_idx
        next_idx += 1
        s1_free = False
        tasks -= 1

    if s2_free and next_idx < N and tasks > 0:
        d2_idx = next_idx
        next_idx += 1
        s2_free = False
        tasks -= 1

    if 0 <= d_idx < len(D) and d[d_idx] < time - last_d1 and not s1_free:
        done_timestamps[d_idx] = time
        task_delta -= 1
        d_idx = -1
        last_d1 = time
        s1_free = True

    if 0 <= d2_idx < len(D) and d[d2_idx] < time - last_d2 and not s2_free:
        done_timestamps[d2_idx] = time
        task_delta -= 1
        d2_idx = -1
        last_d2 = time
        s2_free = True

    if task_delta != 0:
        task_t.append(task_t[-1] + task_delta)
        timestamps.append(time)

    time += 0.0001

sorted_timestamps = deepcopy(done_timestamps)
sorted_timestamps.sort()

plt.scatter(timestamps, task_t)
plt.title("Liczba zadań w kolejce w zależności od czasu")
plt.show()

plt.scatter(done_timestamps, [done_timestamps[i] - A[i] for i in range(N)])
plt.show()


plt.scatter(sorted_timestamps, range(100))
plt.show()
