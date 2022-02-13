from symulacja import symuluj_trajektorie
import matplotlib.pyplot as plt


licznik = 0

prawdopodobienstwa = {49/100:(1,2), 1/2:(3,4), 51/100:(5,6)}
a = 50
b = 50

for p in prawdopodobienstwa:

    lr, wyg, kapi, w = symuluj_trajektorie(a,b,p)
    with plt.style.context('dark_background'):
        plt.subplot(3,2,prawdopodobienstwa.get(p)[0])
        plt.plot(range(lr),kapi, color = "#236AB9")
        plt.title(f"Trajektoria kapitalu p = {p}")
        plt.xlabel("Liczba rund")
        plt.ylabel("Kapital")
        plt.subplot(3,2,prawdopodobienstwa.get(p)[1])
        plt.plot(range(lr), wyg, color = "#FC7307")
        plt.title(f"Trajektoria wygranych p = {p}")
        plt.xlabel("Liczba rund")
        plt.ylabel("Liczba wygranych")
        plt.suptitle("Problem G\Trajektorie Kapitalu i Wygranych")

plt.show()

