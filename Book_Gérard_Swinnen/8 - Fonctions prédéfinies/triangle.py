''' Programme qui 3 longeurs détermine ensuite s'il est un triangle
    Pour que trois longueurs puissent former un triangle, il faut que:
    - a + b > c
    - a + c > b
    - b + c > a
    Un triangle est rectangle si c^2 = a^2 + b^2 avec c étant la plus grand côté
'''

#Recevoir les longeurs
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print("Les 3 longeurs peuvent former un triangle !")
    if a==b==c:
        output="Le triangle est équilatéral"
    elif a==b or a==c or b==c:
        output="Le triangle est isocèle"
    else:
        output="Le triangle est quelconque"
    if a**2+b**2 != c**2 and a**2+c**2 != b**2 and b**2+c**2 != a**2:
        output += " et n'est pas rectangle"
    else:
        output += " et rectangle"
    print(output)
else:
    print("Ces longeurs ne peuvent pas former un triangle !")


