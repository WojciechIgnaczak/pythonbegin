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
Pomimo swojej niskiej wydajności, może być używane do sortowania małych zbiorów danych, gdzie inne bardziej zaawansowane algorytmy mogą być nadmiernie skomplikowane.
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
Proste zastosowania: Jest prosty do zrozumienia i implementacji, co czyni go dobrym wyborem dla prostych zastosowań lub w przypadku niewielkich zbiorów danych.
Sortowanie małych zbiorów danych: Pomimo swojej niskiej wydajności, może być używany do sortowania małych zbiorów danych, gdzie inne bardziej zaawansowane algorytmy mogą być nadmiernie skomplikowane.
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
## Sortowanie przez wstawianie (insert)
Sortowanie przez wstawianie jest skuteczne dla małych zbiorów danych lub już prawie posortowanych danych. Jest też używane jako część innych algorytmów sortowania.
```
import time
import random

#lista=[2,5,5,3,5,1,89,3,5,2]

def insert_sort(lista):
    number=len(lista)
    for i in range(1,number):
        temp=lista[i]
        t=i-1
        while t>=0 and lista[t]>temp:
            lista[t+1]=lista[t]
            t-=1
            lista[t+1]=temp
    return lista
ile_liczb=10000
lista=[random.randint(1,100) for i in range(ile_liczb)]
start_time=time.time()
insert_sort(lista)
end_time=time.time()
czas=end_time-start_time
print(f"Czas sortowania dla {ile_liczb} liczb wynosi: {round(czas,6)}")
```
## Sortowanie przez zliczanie
Sortowanie przez zliczanie (Counting Sort) jest szczególnie skuteczne, gdy mamy do czynienia z dużą liczbą powtarzających się elementów w ograniczonym zakresie
```
lista=[1,32,4,2,4,2,45,5,6,45,6,57,34,6,7,7,4,5,53,34,3]
def sort_scal(lista):
    maximum=max(lista)
    ilosc=maximum+1
    tablica=[0]*ilosc
    for i in lista:
        tablica[i]+=1
    posortowana = []
    for i in range(ilosc):
        posortowana.extend([i] * tablica[i])
    return posortowana
print(sort_scal(lista))
```
## Sortowanie kubełkowe
Najlepiej działa, gdy dane wejściowe są równomiernie rozłożone w zakresie. Jest używany w sytuacjach, gdzie zakres danych jest znany i niezbyt duży.
Sortowanie z dużą ilością danych: Jest efektywny, gdy mamy do czynienia z dużą ilością danych, które można podzielić na wiele kubełków, co pozwala na równoległe sortowanie.
```
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Umieszczamy każdy element w odpowiednim kubełku
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    # Sortujemy zawartość każdego kubełka
    for bucket in buckets:
        insertion_sort(bucket)

    # Łączymy posortowane kubełki
    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr

# Przykładowe użycie
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23]
sorted_arr = bucket_sort(arr)
print("Posortowana lista:", sorted_arr)
```

## Technika "dziel i rządź", sortowanie przez scalanie:
Sortowanie przez scalanie jest efektywnym algorytmem sortowania, który stosuje technikę "dziel i rządź", dzieląc listę na mniejsze części, sortując je, a następnie łącząc w jedną posortowaną listę. Doskonale sprawdza się w przypadku sortowania list lub tablic o dużych rozmiarach.
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
Quicksort to algorytm sortowania, który wybiera element referencyjny (zazwyczaj ostatni element w liście) i dzieli resztę elementów na dwie grupy: te mniejsze i większe od elementu referencyjnego, a następnie rekursywnie sortuje obie grupy. Quick Sort jest jednym z najszybszych algorytmów sortowania dla typowych zbiorów danych. Jest wydajny dla dużych zbiorów danych, dzięki swojej złożoności czasowej O(n log n) w przypadku średnim.
Systemy baz danych: Quick Sort jest często używany w systemach baz danych do sortowania wyników zapytań, sortowania indeksów, czy nawet wewnętrznych operacji sortowania w bazach danych.

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

#### Sortowanie przez scalanie (Merge Sort):

-Średnia i najgorsza złożoność czasowa: O(n log n)

-Najlepsza złożoność czasowa: O(n log n)

#### Sortowanie przez wstawianie (Insertion Sort):

-Średnia i najgorsza złożoność czasowa: O(n^2)

-Najlepsza złożoność czasowa: O(n), gdy dane są już posortowane

#### Sortowanie bąbelkowe (Bubble Sort):

-Średnia i najgorsza złożoność czasowa: O(n^2)

-Najlepsza złożoność czasowa: O(n), gdy dane są już posortowane

#### Sortowanie kubełkowe (Bucket Sort):

-Średnia złożoność czasowa: O(n + k), gdzie k jest liczbą kubełków

-Najgorsza złożoność czasowa: O(n^2), gdy wszystkie elementy trafią do jednego kubełka

-Najlepsza złożoność czasowa: O(n + k), gdy dane są równomiernie rozłożone po kubełkach
#### Sortowanie przez zliczanie (Counting Sort):
Złożoność czasowa: O(n + k), gdzie k jest zakresem danych
Jest liniowym algorytmem sortowania, ale może wymagać dużo pamięci w zależności od zakresu danych.

### Sortowania niestabilne:

#### Sortowanie szybkie (Quick Sort):
Średnia złożoność czasowa: O(n log n)

Najgorsza złożoność czasowa: O(n^2), gdy pivot jest zawsze najmniejszy lub największy element

Najlepsza złożoność czasowa: O(n log n), gdy pivoty są dobrze wyważone

#### Sortowanie przez wybieranie (Selection Sort):

Średnia, najgorsza i najlepsza złożoność czasowa: O(n^2)

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
```
# Algorytm Kruskala
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimum_cost = 0
        print("Minimalne drzewo rozpinające:")
        for u, v, weight in result:
            print(f"Krawędź {u} - {v}, waga: {weight}")
            minimum_cost += weight
        print("Minimalny koszt:", minimum_cost)


# Przykładowe użycie:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal()

```
```
# Algorytm Prima
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = None

        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v

        return min_index

    def prim(self):
        parent = [None] * self.V
        key = [sys.maxsize] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Minimalne drzewo rozpinające:")
        for i in range(1, self.V):
            print(f"Krawędź {parent[i]} - {i}, waga: {self.graph[i][parent[i]]}")


# Przykładowe użycie:
g = Graph(5)
g.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

g.prim()

```

# W6. Programowanie dynamiczne. Problem plecakowy, problem wydawania reszty.
### Programowanie dynamiczne:
Programowanie dynamiczne polega na rozwiązywaniu problemów poprzez rozwiązanie podproblemów i pamiętanie wyników, aby uniknąć wielokrotnego rozwiązywania tych samych podproblemów.

### Problem plecakowy:
Problem plecakowy polega na wybraniu przedmiotów o maksymalnej wartości, które zmieszczą się w plecaku o określonej pojemności.Problem plecakowy jest jednym z klasycznych problemów optymalizacyjnych, w którym chcemy wybrać przedmioty o maksymalnej wartości, które zmieszczą się w plecaku o ograniczonej pojemności. Istnieją różne warianty tego problemu, ale jeden z najczęstszych to "0/1 problem plecakowy", gdzie każdy przedmiot można wybrać tylko raz (lub nie wybrać wcale).
```
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Przykładowe użycie:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value = knapsack(weights, values, capacity)
print("Maksymalna wartość, którą można umieścić w plecaku:", max_value)

```
### Problem wydawania reszty:
Problem wydawania reszty polega na znalezieniu najmniejszej liczby monet lub banknotów, które są potrzebne do wydania określonej kwoty.
Problem wydawania reszty polega na znalezieniu minimalnej liczby monet (lub banknotów) potrzebnych do wydania danej kwoty, używając dostępnych nominałów. Ten problem często występuje w codziennym życiu, np. przy obsłudze automatów, sklepów lub bankomatów
```
def wydaj_reszte(nominaly, kwota):
    nominaly.sort(reverse=True)  # Sortujemy nominały malejąco
    reszta = []
    for nominal in nominaly:
        while kwota >= nominal:
            reszta.append(nominal)
            kwota -= nominal
    return reszta

# Przykładowe użycie:
nominaly = [200, 100, 50, 20, 10, 5, 2, 1]  # Dostępne nominały
kwota = 348  # Kwota do wydania reszty

reszta = wydaj_reszte(nominaly, kwota)
print("Minimalna liczba nominałów potrzebna do wydania reszty:", len(reszta))
print("Nominały wydane jako reszta:", reszta)

```
# W7. Listy jedno- i dwukierunkowe.
## Listy jednokierunkowe składają się z węzłów, z których każdy zawiera wartość oraz wskaźnik do następnego węzła.
### Zalety:

-prosta implementacja

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