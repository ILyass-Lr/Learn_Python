#Programme qui affiche chaque chaîne avec le nombre de caractères correspondant

lisCh= ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien',
'Alexandre-Benoît', 'Louise']

c = 0 # compteur
while c < len(lisCh):
    print(lisCh[c],":",len(lisCh[c]))
    c += 1



