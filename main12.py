#creation d'une liste vide
L = []

# Remplir la liste avec des mots
for i in range(5):
    mot = input(f"Entrez un mot ({i+1}/5) : ")
    L.append(mot)

# Affichage de la liste avant le tri
print(f"Liste avant le tri : {L}")

# Tri alphabétique
L.sort()

# Affichage de la liste après le tri
print(f"Liste après le tri alphabétique : {L}")
