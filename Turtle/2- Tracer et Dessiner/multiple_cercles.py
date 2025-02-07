import turtle as t
if __name__ == "__main__":
    rayon = 30
    ecart = 20
    for i in range(5):
        t.up()
        t.goto(0,-rayon)
        t.down()
        t.circle(rayon)
        t.up()
        rayon+=ecart
    t.up()
    t.home()
    t.exitonclick()
