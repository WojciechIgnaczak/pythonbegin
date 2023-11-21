def suma_cyfr(cyfry):
    suma= 0
    for cyfra in cyfry:
        suma =suma+int(cyfra)
    return suma

    
    
#suma cyfr liczby całkowitej
liczba= input("Podaj liczbe: ")
suma_cyfr_liczby= suma_cyfr(liczba)
print(f"Suma cyfr podanej liczby ={suma_cyfr_liczby}")