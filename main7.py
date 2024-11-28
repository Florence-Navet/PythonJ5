L =[8,24,48,2,16]

def multiple_trois(L):
    i = 0
    for num in L:
        if num % 3 == 0:
            i += 1
    return i

#appeler la fonction
result = multiple_trois(L)
print(f"Nombre de multiple de trois dans la liste : {result}")

