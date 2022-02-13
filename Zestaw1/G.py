from helpers import Player, simulate_games
from matplotlib import pyplot as plt

ps = [0.3, 0.5, 0.7]

for i in range(len(ps)):
    player_a = Player("A", ps[i], 50)
    player_b = Player("A", 1 - ps[i], 50)

    simulate_games([player_a, player_b], 1)

    x = range(len(player_a.wins_trajectory))

    plt.subplot(3, 2, 2 * i + 1)
    plt.plot(x, player_a.wins_trajectory)
    plt.title(f"p={ps[i]} wygrane")

    plt.subplot(3, 2, 2 * i + 2)
    plt.plot(x, player_a.capital_trajectory)
    plt.title(f"p={ps[i]} kapitał")

plt.show()
