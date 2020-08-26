from matplotlib import pyplot
from math import *

X=[i for i in range(2,1000)]
Y=[x for x in X]
Z=[log2(x) for x in X]

pyplot.ylim([0,20])
pyplot.xlabel("Taille de l'entrée")
pyplot.ylabel("Nombre d'étapes")
pyplot.grid()
pyplot.plot(X,Y,label='Balayage')
pyplot.plot(X,Z,label='Dichotomie')
pyplot.legend(loc=0)
pyplot.show()
