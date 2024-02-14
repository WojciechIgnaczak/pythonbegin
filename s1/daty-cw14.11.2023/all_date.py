import datetime
import sys


        #FORMATOWANIE DATY
now = datetime.datetime.now()
#wyswietlanie dzisiejszej daty i godziny
print(f"Dzisiejsza data: {now}")

#wyswietl tylko rok
now_year= now.strftime("%Y")
print(f"dzisiejszy rok: {now_year}")

#wyswietlanie daty w formacie yyyy-mm-dd
data= now.strftime("%Y"'-' "%m"'-' "%d")
print(f"Dzisiejsza data inny format bez godziny {data} ")

#wyswietl tylko miesiąc pełna nazwa
now_month= now.strftime("%B")
print(f"Miesiac pelna nazwa po ang: {now_month}")

#miesiąc skrót nazwy
now_month= now.strftime("%b")
print(f"Miesiac skrócona nazwa po ang: {now_month}")

#miesiąc cyfra
now_month=now.strftime("%m")
print(f"Miesiac cyfra {now_month}")

#miesiąc po polsku
miesiac= {1:"Styczeń",2:"Luty",3:"Marzec",4:"Kwiecień",5:"Maj",6:"Czerwiec",7:"Lipiec",8:"Sierpień",9:"Wrzesień",10:"Październik",11:"Listopad",12:"Grudzień"}
now_month= int(now.strftime("%m"))
month= miesiac[now_month]
print(f"Miesiac po polsku: {month}")

#wyswietl dzien tygodnia
day= now.strftime("%A")
print(f"dzien tygodnia: {day}")






#dodanie n dni, m tygodni do aktualnej daty
add= datetime.datetime.now()
new= add + datetime.timedelta(days=5, weeks=-2)
add= new.strftime("%Y"'-'"%m"'-'"%d")
print(f"dodane n dni i m tygodni do daty {add}")

#podanie przez uzytkownika daty w formacie dd.mm.yyyy i zamiana na date w formacie yyyy-mm-dd
try:
    today= input("podaj date w formacie dd.mm.yyyy : ")
    today_date = datetime.datetime.strptime(today, '%d'"."'%m'"."'%Y')
    today_new_date= today_date.strftime("%Y""-""%m""-""%d")
    print(f"zmieniony format daty podanej przez uzytkownika: {today_new_date}")

   
except ValueError: 
    print("Podaj prawidlowy format daty")
    sys.exit()




        #RÓŻNICE MIEDZY DATAMI
#roznica w latach miedzy podaną data a dzisiejszą
now= datetime.datetime.now()
now_year= now.year
today_date_year=today_date.year
roznica= now_year - today_date_year
print(f"Róznica w latach od podanej daty wynosi: {roznica} lat")
    #roznica w dniach
now= datetime.datetime.now()
roznica= now - today_date
print(f"Róznica w dniach od podanej daty wynosi: {roznica.days} dni")
    #róznica w tygodniach
now= datetime.datetime.now()
roznica= now - today_date
roznica_weeks= roznica.days/7
print(f"Róznica w tygodniach od podanej daty wynosi: {int(roznica_weeks)} tygodni")
    #róznica w godzianch
now= datetime.datetime.now()
roznica= now - today_date
roznica_hours= roznica.days*24
print(f"Róznica w godzinach od podanej daty wynosi: {roznica_hours} godzin")
    #róznica w minutach
now= datetime.datetime.now()
roznica= now - today_date
roznica_min= roznica.days*24*60
print(f"Róznica w minutach od podanej daty wynosi: {roznica_min} minut")
    #róznica w sekundach
now= datetime.datetime.now()
roznica= now - today_date
roznica_sec= roznica.days*24*60*60
print(f"Róznica w sekundach od podanej daty wynosi: {roznica_sec} sekund")