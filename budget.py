# Zadanie 1: Kalkulator Budżetu Domowego
# Cel: Napisz program do zarządzania budżetem domowym. Program powinien umożliwić dodawanie wydatków i przychodów, przechowywać je w pliku i generować podsumowanie budżetu.
# Funkcje:
# Dodawanie wydatku/przychodu.
# Zapisywanie danych do pliku.
# Odczytywanie danych z pliku.
# Generowanie podsumowania (np. łącznych wydatków i przychodów).
# Wyświetlanie historii transakcji.
#[[przychod,1000],[wydatek,1000]]

from datetime import datetime
import math
def read():
    budzet=[]
    try:
        with open(FILE_PATH, 'r')as file:
            for line in file:
                new= line.strip().split(';')
                budzet.append(new)
    except:FileExistsError
    return budzet

def dodaj():
    budzet=read()
    przychod_wydatek= input("wydatek czy przychod(wpisz odpowiednie slowo): ")
    data=datetime.now()
    new_date=data.strftime("%Y.%m.%d")
    if przychod_wydatek=='przychod' or przychod_wydatek=="wydatek":
        try:
            if przychod_wydatek=='przychod':
                ile=float(input("podaj ile zarobiles: "))
                nowy_przychod=['przychod',ile,new_date]
                budzet.append(nowy_przychod)
            elif przychod_wydatek=='wydatek':
                    ile=float(input("podaj ile wydales: "))
                    nowy_przychod=['wydatek',ile,new_date]
                    budzet.append(nowy_przychod)
        except:
            print("podaj liczbe!")
           
    else:
        print("podaj prawidlowa wartosc")
    return budzet  
    
def zapis():
    budzet=dodaj()
    with open(FILE_PATH,'w') as file:
        for i in budzet:
            file.write(f"{i[0]};{i[1]};{i[2]}\n")
    print("Zapisano.")
    
def historia():
    print("---HISTORIA---")
    budzet=read()
    for line in budzet:
        print(f"{line[0]}, {line[1]}zl, {line[2]}")
    print("\n")

def podsumowanie():
    budzet=read()
    przychod=0
    wydatek=0
    bilans=0

    for i in budzet:
        if i[0]=='przychod':
            przychod= przychod+ float(i[1])
        if i[0]=='wydatek':
            wydatek=wydatek + float(i[1])
            wydatek= round(wydatek,3)
    bilans= przychod - wydatek
    print("---PODSUMOWANIE---")
    print(f"Przychody: {przychod}zl\nWydatki: {wydatek}zl\nBilans: {bilans}zl")

FILE_PATH = 'budzet.txt'   

while True:
    print("\nCo robić?\n1.Zapisz nowy wydatek/przychod.\n2.Wyświetl historie.\n3.Wyświetl bilans.\n4.Wyjdź")
    what=input("Podaj odpowiednią liczbe:")
    if what == '1':
        zapis()
    elif what == '2':
        historia()
        
    elif what == '3':
        podsumowanie()

    elif what =='4':
        print("Koniec")
        break    
    else: break