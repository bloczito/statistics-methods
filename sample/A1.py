import random
import math
import matplotlib.pyplot as plt
import numpy.random

def wygeneruj_punkty_w_kwadracie( N: int ) -> list():
    pary = list()
    for i in range ( 1, N ):
        v1 = random.uniform( -1, 1 )
        v2 = random.uniform( -1, 1 )
        pary.append( ( v1, v2 ) )
    return pary

def zawez_do_kola( punkty: list() ) -> list():
    nowe_punkty = [ x for x in punkty if math.sqrt( ( (x[0])**2 ) + ( (x[1])**2 ) ) < 1 ]
    return nowe_punkty

def zmien_na_losowe( punkty: list() ) -> list():
    nowe_punkty = list()
    for punkt in punkty:
        v1 = punkt[0]
        v2 = punkt[1]
        r2 = ( v1 )**2 + ( v2 )**2
        if r2 < 1:
            t = math.sqrt( ( ( -2 ) * ( math.log(r2) ) ) / ( r2 ) )
            y1 = v1 * t
            y2 = v2 * t
            nowe_punkty.append( ( y1, y2 ) )

    return nowe_punkty



def wygeneruj_normalne( N: int ) -> list():
    lista = list()
    for i in range(1, N):
        x = numpy.random.normal()
        lista.append(x)
    return lista



def policz_wariancje_i_srednia( zmienne: list() ) -> int:
    srednia = 0
    for zmienna in zmienne:
        srednia += zmienna

    srednia = srednia / len(zmienne)
    suma = 0
    for zmienna in zmienne:
        ss = ( zmienna - srednia )**2
        suma += ss
    suma = suma / len(zmienne)

    return srednia,suma



N = 10000

punkciki = wygeneruj_punkty_w_kwadracie( N )
punkciki = zawez_do_kola( punkciki )
punkciki = zmien_na_losowe(punkciki)
iksy = [ x[0] for x in punkciki ]
igreki = [ x[1] for x in punkciki ]
wszystkie = iksy + igreki


normalne = wygeneruj_normalne( N )
srednia, wariancja = policz_wariancje_i_srednia(wszystkie)
print(f"Mean of variables obtained from Marsaglia method: {srednia}")
print("Mean of variables in Normal(0,1) distribution: 0")
print(f"Variance of variables obtained from Marsaglia method: {wariancja}")
print("Variance of variables in Normal N(0,1) distribution: 1")

plt.subplot(2,1,1)
plt.hist(wszystkie,color = "red")
plt.title("Marsaglia/Polar method")

plt.subplot(2,1,2)
plt.hist(normalne)
plt.title("Normal distribution")
plt.show()