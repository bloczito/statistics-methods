import numpy as np
import matplotlib.pyplot as plt


def get_theoretical_result(a, b, pa, pb):
    if pa != 0.5:
        z = a + b
        counter = (pb / pa) ** a - (pb/pa) ** z
        denominator = 1 - (pb / pa) ** z
        return counter / denominator
    else:
        return 1 - a / (a + b)


def simulate_ruin(a, b, N):
    win_p = []
    for i in range(30, 70):
        wins = [False] * N
        for j in range(N):
            p1b = a
            p2b = b
            while p1b > 0 and p2b > 0:
                p1_win = np.random.uniform(0, 1) < i / 100
                p1b = p1b + 1 if p1_win else p1b - 1
                p2b = p2b - 1 if p1_win else p2b + 1
            wins[j] = p1b > 0
        win_p.append(1 - (sum(wins) / N))
    return win_p




N = 100
pa = 0.5001
a = 50
b = 50


x = []
y = []

# for i in range(30, 70):
#     probA = i/N
#     x.append(gamblersRuin(N, a, b, probA))
#     y.append(probA)

# for i in range(30, 70):
#     probA = i/N
#     x.append(gambersRuinPreciseForumla(probA, 1-probA, 1, 50))
#     y.append(probA)
#
x = [x for x in range(30, 70)]

plt.plot(x, simulate_ruin(a, b, 100))
plt.show()
