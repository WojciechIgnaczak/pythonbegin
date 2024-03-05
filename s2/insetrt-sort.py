#sortowanie przez wstawianie
import time
import random

#lista=[2,5,5,3,5,1,89,3,5,2]

def insert_sort(lista):
    number=len(lista)
    for i in range(1,number):
        temp=lista[i]
        t=i-1
        while t>=0 and lista[t]>temp:
            lista[t+1]=lista[t]
            t-=1
            lista[t+1]=temp
    return lista
ile_liczb=10000
lista=[random.randint(1,100) for i in range(ile_liczb)]
start_time=time.time()
insert_sort(lista)
end_time=time.time()
czas=end_time-start_time
print(f"Czas sortowania dla {ile_liczb} liczb wynosi: {round(czas,6)}")