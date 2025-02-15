#Programme qui convertit en radians un angle donné en degrée
#en minutes d'arc et puis en secondes d'arc
pi = 3.14159265359
#L'angle donnée en degrée
angle,mi,s = 32,13,49
# 1 degrée à radian
unRadian = 180/pi
# 1 degrée en minutes d'arc
unMinute = 60
# 1 degrée en secondes d'arc
unSeconde = 3600

fm = s / 60             #fraction minute
fd = (fm + mi) / 60     #fraction degrée
deg = angle + fd        #degrée en notation décimale
radian = deg / unRadian

print(f"{angle}° {mi} ' {s} = {radian} radian(s)")





