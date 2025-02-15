#Programme qui permette d'encoder des valeurs dans une liste

liste = []
while True:
    inp = input(" Veuillez entrer une valeur : ")
    if inp == '':
        break
    liste.append(int(inp))

print(liste)
