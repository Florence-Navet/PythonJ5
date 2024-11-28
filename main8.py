L = [8, 24,27,48,2,16,9,7,84,91]

#programme calculant la somme du tableau
def som_val_tab(L):
    total = 0
    for num in L:
        if num % 2 == 0:
            total += num
    return total

#appeler la fct et afficher le résultat
resultat = som_val_tab(L)
print(f"La somme de toutes les valeurs paires du tableau est : {resultat}")