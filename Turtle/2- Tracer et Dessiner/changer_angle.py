import turtle

LARGEUR, HAUTEUR = 640, 480

if __name__ == "__main__":
    turtle.forward(LARGEUR/3)  #Avance de d'un tiers de la largeur
    turtle.left(80)  #Tourne de 80° à gauche
    turtle.up()  #Lève le curseur
    turtle.forward(HAUTEUR/4)  #Avance d'un quart de la hauteur
    turtle.down()  #Baisse le curseur
    turtle.right(180)  #Tourne à 180 à droite
    turtle.backward(HAUTEUR/4)  #Recule d'un quart de la hauteur
    turtle.pensize(3)  #Change l'épaisseur du tracé
    turtle.home()  #Retourne à la maison
    turtle.exitonclick()  #Clique gauche pour fermer 
