#walidacja maila

# dlugosc 6-30
# czy jest @
# jaki jest username username@pw.edu.pl
# jaka domene
#walidacja pustych znaków


def validate_email (mail):
    if mail.count('@') != 1 : raise ValueError("to nie jest adress mailowy") #sprawdza czy jest malpa lub wiecej niz 1
    atrybut= mail.split('@')
    username= atrybut[0]
    domena= atrybut[1]
    

mail= "usernamewpw.edu.pl"
try:
    validate_email(mail)
except ValueError as e:
    print(f"Komunikat bledu: {e}")