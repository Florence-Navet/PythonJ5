li = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Programme pour récupérer la valeur maximale
max_val = li[0]
for i in range(0, len(li)):  
    if li[i] > max_val:
        max_val = li[i]

print(f"Le plus grand élément de la liste est : {max_val}")


#programme pour récupérer la valeur minnimale
min_val = li[0]
for i in range(0, len(li)):
    if li[i] < min_val:
        min_val = li[i]

print(f"Le plus petit élément de la liste est : {min_val}")


# max_val = max(L)
# min_val = min[L]