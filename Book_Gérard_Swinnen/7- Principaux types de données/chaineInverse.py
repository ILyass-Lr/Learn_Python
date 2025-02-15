#programme qui recopie une chaîne dans une nouvelle variable
#en l'inversant

ch = 'ILyass'
lc = len(ch) #longuer de la chaîne
i = lc - 1   #compteur parcourant la chaîne
output = ''  #la chaîne résulatnt
while i>=0:
    output += ch[i]
    i -= 1
print("La chaîne avant :",ch)
print("La chaîne après :",output)
