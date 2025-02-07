import turtle
turtle.up()
turtle.goto(-150, 0)
turtle.down()
#Carré noir rempli de rouge
print(turtle.fillcolor())  #Affiche 'black'
turtle.fillcolor("red")  #Change la couleur de remplissage à rouge
turtle.begin_fill()  #Précise le début du remplissage
for i in range(4):
    turtle.forward(120)
    turtle.left(90)
turtle.end_fill()


turtle.up()
turtle.goto(40, 0)
turtle.down()
#Moitié d'octogone en vert (sauf le dernier trait) rempli de jaune
turtle.pencolor("green")  #Change la couleur de traçage à vert
turtle.fillcolor("yellow")  #Change la couleur de remplissage à jaune
turtle.begin_fill()  #Précise le début du remplissage
for i in range(4):
    turtle.forward(75)
    turtle.left(360/8)
turtle.end_fill()  #Précise la fin du remplissage

turtle.exitonclick()