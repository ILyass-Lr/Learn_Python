#Programme qui trie affcihe deux liste, lun des pairs et l'autre des impaires
#en se basant d'une liste donné


Liste = [32, 5, 12, 8, 3, 75, 2, 15]

i,lPaire,lImpaire = 0,[],[]
while i < len(Liste):
    if Liste[i]%2==0:
        lPaire.append(Liste[i])
    else:
        lImpaire.append(Liste[i])
    i += 1

print("la liste des pairs est :",lPaire)
print("la liste des pairs est :",lImpaire)




