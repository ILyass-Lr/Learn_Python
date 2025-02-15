from dessins_tortue import *
setup(900, 480)
speed(0)
taille,espacement = 30, -400
up()
goto(espacement, 20)
down()
for i in range(5):
    espacement += taille
    carre(taille, 45)
    up()
    goto(espacement + 25, 20)
    espacement += taille
    down()
    triangle(taille, "blue", 25)
    up()
    goto(espacement + 35, 30)
    down()
    espacement += 60
    taille += 10

taille,espacement = 20, -400
up()
goto(espacement, -100)
down()
setheading(0)
for i in range(9):
    espacement += taille
    if i < 5:
        taille += 10
        etoile6(taille)
    else:
        taille -= 10
        etoile6(taille)
    up()
    goto(espacement + 60, -100)
    down()
    espacement += 60

help(etoile5)
    
