""" Module dessins_tortue.py
Contient des fonctions pour le tracage de:
- Carrées dans différentes angles
- Triangle dans différentes angles
- Étoile de 5 côtés
- Étoile de 6 côtés
"""
from turtle import *
from math import sqrt
def carre(taille, angle=0):
    "Tracer une carrer dans un angle donnée"
    setheading(angle)
    color("red")
    for i in range(4):
        fd(taille)
        right(90)


def triangle(taille, couleur, angle=0):
    "Tracer un triangle dans un angle donnée"
    setheading(angle)
    color(couleur)
    for i in range(3):
        fd(taille)
        right(120)

        

def etoile5(taille):
    """ Une étoile de 5 branches est inscrit dans un
    polygone régulier de 5 côté constitué de 5 triangle isocèle dont le
    sommet est egale à 360 / 5 Règle: la mesure d'un angle inscrit dans
    un cercle interceptant un cercle vaut moitié de celle de l'angle au
    centre interceptant le même angle

     Dans notre cas: L'angle inscrit est cette qu'on cherche
     L'angle au centre est 360 / 5
     => L'angle entre le côtés de l'étoile est donc (360 / 5) / 2
    """
    color("blue")
    for i in range(5):
        fd(taille)
        right(180 - 360 / 5 / 2)


def etoile6(taille):
    "Tracer une étoile à 6 branche"
    triangle(taille, "blue")
    (x, y) = pos()
    up()
    goto(x, y+sqrt(13/12)*taille)
    down()
    triangle(taille, "blue", angle = 300)
    
    
