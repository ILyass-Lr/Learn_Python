# Premier essai de script Python
# petit programme simple affichant une suite de Fibonacci, c.à.d. une suite
# de nombres dont chaque terme est égal à la somme des deux précédents.
a, b, c = 1, 1, 1 # a & b servent au calcul des termes successifs
# c est un simple compteur
print("1 :",b) # affichage du premier terme
while c<50: # nous afficherons 15 termes au total
    a, b, c = b, a+b, c+1
    print(c,":",b)
