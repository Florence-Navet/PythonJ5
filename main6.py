def change_place(L):

#verfier que la liste n est pas vide
    if len(L) > 0:

#inversion posiions 1er et derniere position    
        L[0], L[-1] = L[-1], L[0]
    return L

#Cree une liste de cinq entiers
L = [1, 2, 3, 4, 5]

print(f"La liste dans l'ordre est : {L}")

# print("La liste avant échange est : ", L )   

#appel de la fonction
L = change_place(L)

print("Liste après échange :", L ) 