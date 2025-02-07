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


if __name__ == "__main__":
    turtle.bgcolor("orange")
    # Le triangle
    deplacer_sans_tracer(-210, -210)
    turtle.color("white", "pink")  # pencolor("white"); fillcolor("pink")
    turtle.begin_fill()
    turtle.goto(210, -210)
    turtle.goto(0, 240)
    turtle.goto(-210, -210)
    turtle.end_fill()
    # Le cercle
    deplacer_sans_tracer(0, 0)
    rayon = turtle.distance(135, 135)
    deplacer_sans_tracer(0, -rayon)
    turtle.fillcolor("purple")
    turtle.begin_fill()
    turtle.circle(rayon)
    turtle.end_fill()
    # Les carrés
    carres = [("green", 270), ("yellow", 180), ("grey", 90)]
    for var_carre in carres:
        deplacer_sans_tracer(-var_carre[1] / 2, -var_carre[1] / 2)
        turtle.color("black", var_carre[0])  # pencolor("black"); fillcolor(var_carre[0])
        turtle.begin_fill()
        carre(var_carre[1])
        turtle.end_fill()
    deplacer_sans_tracer(0, 0)
    turtle.exitonclick()