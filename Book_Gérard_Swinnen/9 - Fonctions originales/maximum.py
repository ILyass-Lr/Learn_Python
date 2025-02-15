# Définissez une fonction maximum(n1,n2,n3) qui renvoie le plus grand
# de 3 nombres n1, n2, n3 fournis en arguments.
def maximum(n1, n2, n3):
    return n1 if (n1 > n2) else n2 if (n2 > n3) else n3

# Programme Principal
print("Veuillez entrez trois nombres: ")
n1 = int(input())
n2 = int(input())
n3 = int(input())
print(maximum(n1, n2, n3))
