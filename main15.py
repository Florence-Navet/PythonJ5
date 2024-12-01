li = [22.4, 4.0, 16.22,9.10, 11.71, 12.22, 14.20, 5.20, 17.50]


li = [int(x) for x in li]

print("Ma liste arrondie originale est :" ,li)

def tri_croissant(li):
        n= len(li)
        for i in range(n):
                min_index = i
                for j in range(i+1, n):
                        if li[j] < li[min_index]:
                                min_index = j
                li[i], li[min_index] = li[min_index],li[i]
        return li

resultat = tri_croissant(li)
print("La liste arrondie dans l'ordre est : ", resultat)

