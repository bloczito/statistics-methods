from simulate import Player, simulate
import matplotlib.pyplot as plt
from statistics import mean



ms = list()
ps = list()
for p in range(1,1000):
    p = p/1000
    pA = Player("A", p, 50 )
    pB = Player("B", 1-p, 50 )

    print(p)
    rounds_list = simulate([pA, pB], 100)

    m = max(rounds_list)
    ms.append(m)
    ps.append(p)

plt.plot(ps,ms)
plt.show()    