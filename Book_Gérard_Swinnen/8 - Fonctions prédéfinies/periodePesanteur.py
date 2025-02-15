from math import sqrt,pi
#Programme qui calcule la période d'un pendule simple de longueur donnée

#Valeur dee l'accéleration de pesanteur
g = 9.80665 
#Recevoir la longeur de pesanteur
l=float(input("Veuillez entrer la longeur de pesanteur : "))

#Calcule de période
T=2*pi*sqrt(l/g)

print(f"La période prise par le pesanteur de longeur {l:.2f}m est {T:.2f}s")
