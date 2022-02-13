import matplotlib.pyplot as plt
from symulacja import symuluj

b = 50
krok = 100 #1/krok
dokladnosc = 100
aty = {
    1:(1,"Black"),
    25:(2,"Black"),
    50:(3,"Black"),
    1000:(4,"Black") 
    }


for a in aty.keys():
    prawdopodobienstwa = list()
    lmaxy = list()
    z = a + b
    for i in range(int(krok/10),krok):
        
        p = i/krok
        q = 1 - p
    
        ra_s,ele = symuluj(a,b,p,dokladnosc)
        lmax = max(ele)
        lmaxy.append(lmax)

        prawdopodobienstwa.append(p)


    with plt.style.context('dark_background'):
        plt.subplot(2,2,aty.get(a)[0])
        plt.plot(prawdopodobienstwa, lmaxy, color = "#00628f")
        plt.title(f"a={a}, b={b}")
        plt.xlabel("p")
        plt.ylabel("Lmax")
        plt.suptitle("Problem E\nMaksymalna liczba gier w zaleznosci od prawopodobienstwa wygrania rundy")


plt.show()
