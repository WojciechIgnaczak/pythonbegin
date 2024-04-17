lista=[1,32,4,2,4,2,45,5,6,45,6,57,34,6,7,7,4,5,53,34,3]
def sort_scal(lista):
    maximum=max(lista)
    ilosc=maximum+1
    tablica=[0]*ilosc
    for i in lista:
        tablica[i]+=1
    posortowana = []
    for i in range(ilosc):
        posortowana.extend([i] * tablica[i])
    return posortowana
print(sort_scal(lista))