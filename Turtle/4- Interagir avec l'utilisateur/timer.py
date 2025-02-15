import turtle


def ecrit_temps():
    """Fonction pour écrire le temps écoulé"""
    turtle.clear()
    turtle.write(f'''Le programme tourne depuis 
                 {heure} h {minute} min et {seconde} s''',
                 align="center",
                 font=("Arial", 16, "bold"))


def incremente_temps():
    """Fonction pour incrémenter le temps"""
    global heure, minute, seconde
    seconde += 1
    if seconde == 60:
        minute += 1
        seconde = 0
    if minute == 60:
        heure += 1
        minute = 0
    ecrit_temps()
    turtle.ontimer(incremente_temps, 1000)  # Fait appel à elle-même toutes les secondes


if __name__ == "__main__":
    turtle.speed(0)
    turtle.hideturtle()
    heure = minute = seconde = 0
    ecrit_temps()
    turtle.ontimer(incremente_temps, 1000)  # Attend une seconde puis commence à incrémenter
    turtle.exitonclick()