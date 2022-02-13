from helpers import Player, simulate_games, calculate_mean
from matplotlib import pyplot as plt


ps =[0.2, 0.5, 0.8]


for i in range(len(ps)):
    player_a = Player("A", ps[i], 50)
    player_b = Player("A", 1 - ps[i], 50)

    rounds = simulate_games([player_a, player_b], 5000)

    mean = calculate_mean(rounds)

    plt.subplot(len(ps), 1, i + 1)
    plt.hist(rounds, density=True)
    plt.title(f"Średnia: {mean}")

plt.show()
