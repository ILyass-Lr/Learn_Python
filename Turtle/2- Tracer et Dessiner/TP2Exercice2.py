import turtle

LARGEUR, HAUTEUR = 640, 480

if __name__ == "__main__":
    turtle.setup(LARGEUR, HAUTEUR)
    turtle.speed("fast")  # Met la vitesse de traçage à rapide
    ecart = 4
    for i in range(30):
        turtle.stamp()
        turtle.left(30)
        turtle.up();
        turtle.forward(ecart);
        turtle.down()
        ecart += 3
    turtle.exitonclick()