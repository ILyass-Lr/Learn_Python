#Programme qui convertit un angle donné en degrée
#minutes d'arc et secondes d'arc en radians

pi = 3.14159265359

#L'angle donnée en radians
angle = 0.5625244660546206

#1 degrée à radian
unDegrée = pi/180

###convresion en degrée notation décimale
deg = angle/unDegrée

####Mon code

###deg => secondes
##Secondes = deg * 3600
##
#####Décomposition de deg en deg° min' s
##deg, mi, s = Secondes // 3600, (Secondes % 3600)//60 , (Secondes % 3600) % 60



###Meilleur approche
deg_entier = int(deg)
minutes = (deg - deg_entier) * 60
minutes_entier = int(minutes)
secondes = (minutes - minutes_entier) * 60


print(f"{angle} radian(s) = {deg_entier}° {minutes_entier}' {secondes:.1f}''")







