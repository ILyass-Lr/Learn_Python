#Programme qui affiche la racine carré d'un nombre donnée
from math import sqrt

while True:
    n = float(input("Veuillez entrer un nombre non négatif : "))
    if n >= 0:
        break
print(f"Le racine carré de {n} est {sqrt(n)}")


