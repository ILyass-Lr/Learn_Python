import turtle

LARGEUR, LONGUEUR = turtle.window_width(), turtle.window_height()
def deplacer_sans_tracer(x, y=None):
    """Fonction pour se déplacer à un point sans tracer"""
    turtle.up()
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) == 2:
        turtle.goto(x)
    else:
        turtle.goto(x, y)
    turtle.down()


def affiche_point(diametre, couleur):
    """Fonction pour afficher seulement la balle"""
    deplacer_sans_tracer(pos_x, pos_y)
    turtle.clear()
    turtle.dot(diametre, couleur)


def reinit_pos():
    """Fonction pour réinitialiser la position de la balle"""
    global pos_x, pos_y
    pos_x = pos_y = 0
    affiche_point(diametre_balle, couleur_balle)


def deplace_x(num=0):
    """Fonction pour changer la coordonnée x de la balle"""
    global pos_x
    pos_x += num
    if pos_x < LARGEUR/2 and pos_x > -LARGEUR/2:
        affiche_point(diametre_balle, couleur_balle)
    else:
        pos_x -= num


def deplace_y(num=0):
    """Fonction pour changer la coordonnée y de la balle"""
    global pos_y
    pos_y += num
    if pos_y < LONGUEUR/2 and pos_y > -LONGUEUR/2:
        affiche_point(diametre_balle, couleur_balle)
    else:
        pos_y -= num


if __name__ == "__main__":
    turtle.speed(0)
    pos_x, pos_y = 0, 0
    diametre_balle, couleur_balle = 20, 'red'

    turtle.hideturtle()

    
    while True:
        try:
            diametre_balle = int(turtle.numinput("Diamètre", "Veuillez entrez le diamètre de la balle", 20))
            break
        except TypeError:
            pass
    while True:
        try:
            couleur_balle = turtle.textinput("Couleur", "Veuillez entrez la couleur de la balle")
            if couleur_balle.isalpha():
                break
        except TypeError:
            pass
    affiche_point(diametre_balle, couleur_balle)

    turtle.listen()  # Pour écouter
    turtle.onkeypress(lambda: deplace_x(-10), "Left")  # Touche gauche
    turtle.onkeypress(lambda: deplace_x(10), "Right")  # Touche droite
    turtle.onkeypress(lambda: deplace_y(10), "Up")  # Touche haut
    turtle.onkeypress(lambda: deplace_y(-10), "Down")  # Touche bas
    turtle.onkeyrelease(reinit_pos, "space")  # Touche espace
    turtle.mainloop()  # Pour démarrer la boucle d'événements