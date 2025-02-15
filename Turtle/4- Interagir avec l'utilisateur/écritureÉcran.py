import turtle
turtle.write("Bonjour !", True)  #Écrit et déplace le crayon à la fin du texte
turtle.up()
turtle.goto(0, -40)
turtle.down()
turtle.write("Salut !", align = "left")  #Écrit à droite du crayon
turtle.up()
turtle.goto(0, -80)
turtle.down()
turtle.write("Coucou !", font = ("Arial", 15, "bold"))  #Écrit selon une police
turtle.exitonclick()