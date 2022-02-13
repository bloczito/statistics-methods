from symulacja import simulate
from symulacja import Player

p1 = Player("A", 1/5, 10)
p2 = Player("B", 1/5, 10)
p3 = Player("C", 1/5, 10)
p4 = Player("D", 1/5, 10)
p5 = Player("E", 1/5, 10)

plist = [ p1, p2, p3, p4, p5 ]

simulate(plist,1000)

for player in plist:
    print(player)