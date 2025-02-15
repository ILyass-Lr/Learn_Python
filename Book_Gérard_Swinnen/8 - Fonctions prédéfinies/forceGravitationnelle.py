#Programme qui affiche la valeur de la force de gravitation s'exerçant entre deux
#masses de 10 000kg

d=float(input("Veuillez entrez la distance : "))
#Calcul de la force
F = 6.67*10**(-11) * 10000**2 / d**2
print(f"d = {d} m : la force vaut {F:.3f} N")



