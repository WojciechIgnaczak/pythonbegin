#podziel tablice na 2 do momentu az wszystkie beda mialy po 2 elementy.
#posortuj wszystkie tablice 2 elementowe
#scalaj posortowane tablice
import random
import time
def dziel(lista)->list: #dzielenie listy na 2 elementowe rekurencyjnie
    if len(lista)>2:
        n=len(lista)//2
        right_site=lista[:n]
        left_site=lista[n:]
        return scal(dziel(right_site),dziel(left_site))
    if len(lista)==2:
        if lista[0]>lista[1]:
            lista[0],lista[1]=lista[1],lista[0]
    return lista


def scal(half1,half2):# scalanie 2 list
    newlist=[]
    n=len(half1)+len(half2)
    for i in range(n):
        if half1[0]<half2[0]:
            newlist.append(half1[0])
            half1.pop(0)
        else:
            newlist.append(half2[0])
            half2.pop(0)
        if len(half1)==0:
            for i in range(len(half2)):
                newlist.append(half2[i])
            break
        if len(half2)==0:
            for i in range(len(half1)):
                newlist.append(half1[i])
            break
    return newlist


lista=[38, 27, 43, 3, 9, 82, 10,1,3,67,2,5,2,5,6,2,1,7,2,45,24,43,5,23,2,53,42,54]
x=dziel(lista)
print(x)


# ile_liczb=10000
# lista=[random.randint(1,100) for i in range(ile_liczb)]
# start_time=time.time()
# dziel(lista)
# end_time=time.time()
# czas=end_time-start_time
# print(f"Czas sortowania dla {ile_liczb} liczb wynosi: {round(czas,6)}")