#Programme qui étant donnée deux bornes entiers a et b additionne les nombres multiples de 3 et de 5
#compris entre ces nombres

#Recoit les bornes comme une tuple (a,b) et les transforme en une liste
b=list(eval(input('Veuillez les deux bornes séparés par une virgule :')))
if b[0]>b[1]:
    b[0],b[1]=b[1],b[0]

#Multiple de 3 et 5    
c = b[0] #compteur
s,output =0, ''
while c <= b[1]:
    if not(c % 3 or c % 5):
        output += str(c) + ' + '
        s +=c
    c += 1

if output:
    output = output[:-3]

#Resultat
print("\n\t__Multiple de 3 et 5__\n")
print(output,"=",s,"\n")

#Multiple de 3 ou 5 
c = b[0] #compteur
s,output =0, ''
while c <= b[1]:
    if not(c % 3 and c % 5):
        output += str(c) + ' + '
        s +=c
    c += 1

if output:
    output = output[:-3]  
#Resultat
print("\t__Multiple de 3 ou 5__\n")
print(output,"=",s)
