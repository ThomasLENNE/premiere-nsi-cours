from random import *
u,v = randint(2**6,2**13),randint(2**6,2**13)
a,b = hex(max(u,v)),hex(min(u,v))
n=len(a)-len(b)
print('    '+a[2:])
print('+   '+n*' '+b[2:])
print("   _______________")
print("            ?      ")
continuer = 1
while continuer:
    rep=input("Ecrire votre réponse : ")
    if int(rep,16)==int(a,16)+int(b,16):
        print ("Bonne réponse !")
        continuer=0
    else:
        print("Mauvaise réponse...")
        
