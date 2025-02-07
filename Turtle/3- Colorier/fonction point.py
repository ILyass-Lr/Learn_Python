import turtle


def deplacer_sans_tracer(x, y=None):
    """Fonction pour se déplacer à un point sans tracer"""
    turtle.up()
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) == 2:
        turtle.goto(x)
    else:
        turtle.goto(x, y)
    turtle.down()


def point(diametre=5, couleur=None):
    """Fonction pour dessiner un point"""
    # On récupère les valeurs courantes du crayon
    etat_crayon = turtle.isdown()
    orientation = turtle.heading()
    position_crayon = turtle.position()
    couleurs_crayon = turtle.color()

    # On se prépare pour dessiner le point
    '''Si une couleur est passée alors le point sera de cette couleur,
    sinon le point aura la même couleur que la couleur de traçage. On vérifie
    alors que la couleur de remplissage est bien la même que la couleur de
    traçage'''
    if couleur != None:
        turtle.color(couleur, couleur)
    elif couleurs_crayon[0] != couleurs_crayon[1]:
        turtle.fillcolor(couleurs_crayon[0])

    deplacer_sans_tracer(position_crayon[0], position_crayon[1] - diametre // 2)
    turtle.setheading(0)

    if not etat_crayon:
        turtle.down()

    # On dessine le point
    turtle.begin_fill()
    turtle.circle(diametre // 2)
    turtle.end_fill()

    # On remet les valeurs comme au début
    deplacer_sans_tracer(position_crayon)
    turtle.setheading(orientation)

    if couleur != None:
        turtle.color(couleurs_crayon[0], couleurs_crayon[1])
    elif couleurs_crayon[0] != couleurs_crayon[1]:
        turtle.fillcolor(couleurs_crayon[1])

    if not etat_crayon:
        turtle.up()
    turtle.setheading(orientation)


# On teste notre fonction
if __name__ == "__main__":
    point(200)
    point(170, 'red')
    turtle.left(180)
    turtle.color('grey', 'white')
    point(100)
    turtle.pencolor('yellow')
    point()
    turtle.exitonclick()