import logging
logging.basicConfig(filename='car.log',level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
class Car:
    def __init__(self,make,model,year):
        self.__make=make
        self.__model=model
        self.__year=year
        self.is_production= False

    def start_production(self):
        if not self.is_production:
            logging.info(f"Rozpoczecie produkcji {self.__make} {self.__model} {self.__year}")
            self.is_production= True
        else:
            logging.warning("Aktualnie jest produkowany")

    def stop_production(self):
        if self.is_production:
            self.is_production=False
            logging.info(f"Zatrzymanie produkcji {self.__make} {self.__model} {self.__year}")
        else:
            logging.warning("Aktualnie nie jest produkowany")
    
    def display_info(self):
        logging.info(f"Marka: {self.__make}")
        logging.info(f"Model: {self.__model}") 
        logging.info(f"Rocznik: {self.__year}")
        logging.info(f"Produkcja: {"Tak" if self.is_production else "nie"}")
        return (f"Marka: {self.__make}\nModel: {self.__model}\nRocznik: {self.__year}\nProdukcja: {"Tak" if self.is_production else "nie"}")
     
class ElektricalCar(Car):#dziedziczenie klasy
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)#super kopiuje ustawienia inita z klasy car
        self.__battery_capacity= battery_capacity

    def display_info(self):
        super().display_info()
        logging.info(f"Pojemnosc baterii: {self.__battery_capacity}KWh")

def main():
    car=Car("Toyota", "Yaris",2023)
    electrical_car=ElektricalCar("Tesla","Model 3",2024,75)
    car.display_info()
    car.start_production()
    car.display_info()
    car.stop_production()
    car.display_info()

    electrical_car.display_info()
    electrical_car.start_production()
    electrical_car.display_info()
    electrical_car.stop_production()
    electrical_car.stop_production()
    electrical_car.display_info()
if __name__=="__main__":
    main()


