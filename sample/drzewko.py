from collections import Counter


def wylicz_PK_N(a,N,p):
    stopnie = list()
    stopnie.append( [ (a,0) ] )

    for wiersz in range(1,N+1):
        ostatni_wiersz = stopnie.pop()
        stopnie.append(ostatni_wiersz)
        obecny_wiersz = list()
        for element in ostatni_wiersz:
            obecny_wiersz.append( (element[0] - 1 , element[1]) ) # przegrana
            obecny_wiersz.append( (element[0] + 1 , element[1] + 1) ) # wygrana
        stopnie.append(obecny_wiersz)

    ostatni_wiersz = stopnie.pop()
    policzony_wiersz = Counter(ostatni_wiersz)

    kapitaly = list()
    prawdopodobienstwa = list()
    for element in policzony_wiersz.keys():
        PK = (policzony_wiersz.get(element)) * ((p)**(element[1])) * ( (1-p)**(N - element[1]) )
        kapitaly.append(element[0])
        prawdopodobienstwa.append(PK)
    return kapitaly, prawdopodobienstwa