#     #1. SUMA CYFR LICZBY CAŁKOWITEJ
# def suma_cyfr(cyfry: str) ->int:
#     suma= 0
#     for cyfra in cyfry:
#         suma =suma+int(cyfra)
#     return suma
# try:
#     liczba= input("Podaj liczbe: ")
#     if liczba.isdigit():
#         suma_cyfr_liczby= suma_cyfr(liczba)
#         print(f"Suma cyfr podanej liczby ={suma_cyfr_liczby}")
#     else: print("Enter only digit!")
# except ValueError:
#     print(f"Invalid input")




        #2. BMI
def bmi(weight :float, height :float)-> float:
        calculate= weight/(height**2)
        return calculate
    
    
def what_bmi(bmi_calc :float)-> float:
    print(f"Your BMI ={round(bmi_calc,2)}")
    if bmi_calc < 18.5: print("You are underweight.")
    elif bmi_calc< 24.9: print("You are normal weight.")
    elif bmi_calc <29.9: print("You are overweight.")
    else: print("You are obese.")
    
    
def check_float(number)-> bool:
    try:
        float(number)
        return True
    except ValueError:
        return False    
    
    
try:  
    weight= float(input("Enter your weight in kilograms: "))
    height= float(input("Enter your height in meters: "))
    if check_float(weight) and check_float(height):
        bmi_calc= bmi(weight, height)
        what_bmi(bmi_calc)
    else: print("Enter only digit")
except ValueError:
    print("Invalid input")