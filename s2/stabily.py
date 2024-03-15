''' 
SORTOWANIE STABILNE I NIESTABILNE- terminy odnoszące się do zachowania algorytmów sortowania  odniesienuy do równych elementów- czyli tych które są równe pod wzgledem wartosci klucza sortowania.
Róznica miedzy stabilnym a niestabilnym lezy w tym jak te algortymy traktują....

SORT. STABILNE
jesli zachowuje wzajemnosc kolejnosc rownych elementow wejsciowych. tzn ze jesli 2 elem. maja taka sama wartosc klucza to ich kolejnosc wzgeledm siebie pozostanie taka sama w wyniku sortowania
np. przez scalanie, wstawianie,babelkowe

SORT. NIESTABILNE
sort szybkie,przez wybor,przez kopcowanie
'''
# dodaj widok dodaj typy numery telefonu, godziny otwarcia, haslo, email,bool
# algorytmy na wtorek sortowania(wstawianie,szybkie,scalanie,bąbelkowe)
#schemat bazodanowy: temat-pytania-odpowiedzi-ktobierzeudzial-jakie ma odpowiedz-wskazalbledy-zlicz punkty-progres,historyczzne dane
#pula pytan a do testu moze byc dana ilosc

lista=[{'id':1,'value':5},
 {'id':2,'value':3},
 {'id':3,'value':5},
 {'id':4,'value':8},
 {'id':5,'value':3},]
key='value'
#zastosuj quicksort -niestabilne
def quicksort(lista,key):
    if (len(lista)<=1):
        return lista
    pivot=lista[0]
    lista_mniejszych_od_pivota=[i for i in lista[1:] if i[key]<=pivot[key]]
    lista_wiekszych_od_pivota=[i for i in lista[1:] if i[key]>pivot[key]]
    
    return quicksort(lista_mniejszych_od_pivota,'value')+ [pivot] +quicksort(lista_wiekszych_od_pivota,'value')

posortowane=quicksort(lista,'value')
for item in posortowane:
        print(item)
#sortowanie przez scalanie- stabilne
