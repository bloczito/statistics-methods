from simulate import Player, simulate
import matplotlib.pyplot as plt

ps = [ ( 49/100, 1), ( 50/100, 2 ), ( 51/100, 3 ) ]

for p in ps:
    Rs = list()
    aas = list()
    for a in range(1,100):
        pA = Player("A",p[0],a)
        pB = Player("B",1-p[0], 100-a)

        print(a)
        x = simulate( [ pA, pB ], 100 )

        aas.append(a)
        Rs.append(pA.R)

    plt.subplot( 3, 1, p[1] )
    plt.plot( aas, Rs, 'o' )

plt.show()