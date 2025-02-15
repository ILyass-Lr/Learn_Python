#programme qui compte le nombre d'occurence de caractère 'e' dans une chaîne

ch = 'suiii'
cl = len(ch)
i = 0   #compteur traitent le caractèe courant
nc = 0  #nombre de caractères trouvé dans la chaîne
while i < cl:
    if ch[i] == 'e':
        nc += 1
    i += 1
print("Le nombre de caractèes troué dans la chaine '",ch,"'est :",nc)
    
    
