import turtle


def toto(x, y):
    print(f"toto : {x}, {y}")


def tutu(x, y):
    print(f"tutu : {x}, {y}")


def tata(x, y):
    print(f"tata : {x}, {y}")


def titi(x, y):
    print(f"titi : {x}, {y}")


def tete(x, y):
    print(f"tete : {x}, {y}")


if __name__ == "__main__":
    # Pas besoin de turtle.listen() vu que l'on ne s'occupe pas du clavier

    # Clique gauche : juste toto au final
    turtle.onscreenclick(titi, 1)
    turtle.onscreenclick(toto, 1)  # <=>  turtle.onscreenclick(toto, 1, False)

    # Clique central : juste tata
    turtle.onscreenclick(tata, 2)

    # Clique droit : tete et tutu
    turtle.onscreenclick(tete, 3)
    turtle.onscreenclick(tutu, 3, True)

    turtle.mainloop()