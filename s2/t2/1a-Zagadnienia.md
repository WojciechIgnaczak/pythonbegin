# DEFINICJA DRZEWA. REPREZENTACJA W PAMIĘCI.

Drzewo to struktura danych składająca się z węzłów, gdzie każdy węzeł ma pewną wartość i wskaźniki do swoich dzieci. Drzewo jest zorganizowane w sposób hierarchiczny, z jednym wyróżnionym węzłem zwanym korzeniem, od którego wychodzą inne węzły. Każdy węzeł może mieć dowolną liczbę dzieci.

Drzewo można reprezentować w pamięci na kilka sposobów:

Lista dzieci: Każdy węzeł przechowuje wskaźniki do swoich dzieci w postaci listy.
Rodzic-wskaźnik: Każdy węzeł przechowuje wskaźnik do swojego rodzica, a także listę dzieci.
Tablica: Drzewo binarne można reprezentować w tablicy, gdzie dla węzła o indeksie i:
lewy dziecko znajduje się na indeksie 2i + 1
prawe dziecko znajduje się na indeksie 2i + 2

jezeli kazdy rodzic ma jedno dziecko to drzewo to jest to lista

# DRZEWA BINARNE. 

# ALGORYTMY PRZESZUKIWANIA DRZEWA: WSZERZ I W GŁĄB.

# PRZESZUKIWANIE LINIOWE I PRZESZUKIWANIE BINARNE. 

# DRZEWO PRZESZUKIWAŃ BINARNYCH. 

# BALANS DRZEWA BINARNEGO. 

# DRZEWA CZERWONO-CZARNE. O(log n) czas operacji
Drzewo czerwono-czarne to zbalansowane drzewo BST z dodatkowymi właściwościami:
Drzewa czerwono-czarne (ang. red-black trees) są odmianą samoorganizujących się binarnych drzew poszukiwań.

W liściach drzew czerwono-czarnych nie przechowuje się danych.

Puste wskazanie w polu syna węzła może być interpretowane jako liść. Jednakże używanie rzeczywistych liści upraszcza niektóre algorytmy na drzewach czerwono-czarnych. 

Drzewa czerwono-czarne gwarantują, iż ich wysokość nie przekroczy dwukrotnej wartości wysokości minimalnej. Dokonywane jest to przez kolorowanie węzłów na czerwono lub czarno i stosowanie po każdej operacji wstawiania lub usuwania odpowiedniej procedury równoważącej drzewo, tak aby były spełnione następujące warunki:

Każdy węzeł drzewa jest albo czerwony, albo czarny.
Każdy liść drzewa (węzeł pusty nil) jest zawsze czarny.
Korzeń drzewa jest zawsze czarny.
Jeśli węzeł jest czerwony, to obaj jego synowie są czarni – innymi słowy, w drzewie nie mogą występować dwa kolejne czerwone węzły, ojciec i syn.
Każda prosta ścieżka od danego węzła do dowolnego z jego liści potomnych zawiera tę samą liczbę węzłów czarnych.

Wstawianie węzła:

Usuwanie wezla:

# SŁOWNIKI I ZBIORY. IMPLEMENTACJA PRZY UŻYCIU DRZEWA PRZESZUKIWAŃ BINARNYCH.

# HASZOWANIE. ALGORYTMICZNE FUNKCJE HASZUJĄCE. 

# TABLICE HASZUJĄCE. PODSTAWOWE TECHNIKI ROZWIĄZYWANIA KONFLIKTÓW.

# ZASTOSOWANIE TABLIC HASZUJĄCYCH DO IMPLEMENTACJI SŁOWNIKÓW I ZBIORÓW.