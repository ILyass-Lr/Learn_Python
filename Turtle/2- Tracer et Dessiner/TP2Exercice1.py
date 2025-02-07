import turtle


def deplacer_sans_tracer(x, y=None):
    """Fonction pour se déplacer à un point sans tracer"""
    turtle.up()
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) == 2:
        turtle.goto(x)
    else:
        turtle.goto(x, y)
    turtle.down()


def carre(longueur):
    """Fonction pour tracer un carré depuis le coin bas gauche"""
    for nb_cote in range(4):
        turtle.forward(longueur)
        turtle.left(90)


def point_octogone(longueur, diametre=5, couleur='black'):
    """Fonction pour faire les points des sommets d'un octogone"""
    for nb_cote in range(8):
        turtle.dot(diametre, couleur)
        turtle.up();
        turtle.forward(longueur);
        turtle.down()
        turtle.left(360 / 8)


if __name__ == "__main__":
    # Deux carrés
    longueurs_carre = [90, 180]
    for longueur in longueurs_carre:
        deplacer_sans_tracer(-longueur / 2, -longueur / 2)
        carre(longueur)
    # Cercle
    rayon = turtle.distance(0, 0)  # nous sommes alors sur le coin bas gauche
    deplacer_sans_tracer(0, -rayon)
    turtle.circle(rayon)
    # Octogone de point
    deplacer_sans_tracer(-1.25 * rayon / 2, -1.25 * rayon - 30)
    point_octogone(1.25 * rayon, 25, 'red')
    # Retour maison
    deplacer_sans_tracer(0, 0)
    turtle.exitonclick()