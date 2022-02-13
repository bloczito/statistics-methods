from Zestaw1.helpers import Player, simulate_games
from matplotlib import pyplot as plt

p1 = Player("A", 0.2, 25)
p2 = Player("B", 0.2, 25)
p3 = Player("C", 0.2, 25)
p4 = Player("D", 0.2, 25)
p5 = Player("E", 0.2, 25)

players = [p1, p2, p3, p4, p5]

simulate_games(players, 1000)

for idx in range(len(players)):
    plt.subplot(3, 2, idx + 1)
    p = players[idx]

    plt.title(f"{p.name} - kapitał")
    x = range(len(p.capital_trajectory))
    plt.plot(p.capital_trajectory)

plt.show()

for idx in range(len(players)):
    plt.subplot(3, 2, idx + 1)
    p = players[idx]

    plt.title(f"{p.name} - wygrane")
    x = range(len(p.wins_trajectory))
    plt.plot(p.wins_trajectory)

plt.show()
