#Programme qui affiche  les 50 premiers termes de la table de multiplication par 13
# mais n'affiche que ceux qui sont multiples de 7.

i = 1      #compteur allant de 1 à 50
while i<=50:
    #calcule de terme
    t = i * 13 
    #verifier si le terme est multiple de 7
    if (t % 7 == 0):  
        print(t ,end=" ")
    i+=1
