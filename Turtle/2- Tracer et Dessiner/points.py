import turtle
from random import randint

COULEURS = ['black', 'grey', 'brown', 'orange', 'pink', 'purple',
            'red', 'blue', 'yellow', 'green']

if __name__ == "__main__":
    turtle.setup(650, 100)
    diametre = 15
    turtle.up(); turtle.setx(-turtle.window_width()/2+2*diametre); turtle.down()
    #Pour le nombre de couleurs disponibles
    for i in range(len(COULEURS)):
        #On choisit un couleur aléatoirement
        index_choisi = randint(0, len(COULEURS)-1)
        #On imprime un point de cette couleur
        turtle.dot(diametre, COULEURS[index_choisi])
        #On supprime la couleur choisie pour éviter de la rechoisir
        del COULEURS[index_choisi]
        #On met à jour le diamètre et on se déplace pour le prochain point
        diametre += 5; turtle.up(); turtle.fd(1.5*diametre); turtle.down()
    turtle.exitonclick()
