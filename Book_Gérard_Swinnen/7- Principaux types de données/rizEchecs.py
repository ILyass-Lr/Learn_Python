#programme qui affiche le nombre de riz a mettre dans chaque case de l'echec
#telle que chaque case sera le doube de celle qui la précède

i, riz = 1, 1

print('\tEn notation entier : ')
while i<65:
    print(f"la case {i} : {riz}")
    i, riz = i+1, riz * 2
print('\tEn notation scentifique : ')
i, riz = 1, 1
while i<65:
    print(f"la case {i} : {riz:.3e}")
    i, riz = i+1, riz * 2
    
