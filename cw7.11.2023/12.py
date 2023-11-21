<<<<<<< HEAD


#sprawdzamy dlugosc nip
def validate_nip(nip):
 wagi= [6,5,7,2,3,4,5,6,7]
 if len(nip)!=10: return False
#sprawdzmay czy ma same liczby
 czy_cyfra= nip.isdigit()
 if czy_cyfra== False: return False
 suma=0
 for i in range(9):
    suma+= int(nip[i])*wagi[i]
    
 if suma%11==10: return False
 if suma%11 != int(nip[9]): return False
 return True

=======


#sprawdzamy dlugosc nip
def validate_nip(nip):
 wagi= [6,5,7,2,3,4,5,6,7]
 if len(nip)!=10: return False
#sprawdzmay czy ma same liczby
 czy_cyfra= nip.isdigit()
 if czy_cyfra== False: return False
 suma=0
 for i in range(9):
    suma+= int(nip[i])*wagi[i]
    
 if suma%11==10: return False
 if suma%11 != int(nip[9]): return False
 return True

>>>>>>> d0217b5a793324b2c5a364914c7d7deadf1f3470
print(validate_nip('7742704378'))