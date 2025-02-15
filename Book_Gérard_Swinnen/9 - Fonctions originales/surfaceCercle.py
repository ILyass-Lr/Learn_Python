# Fonction qui calcule l'Aire d'un cercle
from math import pi
def surfCercle(R):
    "Calcule la surface d'une cercle de rayon R"
    return  pi * R**2

# Programme Principal
rayon=eval(input("Veuillez entrez le rayon de votre cercle: "))
print(surfCercle(rayon))
