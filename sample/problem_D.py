from symulacja import symuluj
import matplotlib.pyplot as plt

pety = [ 1/5, 1/2, 4/5 ]

pety = {1/5:(1,"violet"), 1/2:(2,"darkviolet"), 4/5:(3,"indigo")}
for p in pety.keys():
    ra, ele = symuluj(p=p,N=20000)

    srednia = sum(ele)/len(ele)
    with plt.style.context('dark_background'):
        plt.subplot(  1,3,pety.get(p)[0]  )
        plt.hist(ele,color = "#00628f")
        plt.title(f"p = {p} Srednia = {srednia}")
        plt.xlabel("Liczba rund")
        plt.ylabel("Liczba gier")
        plt.suptitle("Problem D\nLiczba gier w zaleznosci od liczby rund")
    

plt.show()

