import turtle
from random import randint

LARGEUR = HAUTEUR = 400

ALIGNEMENTS = ["left", "center", "right"]
FORMATAGES = ["normal", "bold", "italic", "underline"]
FRUITS = {"Clémentine" : "orange", "Ananas" : "brown", "Pomme" : "green",
          "Poire" : "lightgreen", "Banane" : "yellow", "Orange" : "orange",
          "Cerise" : "darkred", "Abricot" : "orange", "Kiwi" : "green",
          "myrtille" : "darkblue", "prune" : "blue"}

def deplacer_sans_tracer(x, y = None):
    """Fonction pour se déplacer à un point sans tracer"""
    turtle.up()
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) == 2:
        turtle.goto(x)
    else:
        turtle.goto(x, y)
    turtle.down()

if __name__ == "__main__":
    turtle.setup(LARGEUR+50, HAUTEUR+50)
    for fruit, couleur in FRUITS.items():
        deplacer_sans_tracer(randint(-LARGEUR//2, LARGEUR//2), randint(-HAUTEUR//2, HAUTEUR//2))
        turtle.pencolor(couleur)
        turtle.write(
            fruit,
            align = ALIGNEMENTS[randint(0, len(ALIGNEMENTS)-1)],
            font = ("Arial", randint(14, 30),
            FORMATAGES[randint(0, len(FORMATAGES)-1)])
        )
    turtle.exitonclick()