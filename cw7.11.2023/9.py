<<<<<<< HEAD
#8znaków, 1 cyfra, 1 duza litera
def validate_password(password):
    is_long = len(password)>=8
    mam_cyfre = any(char.isdigit() for char in password)
    mam_wielk_litera = any(char.isupper() for char in password)
    return mam_cyfre and mam_wielk_litera and is_long

haslo = input("podaj swoje haslo")
if validate_password(haslo):
    print("mama silne haslo")
=======
#8znaków, 1 cyfra, 1 duza litera
def validate_password(password):
    is_long = len(password)>=8
    mam_cyfre = any(char.isdigit() for char in password)
    mam_wielk_litera = any(char.isupper() for char in password)
    return mam_cyfre and mam_wielk_litera and is_long

haslo = input("podaj swoje haslo")
if validate_password(haslo):
    print("mama silne haslo")
>>>>>>> d0217b5a793324b2c5a364914c7d7deadf1f3470
else: print("masz za slabe haslo")