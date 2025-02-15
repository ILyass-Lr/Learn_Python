#Programme qui crée uneliste contenant les éléments des deux listes en alternance

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]

i, t3 =0, []
while i < 12:
    t3.append(t2[i])
    t3.append(t1[i])
    i += 1

print(t3)


