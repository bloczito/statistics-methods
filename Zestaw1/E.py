from helpers import Player, simulate_games
from matplotlib import pyplot as plt

N = 100
rounds = []
ps = []

for x in range(1, N):
    p = x / N

    player_a = Player("A", p, 50)
    player_b = Player("B", 1 - p, 50)

    rounds_played = simulate_games([player_a, player_b], 100)

    ps.append(p)
    rounds.append(max(rounds_played))

plt.plot(ps, rounds)
plt.show()

