import turtle

while True:
    try :
        nom = turtle.textinput("Nom", "Veuillez saisir votre nom s'il vous plaît")
        if nom.isalpha() and len(nom) < 21:
            break
    except TypeError:
        pass
print(nom)