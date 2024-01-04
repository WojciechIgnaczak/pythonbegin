import os
import datetime

class Dentistbook:
    def __init__(self,file_path:str):
        self.file_path =file_path
        
    def validate_number(self,phone_number:str)-> bool:
        #sprawdza numer telefonu
        return len(phone_number) == 9 and phone_number.isdigit()

    def check_file_exist(self):
        #sprawdza czy plik istnieje
        try:
            with open(self.file_path):
                return True
        except FileNotFoundError:
            return False

    def get_appointment_from_file(self,file_path):
        #wczystuje zapisane wizyty w pliku
        if self.check_file_exist(file_path):
            with open(file_path,'r') as file:
                return file.readlines()
        return []

    def check_availability(self,appointments:list,date):
        #sprawdza ilosc wizyt w danym dniu
        #return sum(date in appt for appt in appointments)<8
        count=0
        for appt in appointments:
            if date in appt:
                count+=1
        return count<8        

    def check_availability_hours(appointments,date, hour):
        working_hours= [f"{hours}:00" for hours in range (9,17)]
        booked_hours= [appt.split(';')[2].strip() for appt in appointments if date in appt]
        available_hours= [hour for hour in working_hours if hour not in booked_hours]
        if  hour in available_hours: 
            return True
        else: 
            return False
        
    def save_appointment(self,file_path,phonenumber,date,time):
        #zapisuje nowa wizyte jesli numer telefonu i data sa poprawbe
        if not self.validate_number(phonenumber):
            print("zly numer")
            return False
        appointment= self.get_appointment_from_file(file_path)
        # if check_availability_hours(appointment,date,time)== False:
        #     print("godzina zajeta")
        #     return False
        if self.check_availability(appointment, date) == False:
            print("brak wolnych miejsc")
            return False
        with open(file_path,'a') as file:
            file.write(f"{phonenumber}; {date}; {time}:00 \n")
        print ("wizyta zapisana")
        return True


    def show_available_hours(self,appointments, date):
        if not self.check_availability(appointments,date):
            print("wszystkie godziny zajete")
            return 
        working_hours= [f"{hour}:00" for hour in range (9,17)]
        booked_hours= [appt.split(';')[2].strip() for appt in appointments if date in appt]
        available_hours= [hour for hour in working_hours if hour not in booked_hours]
        
        if available_hours:
            print(f"dostepne godziny, {available_hours}")
        else:
            print("brak wolnych terminów")
            