import os

from matplotlib import pyplot as plt
from helpers import Player, simulate_games, get_theoretical_result
ruin_ps = []
start_capitals = []


for a in range(1, 100):
    # os.system("clear")
    print(f"Simulating... {a} %")

    player_a = Player("A", 0.5, a)
    player_b = Player("B", 0.5, 100 - a)

    simulate_games([player_a, player_b], 100)

    start_capitals.append(a)
    ruin_ps.append(player_a.ruin_p)

plt.plot(start_capitals, ruin_ps)
plt.show()


x = [a for a in range(1, 100)]
y = [get_theoretical_result(a, 100 - 1, 0.5, 0.5) for a in x]

plt.plot(x, y)
plt.show()

# N = 100
# probA = 0.5000
# a = 50
# b = 50
#
# runi_ps = []
# aas = []
#
# def gamblersRuin(N, z, prob):
#     for a in range(1, 100):
#         wins = [False] * N
#
#         for i in range(N):
#             p1b = a
#             p2b = z - a
#             while p1b > 0 and p2b > 0:
#                 p1_win = np.random.uniform(0, 1) < prob
#                 p1b = p1b + 1 if p1_win else p1b - 1
#                 p2b = p2b - 1 if p1_win else p2b + 1
#             wins[i] = p1b > 0
#         runi_ps.append(1 - (sum(wins)/N))
#         aas.append(a)
#
# gamblersRuin(100, 100, probA)
#
# plt.plot(aas, runi_ps)
# plt.show()