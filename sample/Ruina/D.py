from simulate import Player, simulate
import matplotlib.pyplot as plt
from statistics import mean

ps = [ ( 1/5, 1 ), ( 1/2, 2 ), ( 4/5, 3 ) ]


for p in ps:

    pA = Player("A", p[0], 50 )
    pB = Player("B", 1-p[0], 50 )

    rounds_list = simulate([pA, pB], 2000)

    m = mean(rounds_list)
    plt.subplot(3,1,p[1])
    plt.hist(rounds_list, density = True)
    plt.title(f"Mean: {m}")

plt.show()    