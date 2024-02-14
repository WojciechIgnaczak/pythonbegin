#walidacja maila

# dlugosc 6-30
# czy jest @
# jaki jest username username@pw.edu.pl
# jaka domene
#walidacja pustych znaków


def validate_email (mail):
    if mail.count('@') != 1 : raise ValueError("to nie jest adress mailowy") #sprawdza czy jest malpa lub wiecej niz 1
    
    param= mail.split('@')
    username= param[0]
    domena= param[1]
    if domena == "pw.edu.pl":
        True
    else: raise ValueError("to nie jest adress mailowy z domenu pw.edu.pl")
    return True 
        

mail= "usernamew@pw.edu.pl"
try:
    validate_email(mail)
except ValueError as e:
    print(f"Komunikat bledu: {e}")