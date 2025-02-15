import turtle
import sys

# Les constantes
NOMBRE_ALLUMETTE = 19 # Numéro d'allumette de début
HAUTEUR_BOIS_ALLUMETTE = 50
HAUTEUR_ROUGE_ALLUMETTE = 10
COULEUR_BOIS_ALLUMETTE = "#CDA88C"
COULEUR_ROUGE_ALLUMETTE = "#DC5844"
COULEUR_FOND = "#8CCDC4"
TITRE = "Jeu des allumettes"
TAILLE_ECRITURE = 26
TAILLE_ECRITURE_2 = 16

# Les autres variables
etat_partie = True # Pour savoir si la partie continue ou non
nombre_allumettes = NOMBRE_ALLUMETTE
joueur_courant = 1


# Les fonctions
def deplacer_sans_tracer(x, y=None):
    """Fonction pour se déplacer à un point sans tracer"""
    turtle.up()
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) == 2:
        turtle.goto(x)
    else:
        turtle.goto(x, y)
    turtle.down()


def initialise_fenetre():
    """Fonction pour initialiser la fenêtre"""
    turtle.hideturtle()
    turtle.setheading(90)
    turtle.title(TITRE)
    turtle.bgcolor(COULEUR_FOND)
    turtle.speed(0)


def dessiner_allumette():
    """Fonction pour dessiner une allumette"""
    turtle.pencolor(COULEUR_BOIS_ALLUMETTE)
    turtle.fd(HAUTEUR_BOIS_ALLUMETTE)
    turtle.pencolor(COULEUR_ROUGE_ALLUMETTE)
    turtle.fd(HAUTEUR_ROUGE_ALLUMETTE)


def dessiner_allumettes(nombre_llumettes):
    """Fonction pour dessiner les allumettes"""
    # le total d'espace des allumettes correspond au moyen de la fenêtre
    espace_entre_allumettes = 60 if nombre_allumettes < 8 else turtle.window_width() / 2 // nombre_allumettes
    taille_crayon = 25 if nombre_allumettes < 8 else espace_entre_allumettes//3
    turtle.pensize(taille_crayon)
    position_allumettes = [-nombre_llumettes / 2 *espace_entre_allumettes, 0]
    for allumette in range(nombre_allumettes):
        deplacer_sans_tracer(position_allumettes)
        dessiner_allumette()
        position_allumettes[0] += espace_entre_allumettes
    if nombre_allumettes != 1:
        afficher_nombre_allumettes(nombre_allumettes)


def afficher_nombre_allumettes(nombre_allumettes, pos = (0, -80)):
    """Fonction pour afficher le nombre d'allumettes"""
    deplacer_sans_tracer(pos)
    turtle.write(f"Il y a {nombre_allumettes} allumettes.",
                align = "center",
                font=("Arial", TAILLE_ECRITURE, "normal")
    )


def bloque_clavier():
    """Fonction pour désactiver les actions des touches a, z, e"""
    turtle.onkeyrelease(None,"a")
    turtle.onkeyrelease(None, "z")
    turtle.onkeyrelease(None, "e")

def debloque_clavier():
    """Fonction pour associer les touches au nombre retiré"""
    turtle.onkeyrelease(lambda : joue(1), "a")
    turtle.onkeyrelease(lambda : joue(2), "z")
    turtle.onkeyrelease(lambda : joue(3), "e")


def joue(nombre_retire = 1):
    """Fonction pour prendre en compte le choix du joueur"""
    bloque_clavier()
    # Mise à jout de nombres d'allumettes
    global nombre_allumettes, etat_partie, joueur_courant
    if nombre_retire != 0 and nombre_allumettes - nombre_retire > 0:
        nombre_allumettes -= nombre_retire
    else:
        debloque_clavier()
        return

    if nombre_allumettes == 1:
        etat_partie = victoire(joueur_courant)
        if not etat_partie:
            quitte()
        # We réinitialise le jeu
        nombre_allumettes = NOMBRE_ALLUMETTE
        afficher_partie(joueur_courant, nombre_allumettes)
        debloque_clavier()
        turtle.listen()
    else:
        joueur_courant = 2 if joueur_courant == 1 else 1
        debloque_clavier()
        afficher_partie(joueur_courant, nombre_allumettes, nombre_retire)


def afficher_joueur(joueur_courant):
    deplacer_sans_tracer(0 , 100)
    turtle.write(f"C'est au joueur {joueur_courant} de jouer !",
                    align="center",
                    font=("Arial", TAILLE_ECRITURE, "normal"))

def afficher_partie(joueur_courant, nombre_allumettes, allumettes_retire = None):
    """Fonction pour afficher la nouvelle état de la partie"""
    turtle.clear()
    afficher_joueur(joueur_courant)
    dessiner_allumettes(nombre_allumettes)
    if allumettes_retire != None:
        afficher_allumettes_retires(allumettes_retire)

def afficher_allumettes_retires(allumettes_retire):
    "Fonction pour afficher les allumettes retirées"
    deplacer_sans_tracer(0, - 110)
    turtle.write(f"(Le joueur {1 if joueur_courant == 2 else 2} a retiré {allumettes_retire} allumette(s))",
                 align="center",
                 font=("Arial", TAILLE_ECRITURE_2, "italic"))

def victoire(joueur_courant):
    """Fonction pour le déroulement de la victoire"""
    turtle.clear()
    dessiner_allumettes(1)
    deplacer_sans_tracer(-35, -100)
    turtle.down()
    turtle.write(f"Le joueur {joueur_courant} a gagné !", align="center",
                    font=("Arial", TAILLE_ECRITURE, "normal"))
    try:
        if (turtle.textinput("Rejouer ?", "Rejouer ? Veuillez entrer 'oui' si c'est le cas.").lower() == 'oui'):
            return True
        return False
    except AttributeError or TypeError:
        quitte()


def quitte(x =0, y= 0):
    """Fonction pour quitter le programme"""
    turtle.bye()
    sys.exit(0)


def main():
    "Fonction principal"
    turtle.listen()
    initialise_fenetre()
    turtle.pencolor(COULEUR_ROUGE_ALLUMETTE)
    afficher_partie(joueur_courant, nombre_allumettes)
    debloque_clavier()
    turtle.onscreenclick(quitte, 3)


if __name__ == "__main__":
    main()
    turtle.mainloop()








