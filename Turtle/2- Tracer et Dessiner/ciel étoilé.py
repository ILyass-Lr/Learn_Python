import turtle
from random import randint

LARGEUR, HAUTEUR = 640, 480
LONGUEUR_MIN, LONGUEUR_MAX = 5, 20


def deplacer_sans_tracer(x, y=None):
    """Fonction pour se déplacer à un point sans tracer"""
    turtle.up()
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) == 2:
        turtle.goto(x)
    else:
        turtle.goto(x, y)
    turtle.down()


def etoile(longueur):
    """Fonction pour dessiner une étoile"""
    turtle.setheading(180 - 2 * 72)
    for i in range(5):
        turtle.forward(longueur)
        turtle.left(180 - 180 / 5)


if __name__ == "__main__":
    turtle.setup(LARGEUR, HAUTEUR)
    turtle.speed(0)  # Met la vitesse de traçage la plus rapide
    nb_etoiles, longueur_etoile = 20, 0
    for i in range(nb_etoiles):
        longueur_etoile = randint(LONGUEUR_MIN, LONGUEUR_MAX)
        deplacer_sans_tracer(randint(-LARGEUR // 2 + LONGUEUR_MAX // 2, LARGEUR // 2 - LONGUEUR_MAX),
                             randint(-HAUTEUR // 2 + LONGUEUR_MAX // 2, HAUTEUR // 2 - LONGUEUR_MAX))
        etoile(longueur_etoile)
    deplacer_sans_tracer(0, 0)
    turtle.exitonclick()