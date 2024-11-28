li=[8,24,27,48,2,16,9,102,7,84,91]

#intialisation du produit
produit = 1

#variable pour vérifier s'il existe des valeurs dans l'intervalle
valeurs_dans_intervalle = False

#parcourir les valeurs dans la liste et multiplier les valeurs dans l'intervalle [25, 90]
for valeur in li:
    if 25 <= valeur <= 90:
        produit *= valeur
        valeurs_dans_intervalle = True

#Affichage du résultat
if valeurs_dans_intervalle: 
    print("Le produit des valeur dans l'intervalle [25, 90] :", produit)
else:
    print("Aucune valeur dans l'intervalle [25, 90].")   







 
 