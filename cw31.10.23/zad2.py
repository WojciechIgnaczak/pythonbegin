
liczba = int(input("podaj liczbe: "))
liczba2 = liczba %2
liczba3 = liczba %3
if liczba2 ==0 and liczba3 == 0:
    print("liczba podzielna prze 2 i 3")
elif liczba3 ==0:
    print("liczba podzielna tylko przez 3")
elif liczba2 ==0:
    print("liczba podzielna tylko przez 2")
else:
    print("liczba nie podzielna ani przez 2 ani przez 3")