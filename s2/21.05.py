import os
import hashlib
password=input("Podaj hasło: ")
algorytm=input("Podaj algorytm hashowania: ")

salt=os.urandom(16)

def secure_password_hash(password,algorytm):
    key=hashlib.pbkdf2_hmac(algorytm,password.encode(),salt, 100000)
    return salt+key

hashed_password=secure_password_hash(password,'md5')
print(f"Twoje zahashowane hasło: {hashed_password}")

hashed_password=secure_password_hash(password,'md5')
print(f"Twoje zahashowane hasło: {hashed_password}")