path= "kontakt.txt"
phonebook= {}
            
def czy_prawdziwy_istnieje(phone_number :str):
    if len(phone_number) != 9: return False
    for keys in phonebook.keys():
        if phonebook[phone_number] == phonebook.values(): return False
        else: return True
    return True

def read_phone(path):
    with open(path,'r') as file:
         file.readline()
        
def save_phonebook(phonebook):
    with open(path, 'r') as file:
        file.close()
        
def display_phonebook(path):
    with open(path, 'r') as file:
        file.readline()
        
def add_entry(name:str, phone_number:str):
    if czy_prawdziwy_istnieje(phone_number) == True:
        with open(path, 'a') as file:
            dict= {name  : phone_number}
            phonebook.update(dict)
            file.write(f"{phonebook}\n")
    else: print('zly numer')
    
def remove_entry(phone_number:str):
    usun= phonebook[phone_number]
    del usun

def modify_entry(old_phone_number:str, new_name:str, new_phone_number:str):
    with open(path, 'a') as file:
        phonebook[old_phone_number]= new_name
        old_phone_number= new_phone_number
add_entry('name','123456789')
save_phonebook('book.txt')