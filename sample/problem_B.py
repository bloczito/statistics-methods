import matplotlib.pyplot as plt
from symulacja import symuluj

b = 50
ra = 0
krok = 1000 #1/krok
dokladnosc = 100
aty = {
    1:(1,"Black"),
    25:(2,"Black"),
    50:(3,"Black"),
    100:(4,"Black") 
    }

plt.rcParams['axes.facecolor'] = "#8601AF"

for a in aty.keys():
    prawdopodobienstwa = list()
    ruiny_s = list()
    ruiny = list()
    z = a + b
    for i in range(100,1000):
        
        p = i/krok
        q = 1 - p
    
        if p != q:
            ra = (((q/p)**a) - ((q/p)**z)) / (1-((q/p)**z))
        else:
            ra = 1 - (a/z)

        ra_s,ele = symuluj(a,b,p,dokladnosc)

        prawdopodobienstwa.append(p)
        ruiny.append(ra)
        ruiny_s.append(ra_s)
    with plt.style.context('dark_background'):
        plt.subplot(2,2,aty.get(a)[0])
        plt.plot(prawdopodobienstwa, ruiny, color = "#ffa600" )
        plt.plot(prawdopodobienstwa, ruiny_s, 'o', color = "#00628f", markersize = 4 )
        plt.title(f"a={a}, b={b}")
        plt.xlabel("p")
        plt.ylabel("ra")
        plt.suptitle("Problem B\nPrawdopodobienstwo ruiny gracza A w zaleznosci od prawdopodobienstwa wygrania rundy")



plt.show()
