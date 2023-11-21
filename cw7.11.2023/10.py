<<<<<<< HEAD
def validate_username(username):
    is_long= 3< len(username) <16
    only_word_digit = username.isalnum()
    return is_long and only_word_digit


user = input("podaj login: ")
if (validate_username(user)): 
    print("masz dobry login")
=======
def validate_username(username):
    is_long= 3< len(username) <16
    only_word_digit = username.isalnum()
    return is_long and only_word_digit


user = input("podaj login: ")
if (validate_username(user)): 
    print("masz dobry login")
>>>>>>> d0217b5a793324b2c5a364914c7d7deadf1f3470
else: print("masz zly login")