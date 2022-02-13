import matplotlib.pyplot as plt
from symulacja import symuluj


dokladnosc = 100

plt.rcParams['axes.facecolor'] = "#8601AF"

pety = { 49/100:( 1, "#FEFE33" ), 1/2:( 2, "#FEFE33" ), 51/100:(3,"#FEFE33") }

for p in pety.keys():
    q = 1 - p
    aaa = list()
    ruiny_s = list()
    ruiny = list()
    
    for a in range(0,100):
        b = 100 - a
        z = a + b
        
        if p != 1/2:
            ra = (((q/p)**a) - ((q/p)**z)) / (1-((q/p)**z))
        else:
            ra = 1 - (a/z)

        ra_s, ELE = symuluj(a,b,p,dokladnosc)
        aaa.append(a)
        ruiny.append(ra)
        ruiny_s.append(ra_s)
    
    with plt.style.context('dark_background'):
        plt.subplot(3,1, pety.get(p)[0] )
        plt.plot(range(0,100), ruiny, color = "#ffa600")
        plt.plot(range(0,100), ruiny_s, 'o', color = "#00628f", markersize = 7)
        plt.xlabel("a")
        plt.ylabel("Prawdopodbienstwo Ruiny Gracza A")
        plt.title(f"Prawdopodobienstwo wygrania rundy = {p}")
        plt.suptitle("Problem C\nPrawdopodobienstwo ruiny Gracza A w zaleznosci od kapitalu poczatkowego")

plt.show()
