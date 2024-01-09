#paradygmat programowania- szablon prawidłowego programowania. oop -objective oriented programming. klasa składa sie z obiektow
class Car:
    #atrybuty klasy (dla wszystkich funkcji):
    kolor='czerwony'
    
    def __init__(self,make,model,year):#dunder metods, konstruktor
        #atrybuty instancji
        self.make=make
        self.model=model
        self.__year=year #atrybut ukryty bo ma __
        
    def get_year(self): #metoda getter
        return self.__year
  
    def set_year(self,new_year): #metoda setter
        self.__year=new_year


#metoda=funkcja,    atrybut=zmienna
car=Car('tayota','camry',2023)
# print(car.kolor)
# car.kolor='zielony'
# print(car.kolor)
# car.uszkodzony='bezwypadkowy'   #atrybuty dynamiczne- nie zdefiniowane w klasie
# print(car.uszkodzony)
# car.__year=2020
#print(car.__year)#nie wypisuje bo jest ukryty
print(car.get_year())
car.set_year(2020)