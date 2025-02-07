import turtle
import math
COTE_TRIANGLE = 550
def courbe_koch(longueur, etape):
    """Fonction récursive pour dessiner une courbe de Von Koch
    (une fonction récursive étant une fonction s'appelant elle-même"""
    if etape == 0:
        turtle.forward(longueur)
    else:
        courbe_koch(longueur / 3, etape - 1)
        turtle.left(60)
        courbe_koch(longueur / 3, etape - 1)
        turtle.right(120)
        courbe_koch(longueur / 3, etape - 1)
        turtle.left(60)
        courbe_koch(longueur / 3, etape - 1)


def flocon_koch(longueur, etape):
    """Fonction pour dessiner un flocon de Von Koch
    depuis le coin haut gauche"""
    for i in range(3):  # Pour chaque côté du triangle initial
        courbe_koch(longueur, etape)  # Courbe de Von Koch
        turtle.right(120)


if __name__ == "__main__":
    turtle.up()
    turtle.goto(-COTE_TRIANGLE / 2, (math.sqrt(3) / 4) * COTE_TRIANGLE)
    turtle.down()
    turtle.speed(0)
    flocon_koch(COTE_TRIANGLE, 4)
    turtle.hideturtle()
    turtle.exitonclick()