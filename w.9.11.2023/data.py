import datetime
now = datetime.datetime.now()
print(now)

#napisz program ktory sprawdza czy dany format daty jest prawidlowy
'dd-mm-yyyy'
todays_date = datetime .date.today()
print(todays_date)


# "1 stycznia 1970 - UTC"
print(datetime .date.fromtimestamp(100656540).year)
b= datetime.datetime(2022,12,28,23,55,59,342380).day
print(b)
a= datetime.time(11,34,56)
print(a)
print(a.minute)
now = datetime.datetime.now()
print(now.strftime("%H"))