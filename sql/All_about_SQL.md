# 0. HISTORIA
Lata 60. i 70.: Początki baz danych IBM
Lata 80.: Relacyjne bazy danych RDBMS ORACLE,IBM,DB2,MSSQL
Lata 90.: Rozwój internetu i open source
XXI wiek: Big Data i NoSQL

# 1. Wprowadzenie do Systemów Baz Danych (DBMS):
Systemy baz danych (DBMS) są to narzędzia, które umożliwiają przechowywanie, zarządzanie i manipulowanie danymi. Są one wykorzystywane w różnych dziedzinach, takich jak biznes, nauka, administracja publiczna itp. DBMS umożliwiają użytkownikom tworzenie, aktualizowanie, odczytywanie i usuwanie danych w sposób zorganizowany i efektywny.

### Relacyjny Model Danych:
Relacyjny model danych jest jednym z najbardziej popularnych modeli baz danych. W modelu tym dane są przechowywane w postaci tabel, gdzie każda tabela składa się z wierszy (rekordów) i kolumn (pól). Relacje między tabelami są reprezentowane za pomocą kluczy obcych i kluczy głównych. Model relacyjny jest elastyczny i umożliwia łatwe wykonywanie zapytań.

### Charakterystyka modelu relacyjnego:

Strukturalność: Dane są przedstawione w postaci tabel, które są prostymi, czytelnymi strukturami.

Integralność danych: Model relacyjny zapewnia integralność danych poprzez reguły i ograniczenia, takie jak klucze główne i obce.
Normalizacja: Proces organizowania danych w celu eliminacji redundancji i zapewnienia spójności.

Niezależność danych: Oddzielenie logicznej struktury danych od ich fizycznej implementacji umożliwia łatwiejsze zarządzanie i modyfikację danych.

### Inne Modele Baz Danych:
Hierarchiczny Model Danych: Dane są zorganizowane w postaci drzewa, gdzie każdy węzeł ma jeden rodzica i wiele dzieci. Ten model był popularny w latach 60. i 70., ale obecnie jest rzadziej stosowany.
Sieciowy Model Danych: Rozbudowany model hierarchiczny, który pozwala na bardziej złożone relacje między rekordami poprzez wprowadzenie wielu rodziców dla danego węzła.
Obiektowy Model Danych: Rozszerzenie relacyjnego modelu danych, które pozwala na przechowywanie obiektów w bazie danych. Obiekty mogą zawierać metody i właściwości, co jest użyteczne w programowaniu obiektowym.
Model Dokumentowy: Dane są przechowywane w postaci dokumentów, na przykład w formacie JSON lub XML. Ten model jest często używany w aplikacjach webowych i NoSQL bazach danych.



# 2. Modelowanie Pojęciowe: Model Związków-Encji (ER)
## Encje:
Encje reprezentują konkretne obiekty lub koncepcje, takie jak osoba, produkt, zamówienie, czy faktura.
Każda encja jest reprezentowana jako prostokąt w diagramie ER, z nazwą encji wewnątrz prostokąta.
Encje mogą mieć atrybuty, które opisują cechy encji, np. imię, nazwisko, cena.
## Atrybuty:
Atrybuty opisują właściwości encji i zawierają informacje na temat każdego rekordu w tabeli.
Mogą być prostymi typami danych, takimi jak liczby całkowite, łańcuchy znaków, daty, lub bardziej złożonymi typami danych, takimi jak obrazy lub dokumenty.
Atrybuty są reprezentowane jako elipsy w diagramie ER, z nazwą atrybutu wewnątrz elipsy.
## Związki:
Związki określają relacje między encjami.
Mogą być jednokierunkowe lub obustronne, oraz binarne lub n-arnie (gdzie n > 2).
Związki są reprezentowane jako linie łączące encje w diagramie ER, z etykietami określającymi naturę związku (np. "ma", "składa się z").
## Transformacja z Modelu Pojęciowego do Relacyjnego
Encje na Tabele:
Każda encja w diagramie ER staje się tabelą w schemacie relacyjnym.
Nazwa encji staje się nazwą tabeli, a jej atrybuty stają się kolumnami tabeli.
Atrybuty na Kolumny:
Atrybuty każdej encji stają się kolumnami w odpowiadających im tabelach.
Każdy atrybut musi zostać przyporządkowany odpowiedniemu typowi danych, np. VARCHAR, INT, DATE, itp.

### Terminologia:

Relacje (Tabele):

Zbiór danych zorganizowanych w formie tabeli, gdzie każda tabela reprezentuje pewien zbiór obiektów lub zdarzeń.
Przykład: Tabela "Pracownicy" może zawierać informacje o pracownikach firmy.
Krotki (Wiersze/Rekordy):

Pojedynczy wiersz w tabeli, który reprezentuje jeden rekord danych.
Przykład: Każdy wiersz w tabeli "Pracownicy" może reprezentować jednego pracownika z danymi, takimi jak imię, nazwisko, stanowisko, itp.
Atrybuty (Kolumny/Pola):

Pojedyncza kolumna w tabeli, która reprezentuje pewien typ danych.
Przykład: Kolumna "Imię" w tabeli "Pracownicy" przechowuje imiona wszystkich pracowników.

### KLUCZE
Główny- identyfikator tabeli

Obcy - powiązania z innymi tabelami

Unikalny- unikalność wartości w kolumnie

Związki na Klucze Obce:
Związki między encjami są reprezentowane za pomocą kluczy obcych w tabelach.
Klucz obcy wskazuje na klucz główny innej tabeli, tworząc w ten sposób relację między nimi.

## Normalizacja i Denormalizacja Schematu Relacyjnej Bazy Danych
Normalizacja:
Normalizacja to proces projektowania bazy danych w taki sposób, aby unikać redundancji danych i anomalii związanych z wprowadzaniem, aktualizacją i usuwaniem danych.
Proces ten jest realizowany poprzez dzielenie tabel na mniejsze, bardziej znormalizowane tabele, aby uniknąć powtarzania tych samych informacji.
Denormalizacja:
Denormalizacja jest przeciwnym procesem do normalizacji, polegającym na dodawaniu redundancji danych w celu poprawy wydajności odczytu danych.
Jest stosowana w przypadkach, gdy wymagane są szybkie zapytania czy raporty, a wydajność zapisu danych jest mniej istotna.

### 1NF (First Normal Form)
Definicja:
Pierwsza postać normalna (1NF) jest pierwszym etapem normalizacji, który ma na celu eliminację wielowartościowych atrybutów oraz powtórzeń grup danych w pojedynczych rekordach.
Aby spełnić warunki 1NF, każda komórka w tabeli musi przechowywać pojedynczą wartość, a nie zestawy wartości.
Właściwości:
Atomowe Atrybuty: Każda kolumna (atrybut) tabeli musi być atomowa, co oznacza, że ​​nie może przechowywać zestawu wartości ani struktur danych.
Unikalne Nazwy Kolumn: Każda kolumna w tabeli musi mieć unikalną nazwę, a nie mogą występować powtarzające się kolumny.
Przykład:
Rozważmy tabelę o nazwie "Zamówienia" z kolumnami: ID_zamówienia, Produkty, Ilość, Klient. Ta tabela nie spełnia warunków 1NF, ponieważ kolumna "Produkty" może zawierać zestawy wartości (np. "telefon, laptop") dla jednego zamówienia.

### 2NF (Second Normal Form)
Definicja:
Druga postać normalna (2NF) jest etapem normalizacji, w którym eliminowane są zależności częściowe od klucza głównego, czyli każda kolumna w tabeli musi bezpośrednio zależeć od klucza głównego.
Właściwości:
Spełnienie 1NF: Tabela musi już być w pierwszej postaci normalnej (1NF).
Brak Zależności Częściowych: Każda niekluczowa kolumna musi być w pełni zależna od każdego klucza kandydującego w tabeli.
Przykład:
Rozważmy tabelę "Zamówienia" z kolumnami: ID_zamówienia, ID_produktu, Nazwa_produktu, Ilość. W tej tabeli ID_produktu jest kluczem częściowym, a kolumna "Nazwa_produktu" zależy tylko od ID_produktu, co oznacza, że tabela nie jest w 2NF.

### 3NF (Third Normal Form)
Definicja:
Trzecia postać normalna (3NF) jest kolejnym etapem normalizacji, w którym eliminowane są zależności przekłamane, czyli każda niekluczowa kolumna musi być niezależna od innych niekluczowych kolumn w tej samej tabeli.
Właściwości:
Spełnienie 2NF: Tabela musi już być w drugiej postaci normalnej (2NF).
Brak Zależności Przekłamanych: Każda niekluczowa kolumna musi być niezależna od innych niekluczowych kolumn w tej samej tabeli.
Przykład:
Rozważmy tabelę "Zamówienia" z kolumnami: ID_zamówienia, ID_klienta, Nazwa_klienta, Miasto_klienta. W tej tabeli kolumna "Miasto_klienta" zależy tylko od ID_klienta, a nie bezpośrednio od ID_zamówienia, co oznacza, że tabela nie jest w 3NF.

Wdrożenie normalizacji od 1NF do 3NF pomaga w zapewnieniu spójności, integralności danych i unikaniu redundancji, co prowadzi do lepszego projektu bazy danych.

### Denormalizacja
Denormalizacja jest procesem celowego wprowadzania redundancji do znormalizowanej bazy danych w celu poprawy wydajności zapytań. Chociaż denormalizacja może prowadzić do niektórych problemów związanych z integralnością danych i większym zużyciem pamięci, może być korzystna w pewnych sytuacjach, takich jak:

Poprawa wydajności odczytu: Szybsze pobieranie danych, ponieważ mniej operacji JOIN jest wymaganych.
Optymalizacja zapytań: Redukcja złożoności zapytań, co może poprawić ich wydajność.

# 3. DDL - język opisu danych. Tworzenie, modyfikacja i destrukcja poszczególnych obiektów bazy danych.
## Tworzenie Obiektów Bazy Danych
### Tabele:
Tworzenie tabeli rozpoczyna się od komendy CREATE TABLE.
Struktura tabeli jest definiowana za pomocą nazwy tabeli, listy kolumn i ich typów danych, a także dodatkowych opcji, takich jak klucze główne, ograniczenia integralności i indeksy.
Przykład:

CREATE TABLE Pracownicy (
    ID INT PRIMARY KEY,
    Imię VARCHAR(50),
    Nazwisko VARCHAR(50),
    Data_zatrudnienia DATE
);

### Indeksy:
Indeksy służą do przyspieszania wyszukiwań w bazie danych.
Tworzenie indeksu rozpoczyna się od komendy CREATE INDEX.
Wskazujemy nazwę indeksu, tabelę oraz kolumny, na których ma być stworzony indeks.
Przykład:

CREATE INDEX idx_imię ON Pracownicy (Imię);

### Widoki:
Widoki są wirtualnymi tabelami, które są wynikiem zapytań SQL.
Tworzenie widoku rozpoczyna się od komendy CREATE VIEW.
Określamy nazwę widoku oraz zapytanie, na podstawie którego ma zostać utworzony.
Przykład:

CREATE VIEW Nowi_pracownicy AS
SELECT * FROM Pracownicy WHERE Data_zatrudnienia > '2022-01-01';

### Procedury:
Procedury to zbiory instrukcji SQL, które mogą być wielokrotnie wykonywane.
Tworzenie procedury rozpoczyna się od komendy CREATE PROCEDURE.
Określamy nazwę procedury, listę parametrów (opcjonalnie) oraz ciało procedury.
Przykład:

CREATE PROCEDURE Dodaj_pracownika (IN imię VARCHAR(50), IN nazwisko VARCHAR(50))
BEGIN
    INSERT INTO Pracownicy (Imię, Nazwisko) VALUES (imię, nazwisko);
END;



## Modyfikacja Obiektów Bazy Danych
### Tabele:
Modyfikacja tabeli może polegać na dodawaniu nowych kolumn, zmianie typu danych kolumny, dodawaniu ograniczeń integralności, usuwaniu kolumn, itp.
Do modyfikacji tabeli używamy komendy ALTER TABLE.
Przykład:

ALTER TABLE Pracownicy ADD COLUMN Stanowisko VARCHAR(100);

### Indeksy:
Modyfikacja indeksów może polegać na zmianie ich nazw, usuwaniu, zmianie typu indeksu, itp.
W niektórych systemach można użyć komendy ALTER INDEX do modyfikacji indeksów, jednak nie jest to standardowa składnia w języku SQL.

### Widoki:
Modyfikacja widoków może polegać na zmianie ich definicji, zmianie nazwy, usuwaniu, itp.
W niektórych systemach można użyć komendy ALTER VIEW do modyfikacji widoków, jednak nie jest to standardowa składnia w języku SQL.

### Procedury:
Modyfikacja procedur może polegać na zmianie ich definicji, dodawaniu lub usuwaniu instrukcji SQL, zmianie nazwy, itp.
W niektórych systemach można użyć komendy ALTER PROCEDURE do modyfikacji procedur, jednak nie jest to standardowa składnia w języku SQL.



## Destrukcja Obiektów Bazy Danych
### Tabele:
Usuwanie tabeli rozpoczyna się od komendy DROP TABLE.
Po tej komendzie struktura i dane w tabeli zostaną trwale usunięte.
Przykład:

DROP TABLE Pracownicy;

### Indeksy:
Usuwanie indeksu rozpoczyna się od komendy DROP INDEX.
Po tej komendzie indeks zostanie trwale usunięty.
Przykład:

DROP INDEX idx_imię ON Pracownicy;

### Widoki:
Usuwanie widoku rozpoczyna się od komendy DROP VIEW.
Po tej komendzie widok zostanie trwale usunięty.
Przykład:

DROP VIEW Nowi_pracownicy;

### Procedury:
Usuwanie procedury rozpoczyna się od komendy DROP PROCEDURE.
Po tej komendzie procedura zostanie trwale usunięta.
Przykład:

DROP PROCEDURE Dodaj_pracownika;

### Podsumowanie
Komendy DDL pozwalają na definiowanie struktury bazy danych, tworzenie nowych obiektów, ich modyfikację oraz usuwanie. Zapewniają one dużą elastyczność i kontrolę nad bazą danych, umożliwiając dostosowywanie jej do zmieniających się wymagań biznesowych.



# 4.DML - język manipulowania danymi. Pojęcie transakcji. Zarządzanie transakcjami. Integralność́ danych, zarządzanie więzami integralności. Indeksy i optymalizacja bazy danych. 


DML (Data Manipulation Language) to podzbiór języka SQL (Structured Query Language), który umożliwia manipulowanie danymi w bazie danych. Pozwala na dodawanie, usuwanie, aktualizację i wybieranie danych w tabelach.

### Podstawowe operacje DML:
INSERT: Wstawianie nowych danych do tabeli.
SELECT: Wybieranie danych z tabeli.
UPDATE: Aktualizowanie istniejących danych w tabeli.
DELETE: Usuwanie danych z tabeli.
Przykłady:

-- INSERT
INSERT INTO Pracownicy (Imię, Nazwisko, Stanowisko) VALUES ('Jan', 'Kowalski', 'Manager');

-- SELECT
SELECT * FROM Pracownicy WHERE Stanowisko = 'Manager';

-- UPDATE
UPDATE Pracownicy SET Stanowisko = 'Dyrektor' WHERE ID = 1;

-- DELETE
DELETE FROM Pracownicy WHERE ID = 1;


### Pojęcie Transakcji
Definicja:
Transakcja to sekwencja operacji wykonywanych w bazie danych, która tworzy logiczną jednostkę pracy.
Transakcje są atomowe, co oznacza, że ​​są wykonywane jako całość lub w ogóle nie są wykonywane.
Transakcje zapewniają spójność i integralność danych w bazie.

Właściwości transakcji:
Atomowość: Transakcja jest wykonywana jako jedna, niepodzielna operacja.
Spójność: Po zakończeniu transakcji baza danych przechodzi z jednego spójnego stanu do innego.
Izolacja: Transakcje są izolowane od siebie, zmiany dokonane przez jedną transakcję nie są widoczne dla innych transakcji do momentu ich zakończenia.
Trwałość: Po zakończeniu transakcji zmiany są trwale zapisywane w bazie danych, nawet w przypadku awarii systemu.
Zarządzanie Transakcjami
Rozpoczęcie transakcji:
Transakcję rozpoczynamy za pomocą instrukcji BEGIN TRANSACTION lub START TRANSACTION.
Zakończenie transakcji:
Transakcję zamykamy za pomocą instrukcji COMMIT, aby potwierdzić zmiany i zatwierdzić je w bazie danych.
W przypadku niepowodzenia transakcji możemy użyć instrukcji ROLLBACK, aby cofnąć zmiany i przywrócić bazę danych do stanu poprzedniego.

Przykład:

BEGIN TRANSACTION;
UPDATE Pracownicy SET Stanowisko = 'Manager' WHERE ID = 1;
COMMIT; -potwierdzenie
ROLLBACK- wycofanie


### Właściwości transakcji: ACID

Atomicity (Niepodzielność):
Transakcja jest niepodzielna, co oznacza, że wszystkie operacje wchodzące w skład transakcji muszą być wykonane w całości, albo żadna z nich. Jeśli jakakolwiek operacja w ramach transakcji zawiedzie, cała transakcja jest wycofywana.

Consistency (Spójność):
Transakcje przenoszą bazę danych z jednego spójnego stanu do innego spójnego stanu. Oznacza to, że wszystkie reguły i ograniczenia danych są spełnione zarówno przed, jak i po transakcji.

Isolation (Izolacja):
Operacje wykonywane w ramach jednej transakcji są izolowane od operacji innych transakcji. Izolacja zapewnia, że równoczesne transakcje nie interferują ze sobą, co jest szczególnie ważne w środowiskach z wieloma użytkownikami.

Durability (Trwałość):
Po zatwierdzeniu transakcji jej wyniki są trwałe, nawet w przypadku awarii systemu. Dane są zapisywane na trwałych nośnikach, takich jak dyski twarde.

### BLOKADY I IZOLACYJNOŚĆ
Blokady współdzielone (Shared Locks):
Umożliwiają wielu transakcjom jednoczesne odczytywanie zasobu, ale blokują jego modyfikację.

Blokady wyłączne (Exclusive Locks):
Umożliwiają jednej transakcji modyfikację zasobu i blokują zarówno odczyt, jak i modyfikację przez inne transakcje.

#### Mechanizny izolacyjności:

READ UNCOMMITED -najniższy poziom, mogą czytać zmiany wprowadzone przez inne transakcje, które nie są potwierdzone

READ COMMITTED- czytają tylko te zmiany które zostały zatwierdzone przez inne transakcje

REPEATABLE READ - transakcje czytają tylko zmiany które zostały zatwierdzone i blokują inne transakcje przed modyfikacją

SERIALIZABLE -najwyższy poziom. Transakcje wykonywane 1 po 2. Obniża wydajność, ale zapobiega błędom

### Integralność Danych i Zarządzanie Więzami Integralności
Definicja:
Integralność danych to stan, w którym dane w bazie są spójne, dokładne i zgodne z określonymi regułami.
Więzy integralności to reguły, które muszą być spełnione, aby zapewnić integralność danych.

### Typy więzów integralności:
Klucz główny (Primary Key): Zapewnia unikalność wartości w kolumnie, identyfikując tym samym każdy rekord w tabeli.
Klucz obcy (Foreign Key): Zapewnia spójność referencyjną między dwiema tabelami, ograniczając wartości w jednej kolumnie, aby odpowiadały wartościom w innej kolumnie w innej tabeli.
Więzy unikalności (Unique Constraint): Zapewnia, że ​​wartości w określonej kolumnie są unikalne.
Więzy check (Check Constraint): Określa warunki, które dane muszą spełniać.

## Indeksy w Bazach Danych
Indeksy są strukturami danych stosowanymi w bazach danych w celu przyspieszenia operacji wyszukiwania, sortowania i łączenia danych. Działają podobnie jak indeksy w książce - pomagają znaleźć potrzebne dane szybciej, skracając czas wyszukiwania.

### Rodzaje Indeksów:

#### Indeks Jednokolumnowy:

Tworzony jest na jednej kolumnie tabeli.
Przyspiesza wyszukiwanie danych w oparciu o tę konkretną kolumnę.
Jest najczęściej używany w bazach danych.


#### Indeks Wielokolumnowy:

Tworzony jest na kilku kolumnach tabeli.
Umożliwia przyspieszenie zapytań, które obejmują te kolumny.

### Indeks Unikalny:

Zapewnia unikalność wartości w kolumnie lub zestawie kolumn.
Uniemożliwia wstawianie duplikatów wartości, które już istnieją w indeksowanej kolumnie lub zestawie kolumn.

### Indeks Kompozytowy:

Jest to rodzaj indeksu wielokolumnowego, który jest tworzony na kombinacji kilku kolumn.
Przyspiesza wyszukiwanie i łączenie danych na podstawie tych kolumn.

### Indeks Pełnotekstowy:

Wykorzystywany jest w przypadku pełnotekstowych wyszukiwań, np. gdy potrzebne jest wyszukanie frazy lub słów kluczowych w tekście.
Zazwyczaj stosowany jest w przypadku dużych zbiorów danych tekstowych.


### Korzyści z Używania Indeksów:
Skrócenie Czasu Wyszukiwania: Operacje wyszukiwania danych są wykonywane szybciej, co przyspiesza działanie aplikacji korzystającej z bazy danych.

Optymalizacja Zapytań: Indeksy mogą optymalizować wykonywane zapytania, co prowadzi do efektywniejszego korzystania z zasobów bazy danych.

Poprawa Wydajności Aplikacji: Dzięki szybszym operacjom wyszukiwania i sortowania danej aplikacji staje się bardziej responsywna i wydajna.

Redukcja Zużycia Zasobów: Pomimo zwiększonej ilości pamięci zajmowanej przez indeksy, korzyści płynące z szybszych operacji mogą przewyższać te koszty.

### Kiedy Stosować Indeksy:
Indeksy powinny być stosowane na kolumnach, które są często używane w operacjach wyszukiwania, sortowania lub łączenia danych.
Ważne jest unikanie nadmiernego indeksowania, ponieważ zbyt wiele indeksów może spowolnić działanie bazy danych podczas operacji wstawiania, aktualizacji lub usuwania danych.

### Optymalizacja Indeksów:
Regularna Analiza Wydajności: Regularna analiza wydajności indeksów pozwala na identyfikację i usuwanie zbędnych lub mało wykorzystywanych indeksów.
Tworzenie Indeksów Tam, Gdzie To Konieczne: Unikaj nadmiernego tworzenia indeksów i stosuj je tam, gdzie faktycznie są potrzebne.
Monitorowanie Zapytań: Monitorowanie zapytań pozwala na identyfikację tych, które mogą wymagać dodatkowych indeksów lub optymalizacji istniejących.
Uwzględnienie Rozmiaru Bazy Danych: W dużych bazach danych indeksy mogą być kluczowe dla wydajności, ale w małych bazach danych mogą powodować nadmierną złożoność i opóźnienia.
Indeksy są ważnym narzędziem w optymalizacji wydajności baz danych. Jednak ich nadmiar lub nieodpowiednie zastosowanie może prowadzić do problemów z wydajnością. Dlatego ważne jest zrozumienie ich zastosowań, rodzajów i wpływu na wydajność systemu.




# 5.Język SQL (m.in.: projekcja, selekcja, grupowanie, sortowanie, połączenie, suma, iloczyn, różnica, podzapytania, zapytania skorelowane).
## 1. Projekcja:
Projekcja w języku SQL polega na wybieraniu określonych kolumn z tabeli lub wyniku zapytania. Jest to operacja wyświetlania tylko tych danych, które są potrzebne dla danego zadania. Może obejmować pojedyncze kolumny lub wyrażenia, które wyliczają wartości na podstawie danych.

Przykład:

SELECT imie, nazwisko FROM pracownicy;

## 2. Selekcja:
Selekcja, znana również jako klauzula WHERE, służy do wybierania wierszy z tabeli, które spełniają określone kryteria. Pozwala na filtrowanie danych na podstawie warunków określonych przez użytkownika.

Przykład:

SELECT * FROM produkty WHERE cena > 100;

## 3. Grupowanie:
Grupowanie w języku SQL pozwala na łączenie wierszy z tabeli na podstawie wartości określonych kolumn, a następnie wykonywanie operacji na każdej grupie. Najczęściej używane są funkcje agregujące, takie jak SUM, AVG, COUNT, MIN, MAX.

Przykład:

SELECT kategoria, COUNT(*) AS liczba_produktow FROM produkty GROUP BY kategoria;

## 4. Sortowanie:
Sortowanie pozwala na uporządkowanie wyników zapytania według wartości określonej kolumny lub kolumn. Można sortować dane rosnąco (ASC) lub malejąco (DESC).

Przykład:

SELECT * FROM klienci ORDER BY nazwisko ASC;

## 5. Połączenie:
Połączenie w języku SQL umożliwia łączenie danych z dwóch lub więcej tabel na podstawie określonych warunków. Najczęściej stosowane są operatory JOIN, takie jak INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN.

Przykład (INNER JOIN):

SELECT pracownicy.imie, dzialy.nazwa FROM pracownicy INNER JOIN dzialy ON pracownicy.dzial_id = dzialy.id;

## 6. Operacje zbiorowe:
Operacje zbiorowe w SQL pozwalają na wykonywanie operacji na zbiorach danych, takich jak suma, iloczyn, różnica. Pozwalają na porównywanie i łączenie danych z różnych tabel.

Przykład (SUM):

SELECT SUM(cena) FROM zamowienia;

## 7. Podzapytania:
Podzapytania pozwalają na osadzanie jednego zapytania wewnątrz innego zapytania. Mogą być używane do wykonywania bardziej złożonych operacji, które wymagają danych z innych tabel lub wyników innych zapytań.

Przykład:

SELECT imie, nazwisko FROM pracownicy WHERE id IN (SELECT pracownik_id FROM projekty WHERE status = 'aktywny');

## 8. Zapytania skorelowane:
Zapytania skorelowane są rodzajem podzapytań, w których zapytanie wewnętrzne odwołuje się do tabeli z zapytania zewnętrznego. Są używane do wykonywania bardziej zaawansowanych operacji, które wymagają dostępu do danych z obu zapytań.

Przykład:

SELECT nazwisko FROM pracownicy p WHERE EXISTS (SELECT * FROM projekty WHERE pracownik_id = p.id);
Rozumienie różnych aspektów języka SQL jest kluczowe dla efektywnego korzystania z baz danych. Poprawne stosowanie tych operacji pozwala na efektywne manipulowanie danymi i wykonywanie zaawansowanych operacji analitycznych.


# 6.
# DB-DML,DDL,dcl.tcl
Języki SQL
DDL-data definicion language         DML-data modification language         TCL         DQL             DCL 
create                              insert                                  commit     select from      grant
drop                                update                                  rollback                    revolk
alter                               delete
truncate


# KOLEJNOSC WYKONYWANIA DZIAŁAŃ W SQL
SELECT...FROM...
JOIN...
WHERE...
GROUP BY...
HAVING...
ORDER BY...
# RODZAJE DANYCH
INT --liczby całkowite

NUMERIC -- liczby dziesietne o stałej precyzji, np. pieniądzie

FLOAT --liczby zmiennoprzecinkowe

CHAR(n) --łańcuch o stałej liczbie znaków n

VARCHAR() --łańcuch o zmiennej liczbie znaków n

TEXT -- reprezentuje długie łańcuchy znaków no. teksty,opisy,artykuły

DATE -- data YYYY-MM-DD

TIME -- czas HH:MM:SS

DATETIME -- data i czas YYYY-MM-DD HH:MM:SS

BOOL --wartości logiczne TRUE/FALSE

BINARY --dane binarne tj. pliki,obrazy


# TWORZENIE BAZY DANYCH
CREATE DATABASE Nazwa_Bazy;

# TWORZENIE TABELI
CREATE TABLE NazwaTabeli;

CREATE TABLE Authors(
author_id INT PRIMARY KEY IDENTITY (1,1), -- id autoinkrementacja od 1 co 1
surename VARCHAR(50) NOT NULL,
name VARCHAR(50) NOT NULL,
biography NTEXT,
username VARCHAR(50)
);

# ALTER TABLE
## Dodawanie kolumny:
ALTER TABLE Production.Product
ADD NewColumn INT;

## Usuwanie kolumny:
ALTER TABLE Production.Product
DROP COLUMN ReorderPoint;

## Zmiana typu danych kolumny:
ALTER TABLE Sales.SalesOrderDetail
ALTER COLUMN OrderQty SMALLINT;

## Zmiana nazwy kolumny:
ALTER TABLE HumanResources.Employee
RENAME COLUMN NationalIDNumber TO EmployeeID;

## Dodawanie ograniczeń (constraint):
ALTER TABLE Person.Address
ADD CONSTRAINT CHK_PostalCode CHECK (LEN(PostalCode) = 5);

## Usuwanie ograniczeń (constraint):
ALTER TABLE Sales.SalesOrderHeader
DROP CONSTRAINT FK_SalesOrderHeader_Address_BillTo_AddressID;

## Zmiana nazwy tabeli:
ALTER TABLE Production.ProductModel
RENAME TO ProductModelNew;

## Dodawanie klucza obcego:
ALTER TABLE Production.BillOfMaterials
ADD CONSTRAINT FK_BillOfMaterials_Product_ProductID FOREIGN KEY (ProductAssemblyID) REFERENCES Production.Product(ProductID);

## Usuwanie klucza obcego:
ALTER TABLE Production.BillOfMaterials
DROP CONSTRAINT FK_BillOfMaterials_Product_ProductID;

## Dodawanie indeksu:
CREATE INDEX IX_Product_ProductNumber
ON Production.Product(ProductNumber);

## Usuwanie indeksu:
DROP INDEX IX_Product_ProductNumber
ON Production.Product;

# DROP
DROP TABLE nazwaTabeli  --usuwa tabele
DROB DATABASE nazwaBazy --usuwa baze
DROP VIEW HumanResources.vEmployee; -- usuwa widok z bazy
-- usuwanie klucza obcego
ALTER TABLE Production.BillOfMaterials
DROP CONSTRAINT FK_NazwaKluczaObcego

# TRUNCATE
TRUNCATE TABLE Production.Product; --usuwa wszystkie dane, wiersze z tabeli, bez tworzenia logów

# DELETE
DELETE FROM Production.Product; --usuwanie wszystkich wierszy, danych z tabeli

# RENAME
EXEC sp_rename 'Production.ProductPhoto', 'ProductImage';  -- zmienia nazwe tabeli
EXEC sp_rename 'Production.Product.ProductNumber', 'ProductCode', 'COLUMN'; --zmienia nazwe kolumny

# WHERE
SELECT * FROM Customers
WHERE Country = 'USA';

# WIDOKI
--tworzenie widoku
CREATE VIEW NazwaWidoku AS
SELECT klumna1,kolumna2,kolumna3
FROM tabela
WHERE warunek

SELECT * FROM NazwaWidoku; --odwołanie się do widoku

DROP VIEW NazwaWidoku; --usuwanie widoku

# KLUCZ OBCY
-- Dodawanie klucza obcego:
ALTER TABLE Production.BillOfMaterials
ADD CONSTRAINT FK_NazwaKluczaObcego FOREIGN KEY (ProductAssemblyID) REFERENCES Production.Product(ProductID);

--Usuwanie klucza obcego:
ALTER TABLE Production.BillOfMaterials
DROP CONSTRAINT FK_NazwaKluczaObcego;

-- klucz obcy podczas tworzenia tabeli
CREATE TABLE Notifications(
notification_id INT PRIMARY KEY IDENTITY (1,1),
notification_type VARCHAR(50),
extension_id INT,
date DATETIME,
content VARCHAR(255),
user_id INT,
FOREIGN KEY (extension_id) REFERENCES Extensions(extension_id),
FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

# SELECT
SELECT * FROM Nazwa_Tabeli;

SELECT Nazwa_Kolumny1, Nazwa_Kolumny2 FROM Nazwa_Tabeli;

# DISCINCT
-- wartości unikalne
SELECT DISTINCT
    PRODUCT.ProductID,
    PRODUCT.Name
FROM Production.Product PRODUCT
# INSERT
INSERT INTO tabela(kolumna1,kolumna2)
VALUES (wartosc1,wartosc2);

# UPDATE
UPDATE MojaTabela
SET Nazwa_Kolumna1=nowawartosc
WHERE ID=4;

# MERGE
--łączy dane z tabeli źródłowej do tabeli docelowej na podstawie warunku
MERGE INTO dbo.TargetTable AS target
USING dbo.SourceTable AS source
ON (target.ID = source.ID)
WHEN MATCHED THEN
    UPDATE SET target.Name = source.Name, target.Quantity = source.Quantity
WHEN NOT MATCHED THEN
    INSERT (ID, Name, Quantity)
    VALUES (source.ID, source.Name, source.Quantity);

# BULK INSERT
-- wstawia dane z pliku do tabeli, tabela nie moze istniec
BULK INSERT tabela
FROM 'sciezka do pliku'
WITH(
    FIELDTERMINATOR = ','
    ROWTERMINATOR = '\n\');

# SELECT INTO
--tworzy nowa tabele na podstawie zapytania select, np. tworzenie mniejszych tabel z wiekszej
SELECT kolumna1,kolumna2
INTO nowatabela
FROM staratabela

# JOINY
-- Inner join- tylko te które są odpowiedniki w 2 tabelach

-- Left join- wszystkie z lewej i z prawej, które są odpowiedniki w lewej tabeli

-- Right join- wszystkie z prawej i z lewej, które są odpowiedniki w prawej tabeli

-- Full join -wszystkie, te które są odpowiednikami i te które nie są z obydwu tabel


# GROUP BY
-- grupuje column1, column2 na podstawie column1, pozwala na uzycie funkcji agregujących
SELECT column1, column2
FROM table_name
GROUP BY column1;

# ORDER BY
ORDER BY Nazwa_kolumny asc; -- sortowanie rosnąco

ORDER BY Nazwa_kolumny desc; --sortowanie malejąco

# FUNKCJE AGREGUJĄCE
SUM(column) - oblicza sumę wartości w kolumnie.

AVG(column) - oblicza średnią wartości w kolumnie.

COUNT(column) - oblicza liczbę wierszy w danej grupie.

COUNT(*) OR COUNT(1) - oblicza liczbe wierszy w wykonaniu SELECT

MIN(column) - zwraca najmniejszą wartość w kolumnie.

MAX(column) - zwraca największą wartość w kolumnie

# FUNCKJE STRINGOWE - LEN(), LEFT,RIGHT,UPPER,LOWER
CONCAT(): Łączy dwa lub więcej ciągów znaków.
SELECT CONCAT(FirstName, ' ', LastName) AS FullName

LEN(): Zwraca długość ciągu znaków.
SELECT LEN(Description) AS DescriptionLength

SUBSTR(): Zwraca podciąg znaków z danego ciągu, na podstawie określonej pozycji i długości.
SELECT SUBSTR(Description, 1, 10) AS ShortDescription -- ciąg 10 znaków, start od 1 znaku ciągu znaków Description


UPPER() / LOWER(): Zamienia wszystkie litery w ciągu na duże lub małe.
SELECT UPPER(FirstName) AS UpperName
FROM Employees;

SELECT LOWER(LastName) AS LowerName
FROM Employees;


TRIM() / LTRIM() / RTRIM(): Usuwa białe znaki z początku i końca ciągu (TRIM), z lewej strony (LTRIM) lub z prawej strony (RTRIM).
SELECT (L/R)TRIM(Description) AS TrimmedDescription
FROM Products

REPLACE(): Zastępuje wszystkie wystąpienia określonego ciągu podciągiem.
REPLACE(Notes, 'old_text', 'new_text') -- zamienia w kolumnie Notes, old_text na new_text

LEFT() / RIGHT(): Zwraca określoną liczbę znaków z lewej (LEFT) lub prawej (RIGHT) strony ciągu
SELECT RIGHT(Description, 15) AS RightPart --zwraca 15 znaków z prawej strony

# FUNCKJE NUMERYCZNE
--SUM(): Służy do sumowania wartości w określonych kolumnach.
SELECT SUM(column_name) FROM table_name;

--AVG(): Oblicza średnią wartość w określonych kolumnach.
SELECT AVG(column_name) FROM table_name;

--COUNT(): Zlicza liczbę wierszy w wyniku zapytania.
SELECT COUNT(column_name) FROM table_name;

--MIN(): Zwraca najmniejszą wartość w określonych kolumnach.
SELECT MIN(column_name) FROM table_name;

--MAX(): Zwraca największą wartość w określonych kolumnach.
SELECT MAX(column_name) FROM table_name;

--ROUND(): Zaokrągla wartość do określonej liczby miejsc po przecinku.
SELECT ROUND(column_name, 2) FROM table_name;

--ABS(): Zwraca wartość bezwzględną liczby.
SELECT ABS(column_name) FROM table_name;

--POWER(): Podnosi liczbę do określonej potęgi.
SELECT POWER(column_name, 2) FROM table_name;

--SQRT(): Oblicza pierwiastek kwadratowy liczby.
SELECT SQRT(column_name) FROM table_name;

--CEILING(): Zaokrągla wartość do najbliższej liczby całkowitej w górę.
SELECT CEILING(column_name) FROM table_name;

--FLOOR(): Zaokrągla wartość do najbliższej liczby całkowitej w dół.
SELECT FLOOR(column_name) FROM table_name;

--SIGN(): Zwraca znak liczby (-1 dla wartości ujemnych, 0 dla zera, 1 dla wartości dodatnich).
SELECT SIGN(column_name) FROM table_name;

--RAND(): Zwraca pseudolosową liczbę zmiennoprzecinkową między 0 a 1.
SELECT RAND();

--LOG(): Oblicza logarytm naturalny z danej liczby.
SELECT LOG(column_name) FROM table_name;

--EXP(): Podnosi liczbę e do potęgi danej liczby.
SELECT EXP(column_name) FROM table_name;

--DEGREES(): Konwertuje wartość kątową wyrażoną w radianach na stopnie.
SELECT DEGREES(column_name) FROM table_name;

--RADIANS(): Konwertuje wartość kątową wyrażoną w stopniach na radiany.
SELECT RADIANS(column_name) FROM table_name;


# HAVING
--Pozwala to na stosowanie warunków do wyników agregacji, co umożliwia bardziej szczegółowe filtrowanie danych niż możliwe jest w samym WHERE
SELECT DepartmentID, COUNT(EmployeeID) AS NumberOfEmployees
FROM Employees
GROUP BY DepartmentID
HAVING COUNT(EmployeeID) > 5;

# PODZAPYTANIA
--Podzapytania w języku SQL to zapytania umieszczone wewnątrz innego zapytania.Stosowane w: WHERE,SELECT,FROM,HAVING
SELECT column1, column2
FROM table_name
WHERE column_name IN (SELECT column_name FROM another_table WHERE condition);

SELECT column1, COUNT(*) AS count
FROM table_name
GROUP BY column1
HAVING COUNT(*) > (SELECT AVG(count) FROM (SELECT COUNT(*) AS count FROM table_name GROUP BY column1) AS subquery);

# ZAPYTANIA SKORELOWANE
-- zapytanie skorelowane
SELECT CustomerID, CompanyName, 
(
	SELECT COUNT(OrderID) 
	FROM dbo.Orders as O
	WHERE o.CustomerID = C.CustomerID

) as LiczbaZlecen
FROM dbo.Customers as C

# ALIASY
SELECT Nazwa_Kolumny1 alias, Nazwa_Kolumny2 AS alias FROM Nazwa_Tabeli;


# UNION
--służy do łączenia wyników dwóch lub więcej zapytań SELECT w jedną listę wyników, bez duplikatów
SELECT column1, column2
FROM table1
WHERE condition1

UNION

SELECT column1, column2
FROM table2
WHERE condition2;


# UNION ALL
--służy do łączenia wyników dwóch lub więcej zapytań SELECT w jedną listę wyników, włącznie z duplikatami
SELECT column1, column2
FROM table1
WHERE condition1

UNION ALL

SELECT column1, column2
FROM table2
WHERE condition2;


# INTERSECT
--służy do łączenia wyników dwóch lub więcej zapytań SELECT w jedną listę wyników, które występują w obu zapytaniach
SELECT column1, column2
FROM table1
WHERE condition1

INTERSECT

SELECT column1, column2
FROM table2
WHERE condition2;


# EXCEPT
--wynik będzie zawierał tylko te wiersze, które występują w wyniku pierwszego zapytania, ale nie występują w wyniku drugiego zapytania.
SELECT column1, column2
FROM table1
WHERE condition1

EXCEPT

SELECT column1, column2
FROM table2
WHERE condition2;


# (NOT)EXISTS
--służy do sprawdzania istnienia wierszy w wyniku zapytania podrzędnego.
SELECT column1, column2
FROM table1
WHERE EXISTS (SELECT * FROM table2 WHERE condition);

# COALESCE
-- zwraca pierwsza niepusta wartosc z listy argumentow
select nazwa,
    coalesce(opis,'brak opisu') as opisproduktu
from produkty

# DATA I CZAS
-- biezaca data
select getdate() as aktualna_data_i_czas 

--dodaje okreslona wartosc do daty day/year itd
select dateadd(day,7,datazamowienia)as data from zamowienia

--zwraca roznice czasowa
select datediff(year,datauridzenia,getdate())as wiek from pracownicy

--year/moth/day - pobiera rok/miesiac/dzien
select year(datazatrudnienia) as rok from pracownicy

--mothname/datename - pobiera nazwe miesiaca/dzien tygodnia z daty
select datename(moth, data zatrudnienia) as nazwamiesiaca from pracownicy


# FUNKCJE LOGICZNE IF/CASE
SELECT IF(Salary > 50000, 'High', 'Low') AS SalaryCategory FROM Employees; -- jesli prawda to High jesli fałsz to Low

SELECT 
    CASE 
        WHEN Salary > 100000 THEN 'Very High
        WHEN Salary > 50000 THEN 'High'
        ELSE 'Low' 
    END AS SalaryCategory 
FROM Employees;


# CAST/CONVERT
--Funkcja CAST jest standardową funkcją w języku SQL, która umożliwia konwersję jednego typu danych na inny. 
SELECT CAST('123' AS INT);

SELECT CONVERT(INT, '123');


# RAW_NUMBER/RANK/DENSE_RANK
--Funkcja ROW_NUMBER() nadaje unikalny numer porządkowy każdemu wierszowi w wyniku zapytania, niezależnie od duplikatów.
SELECT 
    ROW_NUMBER() OVER (ORDER BY ColumnName) AS RowNumber,
    OtherColumn1, OtherColumn2
FROM TableName;

--Funkcja RANK() przypisuje wspólny numer porządkowy dla równych wartości, ale wiersze, które mają te same wartości, otrzymają ten sam numer porządkowy, a następnie numer porządkowy następny będzie pomijany.
SELECT 
    RANK() OVER (ORDER BY ColumnName) AS Rank,
    OtherColumn1, OtherColumn2
FROM TableName;

--Funkcja DENSE_RANK() przypisuje wspólny numer porządkowy dla równych wartości, ale numer porządkowy dla każdego wiersza zawsze zwiększa się o 1 w stosunku do poprzedniego. W przypadku duplikatów funkcja DENSE_RANK() nie pomija żadnych numerów porządkowych.
SELECT 
    DENSE_RANK() OVER (ORDER BY ColumnName) AS DenseRank,
    OtherColumn1, OtherColumn2
FROM TableName;

# IS NULL / IS NOT NULL
SELECT * FROM Employees
WHERE LastName IS NULL;

SELECT * FROM Products
WHERE Price IS NOT NULL;

# IN, BETWEEN, AND, OR, NOT, LIKE
SELECT * FROM Customers
WHERE Country = 'USA' AND City = 'New York';

SELECT * FROM Customers
WHERE Country = 'USA' OR Country = 'Canada';

SELECT * FROM Customers
WHERE NOT Country = 'USA';

SELECT * FROM Customers
WHERE Country IN ('USA', 'Canada', 'UK');

SELECT * FROM Orders
WHERE OrderDate BETWEEN '2022-01-01' AND '2022-12-31';

SELECT * FROM Products
WHERE ProductName LIKE 'Apple%';

# TWORZENIE WŁASNYCH TYPÓW
CREATE TYPE my_type FROM VARCHAR(30);

CREATE TYPE My_number FROM INT;

# INDEKSY
-- klastrowe- sortują i przechowują faktyczne dane w tabeli w określonym porządku.uporządkowana według wartości klucza głównego
CREATE CLUSTERED INDEX IX_ClusteredIndexName ON TableName (PrimaryKeyColumn);

-- nieklastrowe-Służą do przyspieszania wyszukiwania danych na podstawie innych kolumn niż klucz główny
CREATE NONCLUSTERED INDEX IX_NonClusteredIndexName ON TableName (IndexedColumn);

-- pełnotekstowe- stosowane do przyspieszania zapytań, które zawierają operatory pełnotekstowe
CREATE FULLTEXT INDEX IX_FullTextIndexName ON TableName (TextField);

-- przestrzenne- Indeksy przestrzenne są używane do obsługi danych przestrzennych, takich jak mapy, geometria, GPS
CREATE SPATIAL INDEX IX_SpatialIndexName ON TableName (GeometryColumn);

-- kolumnowe- dla dużej ilości danych, stosowane w bazach danych kolumnowych, gdzie dane są przechowywane w postaci kolumnowej, a nie wierszowej.
CREATE COLUMNSTORE INDEX IX_ColumnIndexName ON TableName (IndexedColumn1, IndexedColumn2);

-- unikalny Create UNIQUE INDEX, zapenia ze wszystkie wartosci są unikalne

Optymalizacja zapytań i stosowanie odpowiednich indeksów są kluczowymi elementami zarządzania wydajnością baz danych. Poprzez analizę planów wykonania zapytań i stosowanie różnych technik optymalizacji, można znacząco poprawić szybkość i efektywność dostępu do danych.


# Procedury
procedury składowane- to skrypty t-sql realizujace dowolne funkcje programistyczne
moga np importowac dane z pliku dokonujac weryfikacji, wykonywac okreslone czynnosci
moga przyjmowac parametry i zwracac zbiory wynikowe, dzieki nim mozemy zaszyc loike biznesowa na serwerze SQL tworzac strukture aplikacji

nie moga byc uzywane w kwerendach chociaz za ich pomoca mozna realizowac dostep do sanych

Wykonywanie procedury przez EXEC
## procedura dodająca nowe zamówienie:

CREATE PROCEDURE DodajNoweZamowienie
    @CustomerID INT,
    @OrderDate DATE,
    @ProductID INT,
    @Quantity INT
AS
BEGIN
    DECLARE @OrderID INT;

    INSERT INTO Sales.SalesOrderHeader (CustomerID, OrderDate)
    VALUES (@CustomerID, @OrderDate);

    SET @OrderID = SCOPE_IDENTITY();

    INSERT INTO Sales.SalesOrderDetail (SalesOrderID, ProductID, OrderQty)
    VALUES (@OrderID, @ProductID, @Quantity);
END;

WYKONANIE PROCEDURY: 

EXEC DodajNoweZamowienie 
    @CustomerID = 123, 
    @OrderDate = '2024-05-06', 
    @ProductID = 456, 
    @Quantity = 10;

## procedura pobierajaca szczegóły zamowienia

CREATE PROCEDURE Pobierzzamowienie
    @OrderID INT
AS
BEGIN
    SELECT sod.SalesOrderID, sod.ProductID, p.Name AS ProductName, sod.OrderQty
    FROM Sales.SalesOrderDetail sod
    INNER JOIN Production.Product p ON sod.ProductID = p.ProductID
    WHERE sod.SalesOrderID = @OrderID;
END;

## Procedura Aktualizujaca Dane Klienta
CREATE PROCEDURE AktualizujDane
    @CustomerID INT,
    @NewName NVARCHAR(50),
    @NewEmail NVARCHAR(100)
AS
BEGIN
    UPDATE Sales.Customer
    SET Name=@NewName,
        Email=@NewEmail
    WHERE CustomerID = @CustomerID
END;
# Funkcje

funckje skalarne-> zwracaja jednoelementowy wynik, mozemy uzyc jej w select lub where

FUNKCJA POBIERAJACA ILOSC ZAMOWIEN KLIENTA
CREATE FUNCTION Pobierzilosczamklienta
(
    @CustomerID INT
)
RETURNS INT
AS
BEGIN
    DECLARE @OrderCount INT;

    SELECR @OrderCount = COUNT(*)
    FROM Sales.SalesOrderHeader
    WHERE CustomerID= @CustomerID;

    RETURN @OrderCount;
END;


FUNKCJA OBLICZAJACA WARTOSC ZAMOWIENIA
CREATE FUNCTION obliczwartosczamowianie
(
    @OrderID INT
)
RETURNS MONEY
AS
BEGIN
    DECLARE @TotalAmount INT;

    Select @TotalAmount = sum(UnitPrice*OrderQty)
    from Sales.SalesOrderDetail
    Where SalesOrderID = @OrderID;

    RETURN @TotalAmount;
END;



FUNKCJA KONWERTUJĄCA DATE
CREATE FUNCTION convertdate
(
    @DateIn INT
)
RETURNS DATE
AS
BEGIN
    DECLARE @DateOut DATE;

    Select @DateOut = CONVERT(DATE, CONVERT(VARCHAR(8),@DateIn),112)

    RETURN @DateOut;
END;

# Funcje tabelaryczne
FUNKCJE TABELARYCZNE- zwracaja zbior elementow mozna uzywac w from
F-cja tabelaryczna pobierajaca produkty z kategorii

Create function Pobierzproduktyzkategorii
(
    @CategoryID INT
)
RETURNS TABLE
AS
RETURN
(
    Select p.ProductID,p.Name as ProductName, p.Color, p.LisPrice
    FROM Production.Product p
    INNER JOIN Production.ProductSubcategoryps ON p.ProductSubcategoryID=ps.ProductSubcategoryID
    WHERE ps.ProductCategoryID = @CategoryID
);

# Triggery
TRIGGERY- wyzwalacze, moga byc uruchamiane na skutek : insert,update,delete. za ich pomoca mozemy sie logowac, czy kontrolowac wszelkie zmainy

CREATE TRIGGER nazwa_triggera
ON nazwa_tabeli
AFTER INSERT, UPDATE,DELETE
AS
BEGIN
    --ciało, na przyklad procedura
END;

AFTER Triggers wykonuja sie po zakonczeniu operacji

INSTEAD OFF Triggers -> wykonuje sie samoistnie


Trigger logujacy zmiany produktow

inseerted- insert update
deleted -  delete


CREATE TRIGGER LogowanieZmianProduktow
ON Production.Product
AFTER INSERT,UPDATE, DELETE
AS
BEGIN
    IF EXISTS (SELECT * FROM inserted) OR EXISTS (SELECT * FROM deleted)
    BEGIN
        INSERT INTO dbo.ProductionChangeLog (ChangeDate, Action)
        VALUES (GETDATE(),"Zmiana w tabeli produkt");
    END;
END;


TRIGGER AKTUALIZUJACY STAN MAGAZYNOWY PO WSTAWIENIU ZAMOWIENIA
CREATE TRIGGER Aktualizacjastanumagazynowaer
ON Sales.SalesOrderDetail
AFTER INSERT
AS
BEGIN
    UPDATE Production.ProductInventory
    SET Quantity = Quantity - i.OrderQty
    FROM Production.ProductInventory pi
    JOIN inserted i ON pi.ProductID = i.ProductID;
END;

TRIGGER SPRAWDZAJACY POPRAWNOSC DANYCH PO USUNIECIU ZAMOWIENIA

CREATE TRIGGER SprawdzaniePoprawnosciDanych
ON Sales.SalesOrderDetail
AFTER DELETE
AS
BEGIN
    IF EXISTS (SELECT * FROM Production.ProductInventory WHERE Quantity <0)
    BEGIN
        RAISERROR("blad",16,1)
        ROLLBACK TRANSACTION
    END;
END;


# Zaawansowanie funkcje SQL

## Funkcje okienkowe
Funkcje okna (ang. window functions lub analytic functions) w SQL to specjalne rodzaje funkcji, które pozwalają na wykonywanie obliczeń na zestawie wierszy z wyniku zapytania, przy zachowaniu relacji między wierszami. Są to funkcje, które pozwalają na realizację skomplikowanych operacji analitycznych i agregacyjnych w obrębie zbioru wynikowego zapytania, bez konieczności korzystania z podzapytań, samodzielnej obróbki wyniku czy tworzenia tymczasowych tabel czy widoków.

SELECT
    worker_id,
    department_name,
    salary,
    AVG(salary) OVER(PARTITION BY department_name ORDER BY salary) AS avg_salary
FROM
    sii.workers;

oblicza średnią pensję w obrębie każdego działu, zachowując porządek rosnący pensji. Dzięki temu, można zobaczyć, jak pensje pracowników w danym dziale porównują się do średniej w ich dziale.    

## Operatory ETL
ETL (Extract, Transform, Load) to proces, który jest kluczowy w przetwarzaniu danych, szczególnie w kontekście hurtowni danych i integracji danych z różnych źródeł.
1. Extract (Ekstrakcja)
W tym etapie dane są pobierane ze źródeł danych. Źródła te mogą być różnorodne, np. bazy danych, pliki CSV, systemy ERP, API, itp. Ekstrakcja danych jest pierwszym krokiem w procesie ETL, który ma na celu zebranie wszystkich niezbędnych danych do dalszego przetwarzania.
Źródła danych: RDBMS, NoSQL, pliki tekstowe, pliki CSV, XML, JSON, systemy ERP, systemy CRM, serwisy internetowe.
Narzędzia do ekstrakcji: SQL, NoSQL

2. Transform (Transformacja)
Transformacja to proces przekształcania danych do odpowiedniego formatu lub struktury, aby były one zgodne z wymaganiami docelowego systemu bądź analizy. Transformacja może obejmować wiele różnych operacji, takich jak czyszczenie danych, agregacja, normalizacja, denormalizacja, wzbogacenie danych oraz mapowanie między różnymi formatami danych.

3. Load (Ładowanie)
Ładowanie to ostatni etap, w którym przekształcone dane są umieszczane w docelowym systemie, takim jak hurtownia danych, baza danych, system analityczny lub inne miejsce przechowywania danych. Ładowanie danych może być wykonane w trybie wsadowym (batch processing) lub w czasie rzeczywistym (real-time processing).

Docelowe systemy: Hurtownie danych, systemy analityczne, bazy danych (RDBMS, NoSQL), chmury obliczeniowe.

Narzędzia ETL
Istnieje wiele narzędzi ETL, które wspierają proces ETL, zarówno open-source, jak i komercyjne. Niektóre z najpopularniejszych to:

Apache Nifi: Open-source narzędzie do automatyzacji przepływu danych.
Talend: Rozbudowane narzędzie ETL, dostępne zarówno w wersji open-source, jak i komercyjnej.
Informatica: Jedno z najpopularniejszych komercyjnych narzędzi ETL.
Microsoft SQL Server Integration Services (SSIS): Narzędzie ETL zawarte w Microsoft SQL Server.
Apache Airflow: Platforma do zarządzania przepływami pracy, często używana do procesów ETL.
Pentaho Data Integration (Kettle): Open-source narzędzie ETL.

## Zapytania rekursywne
Zapytania rekursywne w SQL Server (MSSQL) pozwalają na wykonywanie złożonych operacji na danych hierarchicznych. Najczęściej używa się ich do pracy z danymi reprezentującymi struktury drzewiaste, takie jak hierarchie pracowników, struktury katalogów, czy elementy BOM (Bill of Materials). W SQL Server zapytania rekursywne realizowane są przy użyciu CTE (Common Table Expressions).

Zapytanie rekursywne składa się z trzech części:

- CTE anchor member: jest to podstawowe zapytanie, które nie jest rekursywne.
- CTE recursive member: jest to zapytanie rekursywne, które odnosi się do CTE.
- Zapytanie końcowe, które łączy wyniki CTE.
# Przechowywanie danych i zarządzanie pamięci

## Organizacja danych na dysku
Organizacja danych na dysku
hierarchia obiektów:
-drzewo widoczne w Object Explorer

każda baza ma swoją strukture
jest zachowana w 2 plikach: pliku bazy (ROWS data)i pliku logu transakcyjnego(LOG)
można dodać własny plik do np. przeniesienia bazy danych
logi-każdy ruch , zapisu, update,delete ale nie odczytu

obiekty bazodanowe musza miec unikalna nazwe : nazwaserwera.nazwabazy.nazwaschematu.nazwaobiektu
minimalna nazwa to nazwaschematu.nazwaobiekty

Schemat: to warstwa zwiazana z zarzadzaniem bezpieczenstwem

jest to kontener w ktorym mozemy tworzyc tabele,funkcjie itd.

każda baza ma domyślny schemat

select SCHEMA_NAME() -> jaki jest domyslny schemat

Tabela-> poddstawowy obiekt w bazie

kolumns-strybuty opisujace elementy

klucze
ograniczenia
wyzwalacze
indeksy
statystyki

widok-> perspektywa to zapisana kweredna 
nazywane czesto wirtualną tabelą

rezultatem jest pewien zbior elementow

tylko na widokach zmaterializowanych mozna dodac indeks

sa sposobem na ukrywanie skomplikowanej struktury bazy danych

nie poprawiaja wydajnosci zapytan jesli nie utworzymy na nich indeksow

synominy to alternatyne nazwy obiektow tj tabale widoki funkcje procedury


Strony i alokacja przestrzeni:

Przestrzeń na dysku jest alokowana w formie stron, które są najmniejszymi jednostkami alokacji.

## Partycjonowanie danych
dane są podzielone na partycje, które można zarządzać o uzyskiwać do nich dostęp oddzielnie. Partycjonowanie może zwiększyć skalowalność, zmiejszyć stopnień rywalizacji o zasoby i zoptymalizować wydajność
może zapewnic dzielenie danych wg wzorca uzycia
mozliwosc skalowania, zmiejszenie stopnia rywalizacji o zasoby

ceL:
skalowalność
wydajnosc
poprawienie bezpieczenstwa
zapewnienie elastycznosci działania
dostosowywanie magazynu danych do sposobu uzycia
zwiekszenie dostępności

Projektowanie partycji
partycjonowanie poziome- dane maja ten sam schemat ale mogą być oddzielone np. rocznikami, alfabetycznie, ważne aby były równomiernie podzielone wg klucza. nie musza byc tego samego rozmiaru. Unikaj tworzenia gorących partycji 

partycjonowanie pionowe- izolacja danych, podzial tabeli na mniejsze tabele, bardziej uzytkowe, mniej uzytkowe, zmiejszenie kosztow operacji wejscia, wyjscia i wydajnosci. np. w jednej name, description w drugiej stan magazynowy cena. 

partycjonowanie funkcyjne- np. faktury agregacja zgodne ze sposobem uzycia w poszczegolnyhc kontekstach.oddzielenie danych odczytu i zapisu od danych tylko do odczytu


# Replikacja i backup

## strategie replikacji
Replikacja i kopiowanie i utrzymywanie danych w wielu bazach danych w celu poprawy dostepności, skalowalności i wydajności. Umożliwia synchronizacje danych pomiędzy różnymi serwerami i lokalizacjami


Replika transakcyjna:
propaguje zmiany danych z bazy publikacji do baz subskrybentów w sposób ciągły, niemal rzeczywisty
zastosowanie: tam gdzie ważna jest minimalna latencja w synchronizacji danych

latencja- opóźnienie w synchronizacji, komunikacji danych

proces: wstepne załadowanie migawki , ciągłe przesyłane zmian danych(wstawianie,aktualizowanie,usuwanie)

publisher---transaction--->subscriber


Replikacja migawkowa- raz na jakiś czas (snap shotowa)
przydatna do aplikacji gdzie aktualizacje danych są rzadkie i mniej istotne

Replikacja mieszana - najczesciej wykorzystywana, łączy cechy obu,
stosowana w sytuacjach gdzie wymagana jest rózna czestotliwosc aktualizacji danych

możliwosći i zastosowania replikacji:
wysok dostępność - dostepnosc nawet podczas awarii serwera
skalowalność0 rozlozenie obciazenia odczytu danych na wiele serwerów
migracja danych - przenoszenie samych pomiędzy serwerami lub centrami danych bez przestojów
zapasowa kopia danych - tworzenei kopii zapasowych w różnych lokalizacjach

Wady i zalety:
zalety: niska latencja, konsystencja danych w czasie rzeczywistym
wady: zlozonosc konfiguarcji, wieksze wymagania dostyczace zasobów

Migawkowa:
z: prosta konfiguracja, mnijesz wymagania zasobów
w: dane moga byc przestaezałe pomiędzy migawksami, niska czestotliwisc aktualizacji

Stworzenie replikacji transakcyjnej:
EXEC sp_replicationdboption
    @dbname='publikacjaDB',
    @optname=''publish',
    @value ='true'

## Bakup i odzyskiwanie danych
proces tworzenia kopii danych, które mogą być uzyte do przywrocenia oryginalu po utracie
odzyskiwanie danych to proces przywracabua tyh kopii do pierwotnej lokalizacji w przypadku awarii

baza->task-> backup-> pełen/różnicowy/logi

### cel:
zapewnienie bezpieczenstwa danych
minimalizacja czasu przestoju i utraty danych

### Backup pełny
kompletna baza danych
podstawa do innych typów danych
duży rozmiar i długi czas tworzenia
pełna kopia wszystkich danych

### backup różnicowy:
zawiera tylko zmiany dokonane od ostaniengo backupu pełnego
redukcja czasu i rozmiary backupu
mniejsze i szybsze w porównaniu do backup pełnego wymaga ostatniego backupy pełnego przywrócenia danych

### backup logów:
kopiuje wszystkie transakcjie dokonane od ostatniego backup dziennika
przywracanie danych do konkretnego punktu w czasie

### strategie backup:
plan w celu zapewnienia integralności i dostępności danych:
pełny cotydzień
różnicowe codziennie
transakcji co godzine

okresy retencji: czas przez który backupy są przechowywane przed ich usunięciem.
przykładL
backup pełny : 1 miesiac
roznicowe: 2 tygodnie
logi: 1 tydzien


### Disaster recovery
Disaster recovery to proces odzyskiwania danych i przywracania funkcjonalnosci systemow po awarii,
wskaxniki RTO i RPO:
RTO recovery time objective: maksymalny akceptowany czas,w którym systemy muszą zostać przywrócone po awarii
RPO Recovery Point Objective: Maksymalna ilość danych, które mogą zostać utracone mierzone w czasie

### Backup pełny:
backup database [nazwabazy]
to disk ='sciezka do pliku'
with format, medianame='nazwabazckupu'
name='nazwabackup';

### Backup roznicowy:
backup database [nazwabazy]
to disk ='sciezka do pliku'
with differentian, medianame='nazwabazckupu'
name='nazwabackup';

### Backup log:
backup log [nazwabazy]
to disk ='sciezka do pliku'
with  medianame='nazwabazckupu'
name='nazwabackup';

## Odzyskiwanie:

Restore database [nazwabazy]
from disk='sciezkapliku_full.back'
with norecovery; -- nie odzyskuje już

Restore database [nazwabazy]-- restore backupy differential
from disk='sciezkapliku_fiff.bak'
with norecovery;

Restore log [nazwabazy] --restore logów
from disk='sciezkapliku'
with recovery;


### tabele msdb
backupset- informacje o kazdym wykonanym backupie

backupmediafamily- info o mediach backupowych na ktorycj sa przechowywame backupy

backupfile- info o plikach wchodzących w skład backupu

### widoki msdb
backupfilegroup - info o grupach plików

backupmediaset

backupset

### procedury msdb

sp_addupdatabase

sp_backupdatabase

sp_restore_databse

sp_delete_backuphistory

# NoSQL i relacyjne bazy danych

## Relacyjne bazy danych (RDBMS)
-dane w wierszach i kolumnach
-tabele mają określony schemat

## Cechy:
-struktura tabelaryczne
-schematy danych 
-ACID dla spójności transakcji
-język SQL

## Przykłady:
-MySQL
-PostgreSQL
-Oracle Database
-Microsoft SQL Server

### - - - - - - - - - - - - - - - - 

## NoSQL (Not Only SQL)
-bardziej elastyczne
-łatwe skalowanie i elastyczne zarządznie różnorodnymi typami danych
-dane przechowywane w sposób niestrukturalizowany

## Cechy:
-elastyczna struktura danych
-skalowalność pozioma
-BASE dla spójności danych
-różnorodne modele przechowywania danych

## Przykłady:
-MongoDB (dokumentowe)
-Cassandra (szerokie kolumny)
-Redis (klucz-wartość)
-Neo4j (grafowe)
-CouchDB (dokumentowe)
-Amazon DynamoDB (klucz-wartość)

### ----------------------------------------------------------------

## Historia relacyjnych baz danych
lata 70. XX wieku
-1970 - artykuł Edgara F. Codda (pracownika IBM) z koncepcją relacyjnych baz danych
-1974 - prototypowa implementacja relacyjnej bazy danych stworzona przez IBM

lata 90. XX w.
-1995 - powstanie MySQL
-1996 - premiera PostGresa

## Historia baz danych NoSQL
koniec lat 90. XX w.
-1998 - powstanie pierwszej bazy
-2000

-2007 - wydanie CouchDB
-2008 - powstanie Apache Cassandra przez Facebooka
-2009 - premiera MongoDB
-2010 - powstaje termin "NoSQL"
-2010 - Apache HBase wydana jako część ekosystemu Apache Hadoop
-2011 - Redis zyskuje popularność

### ----------------------------------------------------------------

## Struktura danych
-tabele
-wiersze
-kolumny


-Dokumenty:

{
    "id": 1,
    "name": "Jan",
    "birthdate": "1990-01-01:,
    "address": {
        "street": "Kwiatka 1
        ...
    }
}


-Grafy:

(Jan)-[Przyjaciel]  ....??


-Klucz-wartość


-Szerokie kolumny

Row 1: {"ID": 1, "Imie": "Jan", "Nazwisko": "Kowalski"}
Row 2: {"ID": 1, "Imie": "Jan", "Nazwisko": "Kowalski", "Miasto": "Kraków"}

## Bazy relacyjne

## Zalety
-niezawodność
-spójność danych (ACID)
-złożone zapytanie (SQL) - skomplikowane operacje na danych, np. JOIN, GROUP BY

## Wady:
-mniejsza skalowalność 
-sztywność schematów
-koszty utrzymania (koszty licencji i konserwacji)


## NoSQL

## Zalety
-elastyczność
-skalowalność (pozioma)
-szybkie operacje na dużych zbiorach danych (analiza w czasie rzeczywistym, big data, aplikacje internetowe)

## Wady:
-mniejsza spójność (BASE)
-brak standaryzowanych języków zapytania
-trudniejsze zarządzanie złożonymi transakcjami

## Kiedy relacyjne bazy danych?:
-transakcje finansowe
-systemy zarządzania danymi
-aplikacje wymagające złożonych zapytań i analiz

## Kiedy bazy NoSQL?:
-aplikacje internetowe o dużej skali (e-commerce, social media)
-systemy analityczne i big data
-aplikacje z dynamicznie zmieniającymi się schematami danych


## Koszty infrastruktury

Serwery i skalowalność:
-Relacyjne bazy danych:
    -serwery: wysokie wymagania dotyczące sprzętu
    -skalowalność: pionowa skalowalność jest kosztowna i ograniczona fizycznie
-NoSQL:
    -serwery: możliwość użycia tańszego sprzętu
    -skalowalnośc: pozioma skalowalność jest bardziej efektywna kosztowo

Koszty licencji i wsparcia
-Relacyjne bazy danych:
    -licencje: wysokie koszty licencji dla mokercyjnych systemów 
    -wsparcie: kosztowne umowy wsparcia
-NoSQL:
    ??
    ??

Koszty operacyjne:
-Relacyjne bazy danych:
    -zarządznie: specjalistyczna wiedza i doświadczenie
    -konserwacja: regularne aktualizacje, optymalizacje
-NoSQL:
    -zarządznie: mniej specjalistyczna wiedza (choć czasem też jest potrzebna specjalistyczna)
    -konserwacja: mniejsza częstotliwość i koszt konserwacji

#----------------------------------------------------------------

## Bezpieczeństwo danych:
-kontrola dostępu
    -Role-Based Access Control (RBAC) - zarządzanie dostępem użytkowników na podts. ich ról
    -granularne uprawnienia - definiowanie szczegółowych uprawnień na poziomie tabel, wierszy, kolumn
-szyfrowanie
    -szyfrowanie w spoczynku (at rest) i tranzycie (in transit)
    -Transparent Data Encryption (TDE)
-audyt i logowanie
    -pełne śledzenie aktywności użytkowników i operacji na danych
    -generowanie szczegółowych logów dostępu i zmian w danych


## Narzędzia i technologie

-MySQL Workbench:
    -opis:
        -graficzne narzędzie do zarządzania bazą danych MySQL
        -umożliwia projektowanie, rozwijanie i administrowanie bazą danych
    -kluczowe funkcje:
        -projektowanie diagramów ER (Entity-Relationship)
        -tworzenie, edytowanie i zarządzanie sche,atami i tabelami
        -wykonywanie zapytań SQL, optymalizacja, debugownaie
        -migracja baz danych i tworzenie kopii zapasowych

-pgAdmin:

-MongoDB Compass:
    -wizualizacja struktury dokumentówi kolekcji
    -tworzenie, edytowanie i usuwanie elementów
    -wykonywanie zapytań agregacyjnych i filtrowanie danych
    -analiza wydajności i monitorowanie operacji na bazie

-Cassandra OpsCenter:

## Przyszłość baz danych

### Hybrydowe podejście: łączenie relacyjnych i NoSQL

-elastyczność i skalowalność NoSQL + spójność i złożone zapytania relacyjnych baz danych

Przykłady
-Polyglot Persistence
-NewSQL

Korzyści:
-elastyczność
-optymalizacja wydajności
-zgodność z regulacjami



### Nowe rozwiąznia:
-bazy NewSQL:
    -Google Spanner
    -CockroachDB
-sztuczna inteligencja i uczenie maszynowe


### Innowacje:
-Serverless Databases: bazy danych jako usługa (DBaaS)
    -Amazon Aurora Serverless, Google Firestore
-Blockchain Databases
    -BigchainDB, IBM Blockchain


### Korzyści:
-automatyzacja - redukacja kosztów i czasu, dzięki automatycznemu zarządzaniu i optymalizacji
-skalowalność i elastyczność
-bezpieczeństwo i integralność

# Big Data

Integracja z systemami CRM i ERP
CRM customer relatioship managment
ERP enterprise resource planning
umożliwia wymiane danych miedzy systemami

Integracja z crm pozwala na lepsze zarzadzanie relacjami z klientami a z erp na efektywne zarzadzanie zasobami przedsiebiorstwa

Integracja z Hadoop
umozliwia analize danych w konteksie transakcyjnuch

z Spark
do przetwarzenia danych w czasie rzeczywistym i analizy danych

z PolyBase 
do wykonywna zapytan mssql bezposrednio na danych przechoywanych w hadoop i

Zwiększona efektywnosc operacyjna
centralizacja i integracja z różnymi systemami 

Automatyzacja procesów raportowania i analizy danych


## ETL
Extract Transform Load
wydobycie, transformacja,ładowanie

Extract - polega na wydobywaniu danych z roznych zrodel

Transform- etap w kktorym dane sa przeksztalcane u przygotowywane do zaladowanie. Transformacja moze obejmowac czyszczenie danych, filtrowanie,agregacje,wzbogacanie, konwersje formatów

Load- Ostateczny etap w którym przetworzone dane są ładowane do docelowego systemu, w którym moze byc hurtownia danych, baza danych, system analityczny lub inne miejsce przechowywania danych


# PRZYSZŁOŚĆ BAZ DANYCH
## Trendy w rozwoju systemów DBMS:
Rozszerzanie funkcjonalności
Elastyczność i skalowalność
Cloud Computing
Bezpieczeństwo danych
## Relacyjne bazy danych a sztuczna inteligencja i uczenie maszynowe
Integracja z narzędziami BI i AI
Zastosowanie baz danych do zarządzania danymi sztucznej inteligencji
## Nowe wyzwania i możliwości
Big Data
Cyfryzacja biznesu
Kompatybilność z nowymi technologiami
Zastosowanie w różnych sektorach

#                                           ADMINISTRACJA

# TEORIA
Znaczenie bezpieczenstwa informacji:
kluczowe aspekty: pufnosc, integralnosc, dostepnosc danych
ryzyka i zagrozenia: naruszenia danych wyciek poufnych info, utrata danych, ataki SQL Injection
skutki naruszen bezpiecz: straty finansowe, szkody reputacyjne, konsekwencje prawne
przyklady z zycia: omówieke naruszenia danych w duzej firmie, pokazujace skutki braku odpowiednich zabezpieczen

Komponenty bezpieczenstwa:
autentykacja (Windows, SQL) i autoryzacja
szyfrowanie- TDE, SSL/TLS
zarzadzania audytemi i monitorowanie
zabezpieczenie przed SQL Incejction- stosowanie parametryzowanych zapytań i minimalizacja uprawnien(blokada root, praca na koncie wbudowanym(windows authentication), utworzenie uzytkownika i role: inne pod aplikacje inne pod administracje, walidacja danych wejsciowych)
sanitacja zapytan- okreslenie z jakich znakow moze skladac sie dane wejsciowe

Definicja bezpieczenstwa- ochrona przed nieautoryzowwanym dostepem
Wycieki danych przyczyny: ataki, bledy konfiguracji systemow, niewlasciwe zarzadzanie uprawnieniami
Metody ochrony: szyfrowanie danych, polityka bezpieczenstwa, audyty bezpieczenstwa i tety penetracyjne

naruszenie integralnosci danych
ryzyka: bledne decyzje

ochrona: kontrola dostepu, autoryzacja wieloskladnikowa

Praktyki:
aktualizacje i łatki bezpieczenstwa
minimalizacja uprawnien
szyfrowanie i zarzadzanie kluczami
regularne audyty i monitorowanie zdarzen w systemie baz danych

Autentykacja userów:
Windows uwierzytelnianie:
uzywa kont windows, zalety: bezpieczenstwo,zarzadzanie,mniej hasla, kiedy? idealny w korporacjach z centralnym zarzadzaniem uzytkownikami i zasobami

SQL server uwierzytelnianie:
uzywa login i haslo. nie zalezy od kont sys oper.
zalety: elastycznosc-mozliwosc dostepow z sys niezitegrowalnych z windows, niezaleznosc- niewymaga kont windows,obsluga starszych aplikacji, obsluga zmieszanych sys oper
kiedy? w rozporszonych i heterogenicznych srodowiskach gdzie nie wszystkie systemy klientow sa zintegrowane z Acrive Directory
wady: login i haslo jest w plain text,nie korzysta z protokołu bezpieczenstwa Kerberos

## przejscie z uwierzytelnienia windows na sql server[login,haslo](sa,pw)
security-logins-sa-properties-sql server authentication-ustaw haslo-status-zmien login na enabled-restart

Uwierzytelnienie:
Login: za kogo podajemy sie w systemie
Hasło: tajny ciag znakow znany tylko przez nas

Jak sie zabezpieczyc?
hashowanie hasel, szyfrowanie danych,uzywanie bezpiecznych połączen tj https

Autoryzacja i zarzadzanie rolami
Uprawnienia na poziomie serwera, uprawnienia na poziomie bazy danych
Przyznawanie uprawnien
GRANT SELECT ON SCHEMA ::HumanResources TO role_HumanResourcesDept; - nadawanie uprawnien
REVOKE SELECT ON SCHEMA ::HumanResources TO role_HumanResourcesDept; - usuwanie uprawniem przyznanym za pomoca grant, ale nie blokuje mozliwosci ponmownego przyznania uprawnien

Deny- odmawia okreslonych uprawnien uzytkownikom lub rolom (np. zabronienie wejsc do danego schematu) - nawet jesli uzytkownik lub rola posiada uprawnienia przyznane przez grant. DENY dominuje

# TWORZENIE UŻYTKOWNIKÓW
## TWORZENIE NOWYCH LOGINÓW
CREATE LOGIN MyName WITH PASSWORD = 'YourPassword'; -- Tworzy nowe logowanie AdventureWorksLogin z hasłem

DROP LOGIN MyName --usuwanie loginu

## TWORZENIE UŻYTKOWNIKÓW Z LOGINEM
USE AdventureWorks;

CREATE USER UserWorks FOR LOGIN MyName; -- Tworzy użytkownika AdventureWorksUser dla nowego logowania AdventureWorksLogin

DROP USER MyName --usuwanie uzytkownikow

## TWORZENIE UZYTKOWNIKÓW BEZ LOGINU
CREATE USER UserWorks WITHOUT LOGIN; --utworzenie uzytkownika bez loginu





# DODAWANIE I USUWANIE UPRAWNIEŃ:

## -do pojedynczej tabeli:
USE AdventureWorks; -- Użyj bazy danych AdventureWorks

GRANT SELECT,UPDATE,INSERT ON Person.Address TO MyUser; -- Nadaj uprawnienia SELECT UPDATE INSERT

REVOKE SELECT,UPDATE,INSERT ON Person.Address FROM MyUser; -- Wycofaj uprawnienia SELECT UPDATE INSERT

## -do całego schematu:
USE AdventureWorks; -- Użyj bazy danych AdventureWorks

GRANT SELECT,UPDATE ON SCHEMA::HumanResources TO MyUser; -- Nadaj uprawnienia SELECT UPDATE dla schematu HumanResources użytkownikowi MyUser

REVOKE SELECT,UPDATE ON SCHEMA::HumanResources FROM MyUser; -- Wycofaj uprawnienia SELECT UPDATE dla schematu HumanResources użytkownikowi MyUser

## -do całej bazy danych:
USE AdventureWorks; -- Użyj bazy danych AdventureWorks

GRANT SELECT ON DATABASE::AdventureWorks TO MyUser; -- Nadaj uprawnienia SELECT dla całej bazy danych AdventureWorks użytkownikowi MyUser

REVOKE SELECT ON DATABASE::AdventureWorks FROM MyUser; -- Wycofaj uprawnienia SELECT dla całej bazy danych AdventureWorks użytkownikowi MyUser



# TWORZENIE I DODAWANIE RÓL

USE AdventureWorks; -- Użyj bazy danych AdventureWorks

CREATE ROLE SalesRole; -- Tworzy nową rolę o nazwie SalesRole

GRANT SELECT,INSERT,UPDATE,DELETE ON SCHEMA::Sales TO SalesRole; --dodanie uprawnien do roli

ALTER ROLE SalesRole ADD MEMBER UserWorks; -- Dodaje użytkownika do roli SalesRole

ALTER ROLE SalesRole DROP MEMBER UserWorks; -- Usuwa użytkownika do roli SalesRole

DROP ROLE SalesRole -- usuwanie roli

# ROLE  - PODSTAWOWE
## ROLE SYSTEMOWE
sysadmin: Użytkownicy w tej roli mają pełny dostęp do wszystkich zasobów i funkcji serwera SQL.

serveradmin: Zarządza konfiguracją serwera i jego ustawieniami.

securityadmin: Zarządza logowaniami oraz uprawnieniami na poziomie serwera i baz danych.

processadmin: Zarządza procesami działającymi na serwerze.

setupadmin: Zarządza konfiguracją linkowanych serwerów oraz serwisów SQL Server Agent.

bulkadmin: Pozwala na wykonywanie operacji masowego ładowania danych (bulk insert).

diskadmin: Zarządza plikami i dyskami używanymi przez serwer SQL.

dbcreator: Umożliwia tworzenie, zmienianie, usuwanie oraz przywracanie baz danych.

public: Wszyscy użytkownicy automatycznie należą do tej roli, ale nie mają żadnych specjalnych uprawnień.

## ROLE BAZOWE
db_owner: Pełny dostęp do bazy danych, możliwość wykonywania wszystkich operacji.

db_securityadmin: Zarządza uprawnieniami w bazie danych.

db_accessadmin: Zarządza dostępem użytkowników do bazy danych.

db_backupoperator: Wykonuje operacje tworzenia kopii zapasowych i odtwarzania bazy danych.

db_ddladmin: Może wykonywać wszystkie polecenia Data Definition Language (DDL).

db_datawriter: Może wstawiać, aktualizować i usuwać dane w wszystkich tabelach.

db_datareader: Może odczytywać wszystkie dane w tabelach bazy danych.

db_denydatawriter: Zabrania wstawiania, aktualizowania i usuwania danych w tabelach.

db_denydatareader: Zabrania odczytywania danych w tabelach.

# DODAWANIE RÓL SYSTEMOWYCH

ALTER ROLE db_datareader ADD MEMBER UserWorks; -- Dodaje użytkownika do roli db_datareade

ALTER ROLE db_datareader DROP MEMBER UserWorks; -- Usuwa użytkownika do roli db_datareade



# OGRANICZENIE UPRAWNIEŃ ZA POMOCĄ DENY

## na tabeli
DENY INSERT,UPDATE ON HumanResources.Employee TO UserWorks;

DENY ALL ON HumanResources.Employee TO UserWorks;

## na schemacie
DENY INSERT,UPDATE ON SCHEMA::HumanResources TO UserWorks;

DENY ALL ON SCHEMA::HumanResources TO UserWorks;

## na bazie
use AdventureWorks2019;

DENY DELETE,DROP TO UserWorks;

# PRZEŁĄCZENIE POMIĘDZY UŻYTKOWNIKAMI
EXECUTE AS USER =  'UserWorks' ; -- przełączenie na użytkownika UserWorks

REVERT; -- powrót na poprzedni User

## Wyświetlenie aktualnego użytkownika
SELECT USER_NAME();

## Uprawnienia na poziomie serwera

VIEW SERVER STATE -wyswietlanie ogolnego stanu serwera np. SELECT * FROM sys.dm_os_perfrormance_counters;

ALTER SERVER ROLE - modyfikuje role serwera np. ALTER SERVER ROLE sysadmin ADD MEMBER mylogin

CONTROL SERVER - pelna kontrola nad serwerem

ALTER ANY LOGIN - modyfikacja logowania dowolnego

VIEW ANY DEFINITION -pozwala na wyswietlenie definicji wszystkich obiektow na serwerze, niezaleznie od bazy danych

## Zapobieganie przed SQL Injection
SQL. Wstrzyknięcie zazwyczaj możliwe jest z jednego powodu – braku odpowiedniego sprawdzenia (walidacji) parametru przekazanego przez użytkownika. Taki parametr, gdy mamy do czynienia z SQL injection, często przekazywany jest bezpośrednio do zapytania SQL.SQL Injection - wstrzykiwanie złośliwych instrukcji SQL do zapytać -> nieautoryzowany dotęp do danych

W zależności od sytuacji możemy mieć do czynienia z:
- nieautoryzowanym dostępem w trybie odczytu lub zapisu do całej bazy danych,
- możliwością ominięcia mechanizmu uwierzytelnienia,
- możliwością odczytania wybranych plików (system operacyjny, na którym pracuje baza danych),
- możliwością tworzenia plików w systemie operacyjnym, na którym pracuje baza,
- możliwością wykonania kodu w systemie operacyjnym (uprawnienia użytkownika, na którym pracuje baza lub web serwer – w przypadku aplikacji webowych)

W jaki sposób się ochronić?
W odpowiedni sposób weryfikować zmienne przekazywane do użytkownika do aplikacji.parametryzowane zapytania -walidacja i sanitacja danych wejściowych -minimalizacja uprawnień użytkowników bazy danych


# AUTENTYKACJA
1. Autoryzacja Windows (Windows Authentication)
Korzysta z konta użytkownika systemu Windows do logowania się do SQL Server.
Autoryzacja jest zarządzana przez kontroler domeny Windows.
Najbardziej bezpieczna i zalecana metoda, zwłaszcza w środowiskach korporacyjnych.

2. Autoryzacja SQL Server (SQL Server Authentication)
Umożliwia logowanie się do SQL Server za pomocą kont SQL Server, które są zarządzane wewnętrznie przez SQL Server.
Użytkownicy mają osobne loginy i hasła, niezależnie od kont Windows.

3. Mixed Mode (Mieszana autoryzacja)
Łączy oba powyższe tryby autoryzacji.
SQL Server akceptuje zarówno loginy Windows, jak i SQL Server.

4. Autoryzacja za pomocą certyfikatów i kluczy (Certificate and Key Authentication)
Wykorzystanie certyfikatów SSL do uwierzytelniania połączeń z SQL Server.

5. Autoryzacja za pomocą OAuth
Korzystanie z protokołu OAuth do autoryzacji w SQL Server, szczególnie przy połączeniach z zewnętrznymi usługami lub aplikacjami webowymi.

# ZABEZPIECZENIA PRZED SQL INJECTON
SQL Injection to atak, który pozwala na wstrzyknięcie złośliwego kodu SQL do zapytań wykonywanych przez aplikację. Może prowadzić do kradzieży danych, usunięcia danych lub uzyskania nieautoryzowanego dostępu.

## Techniki zabezpieczające przed SQL Injection:

Używanie parametrów w zapytaniach

Używanie procedur składowanych

Weryfikacja i filtrowanie danych wejściowych

Ograniczanie uprawnień

Używanie ORM (Object-Relational Mapping)





















































