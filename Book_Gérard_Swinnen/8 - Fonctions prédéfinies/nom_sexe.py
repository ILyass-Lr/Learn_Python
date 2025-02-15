#Programme qui recoit le nom et le sexe d'utilisateur et affiche un message selon les données entrées

nom = input('Veuillez entrer votre nom : ')
sexe = input('Veuillez entrer votre sexe (M ou F)').upper()

if sexe == 'F':
    print(f'Chère Mademoiselle {nom}')
else:
    print(f'Cher Monsieur {nom}')
