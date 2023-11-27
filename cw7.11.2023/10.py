def validate_username(username):
    is_long= 3< len(username) <16
    only_word_digit = username.isalnum()
    return is_long and only_word_digit


user = input("podaj login: ")
if (validate_username(user)): 
    print("masz dobry login")
else: print("masz zly login")