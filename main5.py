#Crée une liste avec au moins cinq entiers
L = [5, 9, 8, 15, 38]
print(f"La deuxième valeur de la liste est : {L[1]}")


#   Afficher une liste d'entier
def liste_entier():
    return L
def replace_sum(L):
    L[3] = L[2] + L[4]
    print(f"Liste après modification: {L}")
    

#Appeler la fonction
replace_sum(L)

#afficher la dernière valeur du tableau
print(f"La dernière valeur du tableau : {L[-1]}")

     

