#Pobierz akualna date
from datetime import datetime
from datetime import date
from datetime import timedelta
from datetime import timezone
now = datetime.now()
print(now)
#tylko rok
print(now.year)
#tylko rok za pomoca dyrektyw
print(now.strftime("%Y"))

# #wyswietl aktualny miesiac jako November
# print(now.strftime("%B"))

# #wyświtl aktualny dzien tygodnia
# print(now.strftime("%A"))

# #konwertuj napis "2023-11-15" na obiekt daty
# data_object = datetime.strptime("2023-11-14","%Y-%m-%d")
# print(data_object)

# #dodaj 5dni do aktualnej daty
# data_object = datetime.strptime("2023-11-14","%Y-%m-%d")
# new_date= data_object + timedelta(days=5)
# print(new_date)

# #odejmij 2 tygodnie
# new_now= now + timedelta(weeks=-2)
# print(new_now)

# #wyswietl roznice w dniach 1.01.2023 a dzisiaj
# past_date= datetime(2023,1,1)
# days= now - past_date
# print(days.days)



#sprawdz czy rok 2024 jest przestepny
import calendar

new_year = calendar.isleap(2024)
if new_year: print("jest rok przestępny")
else:print("nie jest to rok przestepny")

#wyswielt numer biezacego tygodnia roku
print(now.strftime("%U"))

#zmien format daty z "2023-11-15" 00:00:00 na format RFC 2822
data_object = datetime.strptime("2023-11-14","%Y-%m-%d")

rfc_date= datetime.strptime("2023-11-15 00:00:00", "%Y-%m-%d %H:%M:%S").strftime("%a,%d %b %Y %H:%M%S +0000")
print(rfc_date)

#znajdz dzien tygodnia dla 4 lipca 2023
data_now= datetime(now.year,07,04)
print(data_now.strftime("%A"))
