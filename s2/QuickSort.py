
lista=[1,2,3,4,5,6,7,21,2,353,52,13,5,2,5,0,53,32]
def quicksort(lista):
    if (len(lista)<=1):
        return lista
    pivot= lista[0]
    lista_mniejszych_od_pivota=[i for i in lista[1:] if i<pivot]
    lista_wiekszych_od_pivota=[i for i in lista[1:] if i>=pivot]
    return quicksort(lista_mniejszych_od_pivota)+ [pivot] +quicksort(lista_wiekszych_od_pivota)

print(quicksort(lista))

