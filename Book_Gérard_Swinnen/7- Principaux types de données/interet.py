#programme qui calcule les intérêts accumulés chaque année pendant 20 ans,
#par capitalisation d'une somme de 100€ placée en banque au taux fixe de 4,3%

interet,annee = 0,1
capital = 100
interet_total = 0
while annee<=20:
    interet = capital * 4.3/100
    capital += interet
    interet_total += interet
    print(f"annee {annee:2}  {capital:.2f}€")
    annee+=1
print(f"Votre intérêt total accumulé après 20 ans : {interet_total:.2f}€")
