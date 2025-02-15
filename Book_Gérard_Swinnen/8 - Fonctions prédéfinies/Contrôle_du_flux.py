''' Note : l'association des fonctions list(eval()) permet de convertir
    en liste toute chaîne de valeurs séparées par des virgules :En fait, la fonction eval()
    évalue le contenu de la dont elle doit renvoyer le résultat. Par exemple : eval("7 + 5") renvoie
    l'entier 12. Si on lui fournit une chaîne de valeurs séparées par des virgules, cela correspond pour
    elle à un tuple. Les tuples sont des séquences apparentées aux listes.
'''
ch =input()
nn = list(eval(ch))
max, index = nn[0], 'premier'
if nn[1] > max: # ne pas omettre le double point !
    max = nn[1]
    index = 'second'
if nn[2] > max:
    max = nn[2]
    index = 'troisième'
print("Le plus grand de ces nombres est", max)
print("Ce nombre est le", index, "de votre liste.")
