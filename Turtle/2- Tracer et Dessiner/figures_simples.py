import turtle

turtle.up()
turtle.backward(450)
turtle.down()
#Un exemple de triangle équilatéral
longueur_cote = 200
turtle.forward(longueur_cote)  #1er côté
turtle.left(360/3)  #Angle
turtle.forward(longueur_cote)  #2ème côté
turtle.left(360/3)  #Angle
turtle.forward(longueur_cote)  #3ème côté

turtle.up()
turtle.setheading(0)
turtle.fd(300)
turtle.down()
#Un exemple de carré
for i in range(4):
    turtle.fd(longueur_cote)
    turtle.left(90)


longueur_cote = 100
turtle.up()
turtle.fd(400)
turtle.down()
#Un exemple d'octogone
for i in range(8):
    turtle.fd(longueur_cote)
    turtle.left(360/8)


turtle.exitonclick()
