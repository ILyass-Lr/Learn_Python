import turtle
import time
id_tampons = []
turtle.up()
turtle.bk(turtle.window_width()/2)
turtle.setup(height= 100)


def reset():
    turtle.reset()
    turtle.up()
    turtle.goto(0-turtle.window_width()/2, 0)


def stamps():
    for i in range(95):
        turtle.stamp()  # Tamponne et on enregistre l'identifiant
        turtle.fd(10)

# Ajout de tamponne successives
stamps()
time.sleep(5)

# Supprime le 15ème tampon
reset()
for i in range(95):
    id_tampons.append(turtle.stamp())  # Tamponne et on enregistre l'identifiant
    turtle.fd(10)
turtle.clearstamp(id_tampons[14])
time.sleep(5)

# Supprime les 9 premiers tampons
reset()
stamps()
turtle.clearstamps(9)
time.sleep(5)

# Supprime les 10 derniers tampons
reset()
stamps()
turtle.clearstamps(-10)
time.sleep(5)

# Supprime tous les tampons restants
reset()
stamps()
turtle.clearstamps()
turtle.home()

turtle.exitonclick()