# W1.Definicja algorytmu. Algorytm Euklidesa. Znajdowanie dzielników i sprawdzanie pierwszości liczby. Sito Eratostenesa. Złożoność obliczeniowa.
Algorytm to skończony zestaw kroków, który przekształca dane wejściowe w oczekiwane dane wyjściowe. Algorytmy są podstawowym narzędziem w informatyce do rozwiązywania problemów.Algorytm to skończony zestaw instrukcji.
Złożoność obliczeniowa O(n) to oznaczenie notacji dużego O, które opisuje górną granicę wzrostu zasobów (np. czasu lub pamięci), które są potrzebne do wykonania algorytmu w zależności od rozmiaru danych wejściowych (oznaczanego przez n).
## Euklides NWD:
```
def nwd2(a,b):
    while b:
        a,b=b,a%b
    return print(a)
nwd2(48,12)
```

## Dzielniki liczb:
```
a=65977
def dzielniki(a):
    dzielnik=[]
    for i in range(1,a+1):
        if a%i==0:
            dzielnik.append(i)
    return print(dzielnik)
dzielniki(a)
```
## Sprawdzanie pierszości liczby:
```
import sys
a=11
def czy_pierwsza(a):
    for i in range(2,a):
        if a%i==0:
            print("nie jest pierwsza")
            sys.exit()
    print("liczba jest pierwsza")

czy_pierwsza(a)
```
## Sito erastotenesa
```
liczby=[]
zakres=200
for i in range(2,zakres+1):
    liczby.append(i)
n=zakres//2 #ilosc przejsc petli

start=1
while start<n:
    start=start+1 
    for liczba in liczby[start:]:
        if liczba%start==0:
            liczby.remove(liczba)
print(liczby)
```
# W2. Problem sortowania. Przykłady naiwnych algorytmów sortowania. Technika "dziel i rządź", sortowanie przez scalanie.
Sortowanie polega na uporządkowaniu elementów zbioru według ustalonego kryterium, na przykład rosnąco lub malejąco.

## Sortowanie bąbelkowe
```
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # Wynik: [11, 12, 22, 25, 34, 64, 90]
```
## Sortowanie przez wybieranie
```
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print(arr)  # Wynik: [11, 12, 22, 25, 34, 64, 90]
```
## Technika "dziel i rządź", sortowanie przez scalanie:
Sortowanie przez scalanie jest efektywnym algorytmem sortowania, który stosuje technikę "dziel i rządź", dzieląc listę na mniejsze części, sortując je, a następnie łącząc w jedną posortowaną listę.
```
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Przykład użycia
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print(arr)  # Wynik: [11, 12, 22, 25, 34, 64, 90]

```
# W3. Sortowanie szybkie. Najgorsze przypadki i sposoby ich zapobiegania.
## Sortowanie szybkie (quicksort):
Quicksort to algorytm sortowania, który wybiera element referencyjny (zazwyczaj ostatni element w liście) i dzieli resztę elementów na dwie grupy: te mniejsze i większe od elementu referencyjnego, a następnie rekursywnie sortuje obie grupy.

## Najgorsze przypadki i sposoby ich zapobiegania:
Najgorszym przypadkiem dla quicksorta jest sytuacja, gdy zawsze wybieramy najmniejszy lub największy element jako element referencyjny, co prowadzi do niemal kwadratowej złożoności czasowej. Możemy temu zapobiec, losując element referencyjny lub używając techniki "trzy środki".

```
lista=[1,2,3,4,5,6,7,21,2,353,52,13,5,2,5,0,53,32]
def quicksort(lista):
    if (len(lista)<=1):
        return lista
    pivot= lista[0]
    lista_mniejszych_od_pivota=[i for i in lista[1:] if i<pivot]
    lista_wiekszych_od_pivota=[i for i in lista[1:] if i>=pivot]
    return quicksort(lista_mniejszych_od_pivota)+ [pivot] +quicksort(lista_wiekszych_od_pivota)

print(quicksort(lista))
```

# W4. Sortowanie stabilne. Sortowanie zbiorów o ograniczonym zakresie wartości.
Sortowanie stabilne:
Sortowanie stabilne zachowuje kolejność równych elementów w oryginalnej liście. Jest to przydatne w przypadku, gdy chcemy sortować po wielu kryteriach.

Sortowanie zbiorów o ograniczonym zakresie wartości:
W przypadku, gdy mamy do czynienia z małym zbiorem możliwych wartości, możemy skorzystać z algorytmu sortowania takiego zbioru, który wykorzystuje tę wiedzę, aby zoptymalizować proces sortowania.

### Sortowania stabilne:

-scalanie

-wstawianie

-bąbelkowe

-kubełkowe

-zliczanie

### Sortowania niestabilne:

-szybkie

-przez wybieranie

# W5. Problemy optymalizacyjne. Algorytmy zachłanne.
Problemy optymalizacyjne:
Problemy optymalizacyjne polegają na znalezieniu najlepszego rozwiązania spośród wielu możliwych w kontekście danego kryterium optymalizacyjnego.

Algorytmy zachłanne:
Algorytmy zachłanne podejmują lokalnie optymalne decyzje na każdym etapie, wierząc, że doprowadzi to do globalnie optymalnego rozwiązania.

Idac krok po kroku wybiera najlepsze mozliwe rozwiazanie bez uwzglednienia konsekwencji dla przyszlych decyzji
podejmuje lokalnie optymalnie wybór na kazdym etapie z nadzieja znalezienia globalnego optymalnalnego rozwiazania
np. optymalizacja trasy dostaw -przez drzewo

-algorytm Dijkstry - znajdowanie najkrótszej ścieżki z jednego wierzchołka do wszystkich innych wierzchołków w grafie ważonym bez wag ujemnych

-algorytm Kruskala - znajdowanie minimalnego drzewa rozpinającego dla połączonego, ważonego grafu

-algorytm Prima - znajdowanie minimalnego drzewa rozpinającego, która rozpoczyna się od pojedynczego wierzchołkaa

algorytmy zachlanne nie zawsze prowadza do rozwiazania globalnie optymalnego

```
# Algorytm Dijkstry - najkrotsza sciezka

mapa={
    "A":{'B':2,"D":4},
    "B":{'C':3,"D":3},
    "C":{'E':2},
    "D":{'C':3,"E":4},
    "E":{}
}


#ustaw najkrotsze odleglosci od wierzcholka
def algorytm_dijkstry(graph,start,goal):
    #wszystkie wezly oznacz jako nieodwiedzone, stworz zbior nieodwiedzonych wezlow
    
    #ustaw odleglosc wezla poczatkowego na 0 reszty na inf
    shortest_distance = {vortex: float('infinity') for vortex in graph}
    shortest_distance[start]=0
    predecessors={}
    #nieodwiedzone wierzcholki
    unvisited=graph.copy()
    
    # petle nieodwiedzonych wierzcholkow, sprawdzac petle o wierzcholku najmniejszej odleglosci
    #wierzcholek z najmniejsza odlegloscia 
    while unvisited:
        current_min_vortex=None
        for  vortex in unvisited:
            if current_min_vortex is None:
                current_min_vortex = vortex
            elif shortest_distance[vortex]< shortest_distance[current_min_vortex]:
                current_min_vortex = vortex
    #sprawdzanie wszystkich sasiadow aktualnego wierzcholka
        for neighbour,cost in graph[current_min_vortex].items():
            if cost + shortest_distance[current_min_vortex]< shortest_distance[neighbour]:
                shortest_distance[neighbour]=cost + shortest_distance[current_min_vortex]
                predecessors[neighbour]= current_min_vortex
    # usunac z listy przetworzony wierzcholek
        unvisited.pop(current_min_vortex)
    # odtworzenie sciezki od startu do celu
    current_vortex=goal
    path=[]
    while current_vortex !=start:
        path.append(current_vortex)
        current_vortex=predecessors[current_vortex]
    path.append(start)
    return path[::-1],shortest_distance[goal]

path, distance= algorytm_dijkstry(mapa,'A','E')
print(f"sciezka: {path}, dlugosc: {distance}")
```
# W6. Programowanie dynamiczne. Problem plecakowy, problem wydawania reszty.
### Programowanie dynamiczne:
Programowanie dynamiczne polega na rozwiązywaniu problemów poprzez rozwiązanie podproblemów i pamiętanie wyników, aby uniknąć wielokrotnego rozwiązywania tych samych podproblemów.

### Problem plecakowy:
Problem plecakowy polega na wybraniu przedmiotów o maksymalnej wartości, które zmieszczą się w plecaku o określonej pojemności.

### Problem wydawania reszty:
Problem wydawania reszty polega na znalezieniu najmniejszej liczby monet lub banknotów, które są potrzebne do wydania określonej kwoty

# W7. Listy jedno- i dwukierunkowe.
## Listy jednokierunkowe składają się z węzłów, z których każdy zawiera wartość oraz wskaźnik do następnego węzła.
### Zalety:

-prosta imolementacja

-efektywna w dodawaniu i usuwaniu elementow na poczatku listy

### Wady:

-dostep do elementow tylko w jednym kierunku

-trudnosc w usuwaniu ostatniego elementu

Zastosowania w kolejkach, stosach, historii przegladania w przegladarkach
```
class SinglyLinkedList:
    def __init__(self) :
        self.head=None #głowa listy, poczatkowo none
    def append(self,data):
        #dodawanie elementu na koniec listy
        if not self.head:
            self.head=Node(data) #jesli lista jest pusta, nowy element staje sie head
            return
        last=self.head
        while last.next:
            last=last.next #przechodzenie do ostatniego elementu
        last.next=Node(data) #tworzenie nowego elementu na koncu
    def display_all(self):
        #wyswietlenei wszystkich wartosci wraz z nastepna wartoscia
        current=self.head
        while current:
            next_value= current.next.data if current.next else "None"
            print(f"{current.data}, Next: {next_value}")
            current=current.next
        
    def display(self,data):
        #wyswietlenei pojedynczej wartosci wraz z nastepna wartoscia
        current=self.head
        while current:
            if current.data ==data:
                next_value= current.next.data if current.next else "None"
                print(f"{current.data}, Next={next_value}")
                return
            current=current.next
        print("Wartosc nie istnieje")
              

lista= SinglyLinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.display_all()
lista.display(2)
```
## Listy dwukierunkowe:
Listy dwukierunkowe są podobne do jednokierunkowych, ale każdy węzeł zawiera również wskaźnik do poprzedniego węzła jak i następnego.
### ZALETY:
-nawigacja w obi strony

-latwiejsze usuwanie danych

### WADY:

-wieksze uzycie pamieci

-skomplikowana implementacja w porownianiu do jednokierunkowych

### Zastosowania:

-kolejka priorytetowa

-zarzadzania zakladnkami w przegladarkach
```
class NodeTwo:
    def __init__(self,data):
        self.data = data #przechowywanie danych elementu
        self.next=None #wskażnik na nastepny element
        self.previous=None #wskaznik na poprzedni
        
class TwoLinkedList:
    def __init__(self) :
        self.head=None #głowa listy, poczatkowo none
    def append(self,data):
        #dodawanie elementu na koniec listy
        if not self.head:
            self.head=NodeTwo(data) #jesli lista jest pusta, nowy element staje sie head
            return
        last=self.head
        while last.next:
            last=last.next #przechodzenie do ostatniego elementu

        new=NodeTwo(data)
        last.next=new #tworzenie nowego elementu na koncu
        new.previous=last
    def display_all(self):
        #wyswietlenei wszystkich wartosci wraz z nastepna wartoscia
        print("\nDisplay all value:")
        current=self.head
        while current:
            previous= current.previous.data if current.previous else "None"
            next_value= current.next.data if current.next else "None"
            print(f"Value: {current.data}, Next: {next_value}, Previous: {previous}")
            current=current.next
        
    def display(self,data):
        #wyswietlenei  wartosci wraz z nastepna wartoscia i poprzednia wartoscia, dla podanej w wejsciu wartosci
        print(f"\nDisplay one value {data}:")
        current=self.head
        while current:
            if current.data ==data:
                next_value= current.next.data if current.next else "None"
                previous= current.previous.data if current.previous else "None"
                print(f"Value: {current.data}, Next={next_value}, Previous: {previous}")
                return
            current=current.next
        print("Wartosc nie istnieje")
        
        
lista2= TwoLinkedList()
lista2.append(1)
lista2.append(2)
lista2.append(3)
lista2.display_all()
lista2.display(1)
```

# W8. Tablice samorozszerzające.
### list() - lista zachowuje sie jako tablica samorozszerzająca, umozliwia dynamiczne dodawanie i usuwanie elementów bez koniecznosci recznego alokowania pamieci

listy moga zawierac wartosci roznych typow i automatycznie dostosuwuja swoj rozmiar dzialaja tak ze alokuja dodatkowa pamiec gdy rozmiar przekroczy jej aktualna pojemnosc gdy tak jest to pysthon alokuje nowa wieksza tablice i kopiuje a stara liste usuwa.

### zalety:

-elastycznosc

-prostota

-wydajnosc

### wady:

-koszt kopiowania

-nieprzewidywania wydajnosc
```
moja_lista=[]
moja_lista.append("fd")
moja_lista.append("fdddd")
print(moja_lista)
moja_lista.remove("fddddddd")
print(moja_lista)
```
# W9. Stosy. Kolejki.
## Stosy:

Stos to struktura danych, w której ostatnio dodany element jest pierwszym elementem do usunięcia (zasada LIFO - Last In, First Out).

```
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None
```
## Kolejki:

Kolejka to struktura danych, w której pierwszy dodany element jest pierwszym elementem do usunięcia (zasada FIFO - First In, First Out).

```
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None
```