#devine un nombre :
from random import *

continuer = 'o'
while continuer=='o' :
    
    N=randint(0,127)
    n =False
    i=0
    print("J'ai choisi un nombre entier entre 0 et 127. Deviner ce nombre")
    while n != N :
        n=int(eval(input("Quelle est votre proposition ?")))
        i=i+1
        if n == N :
            print("Gagné en "+ str(i) +" coups")
            continuer = input("Continuer le jeu ? (o/n)")

        else:
            if n > N :
                print("Plus petit")
            else : 
                print("Plus grand")
