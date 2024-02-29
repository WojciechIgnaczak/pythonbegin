#sito euklidesa

liczby=[]
zakres=200
for i in range(2,zakres+1):
    liczby.append(i)
n=zakres//2 #ilosc przejsc petli

start=1
while start<n:
    start=start+1 
    for liczba in liczby[start:]:
        if liczba%start==0:
            liczby.remove(liczba)
print(liczby)