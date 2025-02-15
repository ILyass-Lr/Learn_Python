#Programme qui stocke les notes d'élèves dans une liste jusqu'à l'utilisateur entre
#une valeur négatif, puis affcher le nombre de notes entrées, le max et le min et le
#moyenne à chaque itération
min, max, s, l, i = 10e10,-1, 0, [], 1
while True:
    print("Veuillez entrez la note numéro",i,": ",end = " ")
    n=float(input())
    if n<0:
        break
    l.append(n)
    s += n
    if n > max:
        max = n
    if n < min:
        min = n
    print("Vous avez entrez",i,"nombre(s)")
    print("La note la plus hausse est :",max)
    print("La note la plus basse est :",min)
    print(f"La moyenne est : {s / i:.2f}")
    i += 1



