import matplotlib.pyplot as plt
import math
import random

def FGP(y: float, y0: float, gamma: float) -> float:
    return 1 / ( ( ( math.pi ) * gamma ) * ( ( 1 ) + ( ( y - y0 ) / ( gamma ) )**2 ) )

def ODDYS(x: float, x0: float, gamma: float) -> float:
    return x0 + ( gamma * ( math.tan( ( math.pi ) * ( x - (1/2) ) ) ) )




N = 10000

ixy = list()
ygreki = list()
y1greki = list()

for i in range( N ):
    x = -5 + i*0.001
    y = FGP(x,0,1/2)
    y1 = ODDYS(random.random(),0,1/2)
    ixy.append(x)
    ygreki.append(y)
    y1greki.append(y1)

plt.hist(y1greki,range=[-5, 5], density=True, bins=40)
plt.plot(ixy,ygreki,color = "red")
plt.show()