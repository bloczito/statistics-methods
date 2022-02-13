from simulate import Player, simulate
import matplotlib.pyplot as plt

ps = [ ( 30/100, 1 ), ( 1/2, 2 ), ( 80/100, 3 ) ]

for p in ps:
    pA = Player("A", p[0], 100)
    pB = Player("B", 1-p[0], 100)

    x = simulate( [ pA, pB ], 1 )

    x = x[0]
    x = range(len(pA.wt))
    plt.subplot(3,1,p[1])
    plt.plot(x,pA.wt)
plt.show()