#Programme qui affiche  les 20 premiers termes de la table de multiplication par 7
# en signalant au passage (à l'aide d'une astérique) ceux qui sont multiples de 3.

i = 1      #compteur allant de 1 à 20
while i<=20:
    if (i*7 % 3 == 0):  
        print(f"{i*7}*",end=" ")
    else:
        print(i*7,end=" ")
    i+=1
