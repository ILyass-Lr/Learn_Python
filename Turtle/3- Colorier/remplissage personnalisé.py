import turtle

EPSILON = 10 ** -10


def notre_begin_fill():
    """Fonction pour commencer à remplir"""
    turtle.begin_fill()
    turtle.begin_poly()


def notre_end_fill():
    """Fonction pour finir de remplir"""
    turtle.end_poly()
    poly = turtle.get_poly()
    # On teste pour savoir si le point actuel est égal à celui de départ
    if abs(poly[0][0] - poly[-1][0]) > EPSILON or abs(poly[0][1] - poly[-1][1]) > EPSILON:
        turtle.goto(poly[0])
    turtle.end_fill()


if __name__ == "__main__":
    turtle.color("red", "green")
    notre_begin_fill()
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)
    notre_end_fill()
    turtle.exitonclick()