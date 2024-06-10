# # hashowanie w python
# przekształca dane wejściowe niezależnie od ich rozmiaru w skrócony, stały ciąg znaków, znany jako wartosć hash
# wartość hash jest generowana przez funkcje hashująca- wbudowana w python
# hashy nie można odszyfrować, można je porównywać

# Właściwości:
# determinizm         -wartosc wejsciowa prowadzi do tej samej wartosci wyjsciowej
# szybkość obliczeń
# nietrwałość         -nie da sie odtworzyć oryginalnych danych
# odporność na kolizje-trudnośź w znalezieniu 2 dane prowadzą do tego samego hash
# bezpieczeństwo malych zmian - każda zmiana danych wejsciowych powinna skutkowac duza zmiana wartosci hash

# Zastosowania:
# hashowanie haseł - bezpieczenstwo danych
# weryfikacja integralności- sprawdzenie czy dane nie zostały zmienione podczas przechowywania i transmisji
# systemy baz danych- szybkie porównywanie złożonych zapytan lub dużych objętości danych bez konieczności ich pełnego przeglądania
# tablice mieszające- hashowanie jest fundamentem dla efektywnego i odnajdywania elementów w strukturach danych tj. tablice hashujące
# cache
# wykrywanie duplikatów

# realizacja hashowania w python z modułem hashlib,można wykorzystywać algorytmy SHA-1, SHA-256, MD5
import hashlib
#sha-256
text="Hello, World!"
hash_object=hashlib.sha256(text.encode())
hash_value=hash_object.hexdigest()
#print(hash_value)

#hashowanie przez wbudowana funkcje
zmienna="1"
#print(hash(zmienna))

#dynamiczne hashowanie
hash_type='sha1'
dynamic_hash=hashlib.new(hash_type)
dynamic_hash.update(b"Hello, World!")
#print(dynamic_hash.hexdigest())

# hashowanie obiektów
class Product:
    name: ''
    quantity: 0
prod1=Product()
prod2=Product()
print(hash(prod1))#hashowanie jest id obiektu, a nie wartości
print(hash(prod2))

# hashowanie plików
def hash_file(file_path):
    hash_obk=hashlib.sha256()
    with open(file_path,'rb') as file:# otwarcie w trybie binarnym
        for chunk in iter(lambda: file.read(4096),b""):
            hash_obk.update(chunk)
    return hash_obk.hexdigest()

# file_hash=hash('example.txt')
# print(file_hash)

import os
def secure_password_hash(password):
    salt=os.urandom(16)
    key=hashlib.pbkdf2_hmac('sha256',password.encode(),salt, 100000)
    return salt+key
password='bezpiecznehaslo123'
hashed_password=secure_password_hash(password)
print(hashed_password)


