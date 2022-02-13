from numpy import log
from random import random

n = 1000
lambd_A = 2
lambd_D = 5

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

print(f"E(R) * lambda_A == E(N)")
print(f"{Er * lambd_A} == {En}")



