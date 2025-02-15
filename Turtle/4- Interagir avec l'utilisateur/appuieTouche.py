import turtle

def appui_sur_a():
    print("Touche 'a' pressée !")

def appui_quelconque():
    print("Touche pressée !")

if __name__ == "__main__":
    turtle.listen()
    turtle.onkeypress(appui_quelconque)  #Toutes les touches libres sont associées à appui_quelconque
    turtle.onkeypress(appui_sur_a, "a")  #La touche A est désormais associée à appui_sur_a
    turtle.mainloop()