#Programme qui détermine si une année est bissextile ou non
''' Une année est bissextile si :
    - Elle est divisible par 4 incluant par 400
    - Elle n'est pas divisible par 100
'''
#Si elle est divisible par 100 et pas 400, elle n'est pas bissextile

bissextile= False
a = int(input('Veuillez saisir une année : '))
if not(a % 4)  and ( not(a % 400) or a % 100):
    bissextile = True

print(a,"est bissextile" if bissextile else "n'est pas bissextile")
    
