from numpy import log
from random import random
from matplotlib import pyplot as plt

n = 1000
lambd_A = 15
lambd_D = 8

a_i = [0.0] * n
d_i = [0.0] * n

for i in range(n):
    a_i[i] = - (log(random()) / lambd_A)
    d_i[i] = - (log(random()) / lambd_D)

max_time = max(sum(a_i), sum(d_i)) + a_i[0]

time = 0.0

time_t = [0]
task_t = [0]

last_arrival_time = 0
last_done_time = a_i[0]

tasks = 0

A = [sum(a_i[0: i + 1]) for i in range(len(a_i))]
D = [0.0] * n

for i in range(n):
    if i == 0:
        D[i] = a_i[0] + d_i[0]
    else:
        D[i] = max(D[i - 1], A[i]) + d_i[i]

done_timestamps = []

while time <= max_time or tasks > 0:
    tasks_to_add = 0
    if len(a_i) > 0 and time - last_arrival_time >= a_i[0]:
        tasks_to_add += 1
        tasks += 1
        last_arrival_time = time
        a_i.pop(0)

    if len(d_i) > 0 and time - last_done_time >= d_i[0] and task_t[-1] > 0:
        tasks_to_add -= 1
        tasks -= 1
        last_done_time = time
        d_i.pop(0)
        done_timestamps.append(time)

    time_t.append(time)
    task_t.append(task_t[-1] + tasks_to_add)

    time += 0.01




# A
# plt.plot(time_t, task_t)
# plt.scatter(done_timestamps, [(D[i] - arrival_times_sum[i]) for i in range(n)])
# plt.show()

plt.title("Liczba zadań w kolejce w zależności od czasu")
plt.plot(time_t, task_t)
plt.show()

plt.title("Czas oczekiwania na wykonanie w zależności od czasu")
plt.plot(done_timestamps, [D[i] - A[i] for i in range(n)])
plt.plot(time_t, [(lambd_A - lambd_D) / lambd_D * t for t in time_t])
plt.show()

plt.title("Liczba wykonanych w zależności od czasu")
plt.plot(done_timestamps, range(1, n + 1))
plt.plot(time_t, [(lambd_A - lambd_D) * t for t in time_t])
plt.show()


plt.title("(lambda_A - lambda_D) * t")
plt.show()


plt.title("(lambda_A - lambda_D) / lambda_D * t")
plt.show()


# print(zip(arrival_times_sum, done_timestamps))
# print([x for x in zip(arrival_times_sum, done_timestamps)])
# B
# plt.show()





