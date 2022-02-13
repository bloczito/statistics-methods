from numpy import s_
from drzewko import wylicz_PK_N
from symulacja import symuluj_kapitaly
import matplotlib.pyplot as plt
from collections import Counter


prawdopodobienstwa = [1/2, 1/5, 4/5]


rundy = { 2:(1,4), 10:(2,5), 20:(3,6) }

for runda in rundy.keys():
    s_prawdo = list()
    kapitaly, p = wylicz_PK_N(50,runda,1/2)

    aty = symuluj_kapitaly(50,runda,1/2,1000)

    policzone = Counter(aty)
    wszystkie = 0
    for element in policzone.values():
        wszystkie = wszystkie + element

    for element in policzone:
        s_prawdo.append( policzone.get(element) / wszystkie )

    s_kapitaly = policzone.keys()

    with plt.style.context('dark_background'):
        plt.subplot(2,3,rundy.get(runda)[0])
        plt.bar(kapitaly,p,color = "#236AB9")
        plt.xlabel("Kapital")
        plt.ylabel("Prawdopodobienstwo")
        plt.title(f"Wartosc analityczna Ilosc rund = {runda}")
        plt.subplot(2,3,rundy.get(runda)[1])
        plt.bar(s_kapitaly, s_prawdo, color = "#FC7307")
        plt.xlabel("Kapital")
        plt.ylabel("Prawdopodobienstwo")
        plt.title(f"Symulacja Ilosc rund = {runda}")
        plt.suptitle("Problem F\nPrawdopodobienstwo posiadania kapitalu K po N rundach")

plt.show()