'''
Dessiner une série de triangles équilatéraux de différentes
couleurs en utilisant des fonctions.
'''
from turtle import *
def deplacer_sans_tracer(x, y=0):
    "Fonction pour pouvoir déplacer à de nouveaux coordonnées sans tracer"
    up()
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) == 2:
        goto(x)
    else:
        goto(x, y)
    down()


def triangle(couleur):
    "Fonction pour pouvoir tracer une Traingle"
    color(couleur)
    begin_fill()
    for i in range(3):
        fd(130)
        left(120)
    end_fill()

# Programme Principal
deplacer_sans_tracer(-220, 0)
triangle("red")
deplacer_sans_tracer(-50, 0)
triangle("green")
deplacer_sans_tracer(120, 0)
triangle("blue")
        
