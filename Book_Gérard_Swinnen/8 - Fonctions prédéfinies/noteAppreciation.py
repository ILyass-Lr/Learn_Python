#Programme qui convertit une note scolaire N quelconque,
#entrée par l'utilisateur sous forme de points (par exemple 27 sur 85), en
#une note standardisée


while True:
    n = float(input("Veuillez entrer la note obtenu : "))
    if n < 0:
        print("La note doit être positif")
    else:
        while True:
            t = int(input("Veuillez entrer sur quoi la note est obtenu : "))
            if n<=t:
                break
            else:
                print("ceci doit être plus grand que la note !!")
        break

if t*0.8 < n:
    print("A")
elif t*0.6 < n:
    print("B")
elif t*0.5 < n:
    print("C")
elif t*0.4 < n:
    print("D")
else:
    print("E")



