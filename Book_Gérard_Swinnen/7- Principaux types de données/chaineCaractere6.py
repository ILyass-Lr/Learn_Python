#Programme qui divise une liste des chaînes en deux
#L'un contenant les chaînes < 6 caractères et l'autre
#contenat les chaînes avec 6 caractèes ou plus


lChaine = [ 'Jean' , 'Maximilien' , 'Brigitte' , 'Sonia' , 'Jean-Pierre' , 'Sandra' ]

i,lMoins6,l6Plus = 0,[],[]
while i < len(lChaine):
    if len(lChaine[i])<6:
        lMoins6.append(lChaine[i])
    else:
        l6Plus.append(lChaine[i])
    i += 1

print("la liste des chaînes comportante moins de 6 caractères est :",lMoins6)
print("la liste des chaînes comportante plus de 6 caractères :",l6Plus)


