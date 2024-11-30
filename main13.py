L = [10, 20,30, 20, 10, 50, 60, 40, 80, 50, 40]
"""

for i, x in enumerate(L):
        print("L index = ", i, " ,valeur =", x, "val = " , L[:i])
"""

print(set(L))



"""
tableau_unique = []

for num in L:
        is_unique = True
        for x in tableau_unique:
                if num == x:
                        is_unique = False
                        break
        if is_unique :
                tableau_unique.append(num)


print(f"La liste sans doublons:", tableau_unique)
"""
