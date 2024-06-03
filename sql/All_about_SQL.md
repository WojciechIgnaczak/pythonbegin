# 1. Wprowadzenie do Systemów Baz Danych (DBMS):
Systemy baz danych (DBMS) są to narzędzia, które umożliwiają przechowywanie, zarządzanie i manipulowanie danymi. Są one wykorzystywane w różnych dziedzinach, takich jak biznes, nauka, administracja publiczna itp. DBMS umożliwiają użytkownikom tworzenie, aktualizowanie, odczytywanie i usuwanie danych w sposób zorganizowany i efektywny.

Relacyjny Model Danych:
Relacyjny model danych jest jednym z najbardziej popularnych modeli baz danych. W modelu tym dane są przechowywane w postaci tabel, gdzie każda tabela składa się z wierszy (rekordów) i kolumn (pól). Relacje między tabelami są reprezentowane za pomocą kluczy obcych i kluczy głównych. Model relacyjny jest elastyczny i umożliwia łatwe wykonywanie zapytań.

Inne Modele Baz Danych:
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
COMMIT;

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

# MASKOWANIE
-- dodawanie maski
ALTER TABLE nazwaTabeli
ALTER COLUMN nazwaKolumny ADD MASKED WITH (FUNCION= 'default()') --maskowanie kolumny 123456789-> xxxx

ALTER TABLE nazwaTabeli
ALTER COLUMN nazwaKolumny ADD MASKED WITH (FUNCION= 'email()') -- jankowalski@gmail.com -> XXX@XXXX.com

ALTER TABLE nazwaTabeli
ALTER COLUMN nazwaKolumny ADD MASKED WITH (FUNCION= 'random(100,10000)') --zastępuje maskowaną komórke liczbami od 100 do 10000, 987654321-> 909

ALTER TABLE nazwaTabeli
ALTER COLUMN nazwaKolumny ADD MASKED WITH (FUNCION= 'partian(3,"X",1)')-- zastępuje komórke tak, że widać 3 piersze znaki i jeden ostatni, a    reszte zastępuje "X"


-- usuwanie maski
ALTER TABLE nazwaTabeli
ALTER COLUMN nazwaKolumny DROP MASKED

-- uprawnienia do odmaskowania danych
GRANT UNMASK  ON nazwaTabeli(nazwaKolumny) FROM nazwaBazyDanych TO nazwaUsera

REVOKE UNMASK ON nazwaTabeli(nazwaKolumny) FROM nazwaBazyDanych TO nazwaUsera
# Procedury

# Funkcje

# Funcje tabelaryczne

# Triggery

# Zaawansowanie funkcje SQL

## Funkcje okienkowe

## Operatory ETL

## Zapytania rekursywne

# Przechowywanie danych i zarządzanie pamięci

## Organizacja danych na dysku

## Partycjonowanie danych

# Replikacja i backup

## strategie replikacji

## Bakup i odzyskiwanie danych

## Narzędzia i techniki backupu

# NoSQL i relacyjne bazy danych

## Porównanie modeli NoSQL i relacyjnych

## Kiedy używać relacyjnych, a kiedy NoSQL

## Systemy NoSQL

# Big Data
# ################################################################################################################################################
#                                           ADMINISTRACJA

# TEORIA

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

# ROLE SYSTEMOWE - PODSTAWOWE
db_owner - pelne uprawnienia

db_datareader -tylko do odczytu, SELECT

db_datawriter -do wpisywanie, alter,drop,insert

db_ddladmin -uprawnienia DDL (data definition language)CREATE,ALTER,DROP,TRUNCATE,GRANT,REVOLKE

db_securityadmin -tworzenie i zarządzanie loginami i rolami, przyracanie haseł

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

