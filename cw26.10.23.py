#PODAJ LICZBE I SPRAWDŹ CZY WIEKSZA OD 10

liczba = int(input("podaj liczbe: "))
if (liczba >10):
    print("liczba wieksza od 10")
else: print("liczba mniejsza lub równa 10")




#PODAJ WIEK, SPRAWDŹ CZY DZIECKO, MŁODZIEŻ, DOROSŁY

wiek= int(input("podaj swoj wiek: "))

if (wiek <10): print("jestes dziecko")
elif (wiek <18): print("jestes młodzież")
else: print("jestes dorosły")




#SPRAWDZENIE WARUNKU TRUE/FALSE

warunek = False

if warunek : print("warunek prawdziwy")
else: print("warunek fałszywy")







#LICZBA PARZYSTA

liczba= int(input("podaj liczbe: "))
parzysta= liczba % 2

if parzysta == 0: print("liczba parzysta")
else: print("nieparzysta")





#AND, SPRAWDZNEIE 2 WARUNKÓW

wiek= int(input("podaj wiek: "))
prawo_jazdy= int(input("czy masz prawo jazdy, wpisz 1 jak tak,0 jak nie masz: "))

if wiek>=18 and prawo_jazdy ==1: print("jestes pełnoletni i masz prawo jazdy")
else: print("nie jestes pełnoletni lub nie masz prawa jazdy")


