from simulate import Player, simulate
import matplotlib.pyplot as plt

# Symulujemy X gier z roznymi wartosciami p
# Obliczamy R


capitals = [
    ( 1, 1, 1 ), ( 1, 25, 2 ), ( 1, 50, 3 ),
    ( 25, 1, 4 ), ( 25, 25, 5 ), ( 25, 50, 6 ),
    ( 50, 1, 7 ), ( 50, 25, 8 ), ( 50, 50, 9 )
    ]

X = 1000
for ab in capitals:
    Rs = list()
    ps = list()
    for i in range(300, 700):
        p = i/X
        pA = Player("A",p,ab[0])
        pB = Player("B",1-p,ab[1])
        x = simulate([pA,pB],100)
        Rs.append(pA.R)
        ps.append(p)

        plt.subplot( 3, 3, ab[2] )
        plt.plot(ps,Rs, "o")
        plt.title( f"a = {pA.CC}, b = {pB.CC}" )
    print(f"XXX: {ab[2]}")

plt.show()
