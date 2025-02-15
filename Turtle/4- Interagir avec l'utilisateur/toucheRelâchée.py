import turtle
def relachement_a():
    print("Touche 'a' relâchée !")

def relachement_haut():
    print("Touche 'Up' relâchée !")

if __name__ == "__main__":
    turtle.listen()
    turtle.onkeyrelease(relachement_haut, "a")  #La touche "A" est associée à relachement_haut
    turtle.onkeyrelease(relachement_a, "a")  #La touche "A" est maintenant associée à relachement_a
    turtle.onkeyrelease(relachement_haut, "Up")  #La touche "Haut" est associée à relachement_haut
    turtle.mainloop()