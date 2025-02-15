from math import sqrt
#Programme qui calcule le périmètre et l'aire d'un triangle


#Recevoir la longeur des trois côtés
print("\t#__Calcule de périmètre d'un triangle#__\n")
print("Veuillez entrer les longeurs de 3 côtés du triangle : ")
a = float(input(">"))
b = float(input(">"))
c = float(input(">"))
print(f"le périmètre de votre triangle est : {a+b+c:.2f}\n")

print("\t#__Calcule de l'aire d'un triangle#__\n")
#Demi-périmètre
d = a+b+c / 2
#Formule utilisé S =√d(d-a)(d-b)(d-c)
S = sqrt(d*(d-a)*(d-b)*(d-c))

print(f"l'aire de votre triangle est : {S:.2f}")
