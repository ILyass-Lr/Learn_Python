import turtle

def deplacer_sans_tracer(x, y = None):
    """Fonction pour se déplacer à un point sans tracer"""
    turtle.up()
    if (isinstance(x, tuple) or isinstance(x, list)) and len(x) == 2:
        turtle.goto(x)
    else:
        turtle.goto(x, y)
    turtle.down()

def triangle_dans_carre(long_carre):
    """Fonction pour tracer un triangle à l'intérieur du carré"""
    #On prend la position du curseur qui est sur le coin bas gauche
    pos_coin_bg = turtle.position()
    #On trace les deux traits restants, la base étant déjà faite
    turtle.goto(pos_coin_bg[0]+long_carre/2, pos_coin_bg[1]+long_carre)
    turtle.goto(pos_coin_bg[0]+long_carre, pos_coin_bg[1])

def carre_avec_triangle(longueur):
    """Fonction pour tracer un carré avec un triangle à l'intérieur"""
    for i in range(4):
        turtle.forward(longueur)
        turtle.left(90)
    triangle_dans_carre(longueur)

if __name__ == "__main__":
    #On initialise les longueurs du grand carré et des petits carrés
    longueur_1, longueur_2 = 150, 75
    #On se positionne au coin bas gauche de notre futur grand carré
    deplacer_sans_tracer(-longueur_1/2, -longueur_1/2)
    #On le dessine
    carre_avec_triangle(longueur_1)
    #On prépare les valeurs des coin bas gauche des petits carrés
    coins = [(longueur_1/2, longueur_1/2),
             (-longueur_1/2-longueur_2, longueur_1/2),
             (-longueur_1/2-longueur_2, -longueur_1/2-longueur_2),
             (longueur_1/2, -longueur_1/2-longueur_2)]
    #On dessine notre quatre petits carrés
    for coin in coins:
        deplacer_sans_tracer(coin)
        carre_avec_triangle(longueur_2)
    #On retourne au centre de notre dessin
    deplacer_sans_tracer(0, 0)
    #On prend la distance entre le centre et le coin par lequel le cercle passera
    rayon = turtle.distance(longueur_1/2+longueur_2, longueur_1/2+longueur_2)
    #On se déplace et on trace notre cercle
    deplacer_sans_tracer(0, -rayon)
    turtle.circle(rayon)
    #On retourne à la maison, et on prend un angle de 90°
    deplacer_sans_tracer(0, 0)
    turtle.left(90)
    turtle.exitonclick()
