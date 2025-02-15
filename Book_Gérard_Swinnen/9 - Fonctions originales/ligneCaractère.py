# Définissez une fonction ligneCar(n, ca) qui renvoie une chaîne de n caractères ca.
def ligneCar(n, ca):
    "renvoie une chaîne de n caractères ca"
    if isinstance(ca, str):
        s = ca*n
    else:
        print("Veuillez entrez de(s) caractère(s)!")
    return s

## Programme Principal
ca = input("Veuillez entrez de(s) caractère(s) :")
n = int(input("Veuillez entrez le nombre d'occurence: "))
print(ligneCar(n, ca))

            
