#                                              PROCEDURY
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


#                                               FUNKCJE

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

SELECT dbo.Pobierzilosczamklienta(20155) AS Ilosc_zamowienia;


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

#                                           FUNKCJE TABELARYCZNE
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

#                                               TRIGGERY
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


#                                          ZAAWANSOWANE FUNKCJE SQL

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

#                               PRZECHOWYWANIE DANYCH I ZARZĄDZANIE PAMIĘCIĄ

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

### Projektowanie partycji:

#### partycjonowanie poziome- dane maja ten sam schemat ale mogą być oddzielone np. rocznikami, alfabetycznie, ważne aby były równomiernie podzielone wg klucza. nie musza byc tego samego rozmiaru. Unikaj tworzenia gorących partycji.Partycjonowanie poziome polega na podzieleniu tabeli na mniejsze, bardziej zarządzalne części, gdzie każda partycja zawiera ten sam zestaw kolumn, ale różne wiersze. W MSSQL partycjonowanie poziome jest realizowane za pomocą partycji tabel.

Utworzenie funkcji partycjonowania:
CREATE PARTITION FUNCTION MyPartitionFunction (INT)
AS RANGE LEFT FOR VALUES (1000, 2000, 3000);

Utworzenie schematu partycjonowania:
CREATE PARTITION SCHEME MyPartitionScheme
AS PARTITION MyPartitionFunction
TO ([PRIMARY], [PRIMARY], [PRIMARY], [PRIMARY]);

Utworzenie tabeli z partycjonowaniem:
CREATE TABLE MyPartitionedTable (
    Id INT PRIMARY KEY,
    Name NVARCHAR(50)
) ON MyPartitionScheme(Id);

INSERT INTO MyPartitionedTable
(Name)

SELECT Name
FROM MyTable

#### partycjonowanie pionowe- izolacja danych, podzial tabeli na mniejsze tabele, bardziej uzytkowe, mniej uzytkowe, zmiejszenie kosztow operacji wejscia, wyjscia i wydajnosci. np. w jednej name, description w drugiej stan magazynowy cena. 
Oryginalna tabela:
CREATE TABLE OriginalTable (
    Id INT PRIMARY KEY,
    Name NVARCHAR(50),
    Address NVARCHAR(100),
    Phone NVARCHAR(15)
);

Podzielenie tabeli na dwie mniejsze:

CREATE TABLE BasicInfo (
    Id INT PRIMARY KEY,
    Name NVARCHAR(50)
);

CREATE TABLE ContactInfo (
    Id INT PRIMARY KEY,
    Address NVARCHAR(100),
    Phone NVARCHAR(15),
    FOREIGN KEY (Id) REFERENCES BasicInfo(Id)
);


partycjonowanie funkcyjne- np. faktury agregacja zgodne ze sposobem uzycia w poszczegolnyhc kontekstach.oddzielenie danych odczytu i zapisu od danych tylko do odczytu


#                                           REPLIKACJA I BACKUP

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

#                                       NoSQL I RELACYJNE BAZY DANYCH

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

#                                               BIG DATA

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


#                                           ADMINISTRACJA

## TEORIA
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

## TWORZENIE UŻYTKOWNIKÓW
## TWORZENIE NOWYCH LOGINÓW
CREATE LOGIN MyName WITH PASSWORD = 'YourPassword'; -- Tworzy nowe logowanie AdventureWorksLogin z hasłem

DROP LOGIN MyName --usuwanie loginu

## TWORZENIE UŻYTKOWNIKÓW Z LOGINEM
USE AdventureWorks;

CREATE USER UserWorks FOR LOGIN MyName; -- Tworzy użytkownika AdventureWorksUser dla nowego logowania AdventureWorksLogin

DROP USER MyName --usuwanie uzytkownikow

## TWORZENIE UZYTKOWNIKÓW BEZ LOGINU
CREATE USER UserWorks WITHOUT LOGIN; --utworzenie uzytkownika bez loginu


## DODAWANIE I USUWANIE UPRAWNIEŃ:

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



## TWORZENIE I DODAWANIE RÓL

USE AdventureWorks; -- Użyj bazy danych AdventureWorks

CREATE ROLE SalesRole; -- Tworzy nową rolę o nazwie SalesRole

GRANT SELECT,INSERT,UPDATE,DELETE ON SCHEMA::Sales TO SalesRole; --dodanie uprawnien do roli

ALTER ROLE SalesRole ADD MEMBER UserWorks; -- Dodaje użytkownika do roli SalesRole

ALTER ROLE SalesRole DROP MEMBER UserWorks; -- Usuwa użytkownika do roli SalesRole

DROP ROLE SalesRole -- usuwanie roli

## ROLE SYSTEMOWE - PODSTAWOWE
db_owner - pelne uprawnienia

db_datareader -tylko do odczytu, SELECT

db_datawriter -do wpisywanie, alter,drop,insert

db_ddladmin -uprawnienia DDL (data definition language)CREATE,ALTER,DROP,TRUNCATE,GRANT,REVOLKE

db_securityadmin -tworzenie i zarządzanie loginami i rolami, przyracanie haseł

## DODAWANIE RÓL SYSTEMOWYCH

ALTER ROLE db_datareader ADD MEMBER UserWorks; -- Dodaje użytkownika do roli db_datareade

ALTER ROLE db_datareader DROP MEMBER UserWorks; -- Usuwa użytkownika do roli db_datareade



## OGRANICZENIE UPRAWNIEŃ ZA POMOCĄ DENY

## na tabeli
DENY INSERT,UPDATE ON HumanResources.Employee TO UserWorks;

DENY ALL ON HumanResources.Employee TO UserWorks;

## na schemacie
DENY INSERT,UPDATE ON SCHEMA::HumanResources TO UserWorks;

DENY ALL ON SCHEMA::HumanResources TO UserWorks;

## na bazie
use AdventureWorks2019;

DENY DELETE,DROP TO UserWorks;

## PRZEŁĄCZENIE POMIĘDZY UŻYTKOWNIKAMI
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

