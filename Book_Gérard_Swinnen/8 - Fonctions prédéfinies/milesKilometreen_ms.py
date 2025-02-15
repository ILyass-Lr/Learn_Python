#Programme qui convertisse :
# miles/heures -> m/s
#miles/heures -> km/h
#avec 1 mile = 1609 mètres


#Inciter l'utilisateur à entrer une valeur 
print("Veuillez saisir la vitesse en (miles/heures) :",end = " ")
vit = float(input())

# 1 mile en mètres
unMile = 1609

# 1 kilomètre en mètres
UnKilo = 1000

#Converssion en m/h
vitM_h = vit*unMile
#Converssion en Km/h
vitKm_h = vitM_h / 1000

print(f"Votre vitesse en Km/h est : {vitKm_h:.2f}")

#Converssion en m/s
vitM_s = vitM_h / 3600
print(f"Votre vitesse en m/s est : {vitM_s:.2f}")
