import time
import random
lista=[2,3,4,6,7,8,9,1,2,3,2,3,2,3,5,6,7,8,6,8]
def median(lista):
    newlist=[lista[0], lista[len(lista)//2],lista[-1]]
    return sorted(newlist)[1]

#lista=[1,2,3,4,5,6,7]
def quicksort(lista):
    if (len(lista)<=1):
        return lista
    pivot=random.choice(lista)
    pivot=median(lista)
    lista_mniejszych_od_pivota=[i for i in lista[1:] if i<pivot]
    lista_wiekszych_od_pivota=[i for i in lista[1:] if i>=pivot]
    return quicksort(lista_mniejszych_od_pivota)+ [pivot] +quicksort(lista_wiekszych_od_pivota)

print(quicksort(lista))
ile_liczb=100
lista=[random.randint(1,100) for i in range(ile_liczb)]
start_time=time.time()
print(quicksort(lista))
end_time=time.time()
czas=end_time-start_time
print(f"Czas sortowania dla {ile_liczb} liczb wynosi: {round(czas,6)}")