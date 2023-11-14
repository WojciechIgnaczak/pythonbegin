#Pobierz akualna date
from datetime import datetime
from datetime import date
from datetime import timedelta
now = datetime.now()
print(now)
#tylko rok
print(now.year)
#tylko rok za pomoca dyrektyw
print(now.strftime("%Y"))

#wyswietl aktualny miesiac jako November
print(now.strftime("%B"))

#wyświtl aktualny dzien tygodnia
print(now.strftime("%A"))

#konwertuj napis "2023-11-15" na obiekt daty
data_object = datetime.strptime("2023-11-15","%Y-%m-%d")
print(data_object)

#dodaj 5dni do aktualnej daty
data_object = datetime.strptime("2023-11-15","%Y-%m-%d")
new_date= data_object + timedelta(days=5)
print(new_date)

#odejmij 2 tygodnie
new_now= now + timedelta(weeks=-2)
print(new_now)

