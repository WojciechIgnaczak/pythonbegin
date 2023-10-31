dniTygodnia= ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]
dzien = input("podaj dzien tygodnia: ").lower
if dzien in dniTygodnia:
    print("jest dzień roboczy")
else:
    print("jest weekend")