from random import *
u,v = randint(2**2,2**4),randint(2**2,2**4)
a,b = bin(max(u,v)),bin(min(u,v))
n=len(a)-len(b)
print('    '+a[2:])
print('x   '+n*' '+b[2:])
print("   _______________")
print("            ?      ")
continuer = 1
while continuer:
    rep=input("Ecrire votre réponse : ")
    if int(rep,2)==int(a,2)*int(b,2):
        print ("Bonne réponse !")
        continuer=0
    else:
        print("Mauvaise réponse...")
        
