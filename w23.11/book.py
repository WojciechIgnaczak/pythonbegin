import json

path_book= "database_book.json"

def load(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError :
        return {}

def save(path, database):
    with open(path,'w') as file:
        json.dump(database, file, indent=4)
        


def add(database,id, tytul, autor, rok):
    id= len(database)+1
    if id in database:
        raise ValueError("Książka o takim id juz istnieje")
    database[id]={"tytul": tytul,
                "autor": autor,
                'rok': rok}
    
def delete(databese,id):
    if id not in database:
        raise ValueError("Nie znaleziono ksiazki o tym ID")
    del database[id]

def edit(database,id,tytul=None,autor=None,rok=None):
    if id not in database:
        raise ValueError("Nie znaleziono ksiazki o tym ID")
    if tytul:
        database[id]['tytul']= tytul
    if autor:
        database[id]['autor']= autor    
    if rok:
        database[id]['rok']= rok

def book_list(base):
    for id, book in base.items():
        print(f"ID:{id}, tytul: {book['tytul']},Autor:{book['autor']}, Rok:{book['rok']}")
    


  
database= load(path_book)
add(database, 1, 'Python dla bystrzaków',"Nolan Illes",2012)
book_list(database)
save(path_book,database)