#Programme qui affiche le plus grand élement dans une liste


Liste = [32, 5, 12, 8, 3, 75, 2, 15]

i ,max = 1, Liste[0]
while i < len(Liste):
    if Liste[i]>max:
        max = Liste[i]
    i += 1

print("le plus grand élément de cette liste a la valeur:",max)




