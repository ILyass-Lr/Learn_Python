#programme qui recopie une chaîne dans une nouvelle variable
#en insérant des astériques entre les caractères
#Exemple : gaston => g*a*s*t*o*n

ch = 'ILyass'
lc = len(ch) #longuer de la chaîne
i = 0        #compteur parcourant la chaîne
output = ''  #la chaîne résultant
while i < (lc - 1):
    output += ch[i] + '*'
    i += 1
output += ch[lc-1]
print("la chaîne avant :",ch)
print("la chaîne après :",output)
    
    
    
