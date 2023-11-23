#Pobierz aktualna date i czas
import datetime
from datetime import timedelta
now= datetime.datetime.now()
import locale
locale.setlocale(locale.LC_ALL, 'pl_PL')
print(now)

#wyswietl aktualny rok
rok= now.year
print(rok)

#aktualny miesiąc i jego nazwe

month= now.strftime("%B")
print(month)

#dodaj 5 dni do aktualnej daty
new_date= now + timedelta(days=5)
print(new_date)

# odejmij 2 tygodnie od dzisiejszej daty
new_date= now + timedelta(weeks=-2)
print(new_date)

#oblicz wiek osoby urodzonej w dniu "1990-05-28"
past= datetime.datetime(1990,5,28).year
old= now.year - past
print(old)

#czyta plik tekstoowy i wyswietli jego zawartosc
filepath = "plik.txt"
f = open(filepath, "r", encoding="utf-8")
print(f.read())