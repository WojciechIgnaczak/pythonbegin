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