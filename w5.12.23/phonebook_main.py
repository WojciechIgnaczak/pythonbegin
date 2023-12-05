
class Phonebook: #tworzenie kklasy
    filename1= b='book.txt'
    
    def __init__(self,filename='book.txt') -> None: #
        self.filename= filename
        self.phonebook= self.read_phonebook()
        
        
        
    def read_phonebook(self):
        phonebook = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone_number = line.strip().split('; ')
                    phonebook[phone_number] = name
        except FileNotFoundError:
            print("brak pliku")
        return phonebook
    
    def save_phonebook(phonebook,self):
        with open(self.filename, 'w') as file:
            for phone_number, name in phonebook.items():
                file.write(f"{name}; {phone_number}\n")
        print("Phonebook saved.")

    def display_phonebook(self):
        phonebook = self.read_phonebook(self)
        for phone_number, name in phonebook.items():
            print(f"{name}: {phone_number}")
            
    def validate_number(phone_number, self):
        return len(phone_number) == 9 and phone_number.isdigit()

    def add_entry(name, phone_number,self):
        if not self.validate_number(phone_number,self):
            print("Invalid phone number.")
            return
        phonebook = self.read_phonebook(self)
        if phone_number in phonebook:
            print("Phone number already exists.")
            return
        phonebook[phone_number] = name
        self.save_book(phonebook,self)
        print("Phone number added.")

    def remove_entry(phone_number,self):
        phonebook = self.read_phonebook(self)
        if phone_number in phonebook:
            del phonebook[phone_number]
            self.save_phonebook(phonebook,self)
            print("Phone number removed.")
        else:
            print("Phone number not found.")

    def modify_entry(old_phone_number, new_name, new_phone_number,self):
        phonebook = self.read_phonebook(self)
        if old_phone_number not in phonebook:
            print("Old phone number not found.")
            return False
        if not self.validate_number(new_phone_number,self):
            print
            
            
phonebook1= Phonebook() 
phonebook1.filename1='ksiazka.txt'
phonebook1.filename='book2.txt'
phonebook1.read_phonebook()

phonebook2= Phonebook('phone.txt')  #klasy przypisujemy do zmiennej. phone.txt nadpisuje book.txt

print(phonebook1.read_phonebook())
phonebook1.add_entry("krzysztof",'123456789','book.txt')
phonebook1.display_phonebook()