FILENAME= 'book.txt'

def validate_number(phone_number :str):
    return len(phone_number)==9 and phone_number.isdigit()



def read_phonebook():
    try:
         with open(FILENAME, 'r') as file:
            return [line.strip()  for line in file.readlines()]

    except FileNotFoundError:
        return []
    
def save_phonebook(phonebook):
    with open(FILENAME,"w") as file:
        #for entry in phonebook:
            file.write(f"{phonebook}\n")
    print("save file")

def display_phonebook():
    for list in read_phonebook():
        print (list)
    
    

def add_entry(name, phone_number):
    if not phone_number.isdigit() or len(phone_number) != 9: 
        print("Invalid phone number")
    
    add_new = f"{name} ; {phone_number}"
    save_phonebook(add_new)
    print("added new phone number")
    
    
def remove_entry(phone_number):
    nowa_lista=[]
    for entry in read_phonebook():
        if phone_number not in entry:
            nowa_lista.append(entry)
    save_phonebook(nowa_lista)        
 # save_phonebook([entry for entry in read_phonebook() if phone_number not in entry]) #to samo co wyzej
            


def modify_entry(old_phone_number, new_name, new_phone_number):
    if not validate_number(new_phone_number):
        print("invalid number")
        return False
    lista= read_phonebook()
    
    for key,row in enumerate(lista):
        if old_phone_number in row:
            lista[key] = f"{new_name}; {new_phone_number}"
            save_phonebook(lista)
            print("save")
            return True
    return

# read_phonebook()
# add_entry("deds", "123456789")
# display_phonebook()
# modify_entry("123456789","ania","987654321")
# remove_entry("123456789")
# display_phonebook()

while True:
    print("0. Exit")
    choice = input("Enter yout choice:")
    if choice == "0": 
        print("Exit")
        break