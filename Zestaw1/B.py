import matplotlib.pyplot as plt
from time import time
from helpers import Player, simulate_games, get_theoretical_result


capitals = [
    (10, 10), (10, 25), (10, 50),
    (25, 10), (25, 25), (25, 50),
    (50, 10), (50, 25), (50, 50)
]

bottom_range = 30
top_range = 70
divider = 100

for cap_a, cap_b in capitals:
    ruin_p_list = []
    p_list = []
    idx = capitals.index((cap_a, cap_b)) + 1
    start_time = time()

    for x in range(bottom_range, top_range):
        p = x / divider
        player_A = Player("A", p, cap_a)
        player_B = Player("B", 1 - p, cap_b)

        simulate_games([player_A, player_B], 100)

        ruin_p_list.append(player_A.ruin_p)
        p_list.append(p)

        plt.subplot(3, 3, idx)
        plt.plot(p_list, ruin_p_list)
        plt.title(f"a = {player_A.start_capital}, b = {player_B.start_capital}")

        # plt.subplot(3, 3, idx)
        x = [p / divider for p in range(bottom_range, top_range)]
        y = [get_theoretical_result(cap_a, cap_b, p / divider, 1 - (p / divider)) for p in range(bottom_range, top_range)]
        plt.plot(x, y, color="salmon")

    end_time = time()
    print(f"Done game {idx} - {round(end_time - start_time, 2)} s")

plt.show()



# plt.plot(x, y)
plt.show()
