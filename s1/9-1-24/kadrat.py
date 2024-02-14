class Kwadrat:
    #atrybuty
    width=0
    height=0
    def __init__(self,width,height):
        self.width=width
        self.height=height
    @classmethod    #parametr, dekorator
    def pole_kwadratu(cls,atrybuty):#cls atrybuty klasowe wchodza 
        return cls(atrybuty,atrybuty)
    
    @staticmethod #statyczna metoda, ktora nie pobiera klasy, niepobiera żadnych danych z klas
    def obwod(a,b):
        return 2*a+2*b
    
    
#pole=Kwadrat(0,0)
pole=Kwadrat.pole_kwadratu(4)
print(pole.height)
print(Kwadrat.obwod(4,6))