#programme qui vérifie c'est une chaîne est une palindrome

ch = 'LIL'
lc = len(ch) #longuer de la chaîne
i = 0        #compteur parcourant la chaîne


while i<len(ch)/2:
    if ch[i] != ch[len(ch)-1-i]:
        print(f"'{ch}' n'est pas un palindrome !")
        break
    i += 1
else:
    print(f"'{ch}' est un palindrome !")
    
