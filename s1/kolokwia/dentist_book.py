import os
import datetime

def validate_number(phone_number:str)-> bool:
    #sprawdza numer telefonu
    return len(phone_number) == 9 and phone_number.isdigit()

def check_file_exist(file_path):
    #sprawdza czy plik istnieje
    try:
        with open(file_path):
            return True
    except FileNotFoundError:
        return False

def get_appointment_from_file(file_path):
    #wczystuje zapisane wizyty w pliku
    if check_file_exist(file_path):
        with open(file_path,'r') as file:
            return file.readlines()
    return []

def check_availability(appointments,date):
    #sprawdza ilosc wizyt w danym dniu
    #return sum(date in appt for appt in appointments)<8
    try:
        datetime.datetime.strptime(date,'%Y-%m-%d')
    except ValueError:
        print("zla data")
        return False
    count=0
    for appt in appointments:
        if date in appt:
            count+=1
    return count<8        

def check_availability_hours(appointments:list,date,hour:int):
    working_hours= [f"{time}:00" for time in range (9,17)]
    booked_hours= [appt.split(';')[2].strip() for appt in appointments if date in appt]s
    available_hours= [hou for hou in working_hours if hou not in booked_hours]
    for godzina in available_hours:
        if  godzina == available_hours: 
            return True
  
    
def save_appointment(file_path,phonenumber,date,hour):
    #zapisuje nowa wizyte jesli numer telefonu i data sa poprawbe
    if not validate_number(phonenumber):
        print("zly numer")
        return False
    appointment= get_appointment_from_file(file_path)
    
    if check_availability_hours(appointment,date,hour)== True:
        print("godzina zajeta")
        return False
    if check_availability(appointment, date) == False:
        print("brak wolnych miejsc")
        return False
    with open(file_path,'a') as file:
        file.write(f"{phonenumber}; {date}; {hour}:00 \n")
    print ("wizyta zapisana")
    return True


def show_available_hours(appointments, date):
    if not check_availability(appointments,date):
        print("wszystkie godziny zajete")
        return 
    working_hours= [f"{hour}:00" for hour in range (9,17)]
    booked_hours= [appt.split(';')[2].strip() for appt in appointments if date in appt]
    available_hours= [hour for hour in working_hours if hour not in booked_hours]
    
    if available_hours:
        print(f"dostepne godziny, {available_hours}")
    else:
        print("brak wolnych terminów")
        
    
    
file_path = 'appointments.txt'
date= input("podaj date(yyyy-mm-dd): ")
appointments= get_appointment_from_file(file_path)
show_available_hours(appointments, date)
hour= input("podaj godzine:: ")
phone_number= input("podaj numer telefonu: ")
save_appointment(file_path, phone_number,date,hour)