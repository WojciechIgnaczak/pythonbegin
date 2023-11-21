# import math #operacje matematyczne
# from math import sqrt #z math importuje tylko sqrt, innych nie
# print(math.sqrt(10))




# import random #wartosci losowe
# print(random.randint(1,100))

# #wybor losowego elementu z listy:
# fruits = ['apple','orange','banana']
# print(random.choice(fruits))

# #mieszanie listy
# numbers = [1,2,3,4,5,6,7,8]
# random.shuffle(numbers) #miesza listy randomowo
# print(numbers)

# #zwrocenie biezacego czasu w sekundach
# import time
# print(time.time())

# #zwrocenie daty
import datetime
now = datetime.datetime.now()
print(now)

#napisz program ktory sprawdza czy dany format daty jest prawidlowy
'dd-mm-yyyy'
todays_date=datetime .data.today()
print(todays_date)





# #napisz kod ktory wypisze liste plikow w biezacym katalogu
# import os
# for file in os.listdir():
#     print(file)

# file_path= "cw7.11.2023"
# if os.path.exists(file_path):
#     print("plik istnieje")


# print(os.listdir('cw7.11.2023'))
# #tworzenie nowego pliku
# with open('nowy_plik.txt', 'w')as f:
#     f.write("to jest nowy pli")
    

# #tworzenie nowego katalogu
# os.mkdir("nowy_katalog.txt") 

# #usuwanie katalogu
# os.rmdir("nowy_katalog.txt")