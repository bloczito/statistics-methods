import copy

from numpy import log
from random import random
from matplotlib import pyplot as plt

n = 10
lambd_A = 2
lambd_D = 10

arrival_times = [0.0] * n
done_times = [0.0] * n

for i in range(n):
    arrival_times[i] = - (log(random()) / lambd_A)
    done_times[i] = - (log(random()) / lambd_D)

max_time = max(sum(arrival_times), sum(done_times)) + arrival_times[0]

time = 0.0

time_t = [0]
task_t = [0]

last_arrival_time = 0
last_done_time = arrival_times[0]

tasks = 0

arrival_times_sum = [sum(arrival_times[0: i + 1]) for i in range(len(arrival_times))]
done_timestamps = []
D = [0.0] * n
for i in range(n):
    if i == 0:
        D[i] = arrival_times[0] + done_times[0]
    else:
        D[i] = max(D[i - 1], arrival_times_sum[i]) + done_times[i]

print(arrival_times)
print(done_times)

while time <= max_time or tasks > 0:
    tasks_to_add = 0
    if len(arrival_times) > 0 and time - last_arrival_time >= arrival_times[0]:
        tasks_to_add += 1
        tasks += 1
        last_arrival_time = time
        arrival_times.pop(0)

    if len(done_times) > 0 and time - last_done_time >= done_times[0] and task_t[-1] > 0:
        tasks_to_add -= 1
        tasks -= 1
        last_done_time = time
        done_times.pop(0)
        done_timestamps.append(time)

    time_t.append(time)
    task_t.append(task_t[-1] + tasks_to_add)

    time += 0.01


print(f"A) {arrival_times_sum}")
print(f"D) {D}")
print([D[i] - arrival_times_sum[i] for i in range(n)])

# A
# plt.plot(time_t, task_t)
plt.scatter(done_timestamps, [(D[i] - arrival_times_sum[i]) for i in range(n)])
# plt.show()

plt.scatter(done_timestamps, range(1, n + 1))
plt.show()



# print(zip(arrival_times_sum, done_timestamps))
# print([x for x in zip(arrival_times_sum, done_timestamps)])
# B
# plt.show()





