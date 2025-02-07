import turtle as t
# Constantes
LARGEUR, HAUTEUR = 1024, 768
POS_X = POS_Y = 50


def recapitulatif():
    """Fonction récapitulant les informations concernant
       notre fenêtre et son contenu"""
    print(f"la largeur est : {t.window_width()} px")
    print(f"la longeur est : {t.window_height()} px")
    print(f"le couleur du fond est : {t.bgcolor()}")
    print(f"l'image est : {t.bgpic()}")


t.setup(LARGEUR,HAUTEUR,POS_X,POS_Y)
t.bgcolor("yellow")
t.bgpic("../images/orange.png",)
recapitulatif()
t.exitonclick()

