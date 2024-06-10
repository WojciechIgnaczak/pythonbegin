use AdventureWorks2016;

--Procedury składowane:

--        Stwórz procedurę, która przyjmuje parametry (imię, nazwisko, data zatrudnienia, dział) i dodaje nowego pracownika do tabeli Person.Person.
create procedure AddEmployee
	@firstname nvarchar(50),
	@lastname nvarchar(50),
	@hiredate date,
	@department nvarchar(50)
as
begin 
	insert into Person.Person (FirstName, LastName,HireDate,Department)
	values (@firstname, @lastname, @hiredate, @department)
end;

   --Procedura zmieniająca adres pracownika:
        --Stwórz procedurę, która przyjmuje ID pracownika i nowy adres, a następnie aktualizuje adres pracownika w tabeli HumanResources.EmployeeAddress.
create procedure changeadress
	@CustomerID int,
	@newadress nvarchar(50) 
as
begin
	update Person.Adress
	set Adress= @newadress
	where CustomerID = @CustomerID
end;

   -- Procedura wyliczająca roczne wynagrodzenie:
  --Stwórz procedurę, która przyjmuje ID pracownika i zwraca roczne wynagrodzenie pracownika na podstawie jego pensji miesięcznej.
create procedure YearSalary
	@EmpID int
as
begin
	declare @monthsalary money
	declare @yearsalary money
	
	select @monthsalary = Rate from HumanResources.EmployeePayHistory
	where BusinessEntityID= @EmpID
	
	set @yearsalary = @monthsalary *12

	select @yearsalary as Roczne_Wynagrodzenia

end;
-- procedura usuwajaca klienta z jego zamówieniami:
-- stworz procedure ktora usuwa klienta z bazy wraz z wszystkimi powiązanymi zamówieniami znajdującymi sie w sales.salesorderheader
create procedure deleteCustomer
	@CustomerID int
as
begin
	delete from Sales.SalesOrderHeader where CustomerID=@CustomerID
	delete from Sales.Customer where CustomerID=@CustomerID
end

--procedura generujaca raport dla okreslonego okres:
-- procedura ktora gneruje raport o sprzedazy dla okreslonego czasu, zwracając sume sprzedaży dla kazdego produktu w danym okresie
create procedure raportsprzedazy
	@start_date date
	@end_date date
as
begin
select sod.ProductID,pp.Name,sum(sod.UnitPrice) kasa from Sales.SalesOrderDetail sod
join Sales.SalesOrderHeader soh on soh.SalesOrderID =sod.SalesOrderID
inner join Production.Product pp on pp.ProductID =sod.ProductID
where soh.OrderDate between @start_date and @end_date
group by sod.ProductID,pp.Name
order by kasa desc
end

-- procedura analizująca stan magazynowy po dodaniu nowej dostawy:
--procedura ktora po dodaniu nowej dostawy aktualizuje stan magazynowy produktow w tabeli Production.ProductInventory
drop procedure aktstanmagz

create procedure aktstanmagz
	@ProductID int,
	@Quantity smallint,
	@locaction int
	as
begin
	update Production.ProductInventory
	set Quantity = @Quantity
	where ProductID= @ProductID and LocationID=@locaction
end

--Funkcje skalarne:

    --Funkcja obliczająca wiek pracownika:
      --  Stwórz funkcję, która przyjmuje datę urodzenia pracownika i zwraca jego wiek w latach.
create function ageemployee
(
@dateborn date
)
returns int
as
begin
	declare @age int
	set @age= DATEDIFF(YEAR,@dateborn,GETDATE())
	return @age
end;

   -- Funkcja sprawdzająca dostępność produktu:
    --    Stwórz funkcję, która przyjmuje ID produktu i zwraca 'Dostępny', jeśli produkt jest w magazynie, a 'Niedostępny', jeśli nie ma go w magazynie.
CREATE FUNCTION available
(
    @ProductID INT
)
RETURNS NVARCHAR(20)
AS
BEGIN
    DECLARE @availability NVARCHAR(20)

    IF EXISTS(SELECT * FROM Production.ProductInventory WHERE ProductID = @ProductID AND Quantity > 0)
        SET @availability = 'Dostepny'
    ELSE
        SET @availability = 'niedostepny'

    RETURN @availability
END;







--Triggery:

  --  Trigger sprawdzający maksymalną liczbę pracowników w dziale:
 --5   --    Stwórz trigger, który po próbie dodania nowego pracownika sprawdza, czy liczba pracowników w danym dziale nie przekracza ustalonej maksymalnej liczby.
create trigger newEmpl on HumanResources.Employee
after insert
as
begin
	declare @departmentID int
	declare @maxemp int
	select @departmentID=DepartmentID, @maxemp=MaxEmployees from HumanResources.Department
	where departmentID in (select departmentID from inserted)

	if (select count(*) from HumanResources.Employee where DepartmentID=@departmentID)>@maxemp
	begin
		raiserror('blad',16,1)
		rollback transaction
	end
end;



    --Trigger aktualizujący stan magazynowy po zmianie zamówienia:
      --  Stwórz trigger, który po zmianie zamówienia aktualizuje stan magazynowy produktów w tabeli Production.ProductInventory.
create trigger changeorder on Production.ProductInventory
after update
as
begin
	Update Production.ProductInventory
	set Quantity=Quantity- (select Quantity from deleted where ProductID = Production.ProductInventory.ProductID)
	where ProductID in (select ProductID from deleted)

	Update Production.ProductInventory
	set Quantity=Quantity + (select Quantity from inserted where ProductID = Production.ProductInventory.ProductID)
	where ProductID in (select ProductID from inserted)
end;


    --Trigger archiwizujący dane klientów:
      --  Stwórz trigger, który po usunięciu rekordu klienta z tabeli Sales.Customer, przenosi ten rekord do tabeli Sales.ArchivedCustomers w celu archiwizacj
	CREATE TABLE [Sales].[Customer](
	[CustomerID] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[PersonID] [int] NULL,
	[StoreID] [int] NULL,
	[TerritoryID] [int] NULL,
	[AccountNumber]  AS (isnull('AW'+[dbo].[ufnLeadingZeros]([CustomerID]),'')),
	[rowguid] [uniqueidentifier] ROWGUIDCOL  NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
)
create trigger archive on Sales.Customer
after delete
as
begin
	insert into Sales.ArchivedCustomers
	select * from deleted
end;


-- trigger automatycznie aktualizujacy date modyfikacji rekorduL
-- aktualizuje modyfikacje rekordu w tabeli humanresources.employee za kazdym razem gdy zostanie zmieniony jakikolwiek rekord
create trigger aktdata on HumanResources.Employee
after update
as
begin
	update HumanResources.Employee
	set ModifiedDate=getdate()
	where BusinessEntityID in (select BusinessEntityID from inserted) or  BusinessEntityID in (select BusinessEntityID from deleted)
end


-- trigger sprawdzajacy poprawnosc danych podczas dosawania nowego produktu no czy cena jest >0 , nazwa jest unikalnka
use AdventureWorks2019
go
create trigger poprawnoscdanych on Production.Product
after insert
as
begin
	declare @price money
	declare @name nvarchar(50)
	select @price= ListPrice, @name = Name from inserted
	IF EXISTS (SELECT Name FROM Production.Product WHERE Name = @name AND ProductID != (SELECT ProductID FROM inserted))
	begin
		rollback transaction
	end
	if @price >0
	begin
		rollback transaction
	end
end


-- partycjonowanie poziome
--plega na podziale tabeli na mniejsze podzbiory w oparciu o wrtosci pewnej kolumny

--utworz schemat partycjonowania dla tabeli sales.salesorderheader wg kolumny OrderDate
--stworz f-cje partycjonowania
--utworz nowa tabele partycjonowanie ktora bedzie przechowywac dane z salesorderheader
--przenies dane z oryginalnej tabeli do nowej partycjonowanej

CREATE PARTITION SalesOrderDatePF (datetime)
AS RANGE RIGHT FOR VALUES ('2010-01-01','2011-01-01','2012-01-01','2013-01-01');
--utworzenei funkcji partycjonowanej
CREATE PARTITION SCHEME SalesOrderDatePS
AS PARTITION SalesOrderDatePF
TO ([PRIMARY],[PRIMARY],[PRIMARY],[PRIMARY],[PRIMARY]);

--utworzenei nowej tabeli partycjonowanej
CREATE TABLE Sales.SalesOrderHeader_Partitioned
(
	[SalesOrderID] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[RevisionNumber] [tinyint] NOT NULL,
	[OrderDate] [datetime] NOT NULL,
	[DueDate] [datetime] NOT NULL,
	[ShipDate] [datetime] NULL,
	[Status] [tinyint] NOT NULL,
	[OnlineOrderFlag] [dbo].[Flag] NOT NULL,
	[SalesOrderNumber]  AS (isnull(N'SO'+CONVERT([nvarchar](23),[SalesOrderID]),N'*** ERROR ***')),
	[PurchaseOrderNumber] [dbo].[OrderNumber] NULL,
	[AccountNumber] [dbo].[AccountNumber] NULL,
	[CustomerID] [int] NOT NULL,
	[SalesPersonID] [int] NULL,
	[TerritoryID] [int] NULL,
	[BillToAddressID] [int] NOT NULL,
	[ShipToAddressID] [int] NOT NULL,
	[ShipMethodID] [int] NOT NULL,
	[CreditCardID] [int] NULL,
	[CreditCardApprovalCode] [varchar](15) NULL,
	[CurrencyRateID] [int] NULL,
	[SubTotal] [money] NOT NULL,
	[TaxAmt] [money] NOT NULL,
	[Freight] [money] NOT NULL,
	[TotalDue]  AS (isnull(([SubTotal]+[TaxAmt])+[Freight],(0))),
	[Comment] [nvarchar](128) NULL,
	[rowguid] [uniqueidentifier] ROWGUIDCOL  NOT NULL,
	[ModifiedDate] [datetime] NOT NULL,
 CONSTRAINT [PK_SalesOrderHeader_Partitioned] PRIMARY KEY CLUSTERED (SalesOrderID, OrderDate)
) ON SalesOrderDatePS(OrderDate);

--przeniesienie danych do nowej tabeli partycjonowanej
INSERT INTO Sales.PK_SalesOrderHeader_Partitioned
([RevisionNumber]
,[OrderDate]
,[DueDate]
,[ShipDate]
,[Status]
,[OnlineOrderFlag]
,[PurchaseOrderNumber]
,[AccountNumber]
,[CustomerID]
,[SalesPersonID]
,[TerritoryID]
,[BillToAddressID]
,[ShipToAddressID]
,[ShipMethodID]
,[CreditCardID]
,[CreditCardApprovalCode]
,[CurrencyRateID]
,[SubTotal]
,[TaxAmt]
,[Freight]
,[Comment]
,[rowguid]
,[ModifiedDate])

SELECT [SalesOrderID]
,[RevisionNumber]
,[OrderDate]
,[DueDate]
,[ShipDate]
,[Status]
,[OnlineOrderFlag]
,[SalesOrderNumber]
,[PurchaseOrderNumber]
,[AccountNumber]
,[CustomerID]
 ,[SalesPersonID]
,[TerritoryID]
,[BillToAddressID]
,[ShipToAddressID]
,[ShipMethodID]
,[CreditCardID]
,[CreditCardApprovalCode]
,[CurrencyRateID]
,[SubTotal]
,[TaxAmt]
,[Freight]
,[TotalDue]
,[Comment]
,[rowguid]
,[ModifiedDate]
FROM [Sales].[SalesOrderHeader]











-- Partycjonowanie pionowe
-- podzial na mniejsze tabele w oparciu o grupy kolumn . podzial tabeli Person.person na dwie tabele w oparciu o grupy kolumn
--TRESC 
--utworz dwie nowe tabele, person.person_part1 i person.person_part2 aby przechowywac rozne grupy kolumn z tabeli person.person
--przenies odpowiednie dane z oryginalnej tabeli do nowych partycjonowanych pionowo
-- utworz widok person.person  łączocy obie partycjonowane pionowo tabele


--utworzneie nowych tabel partycjonowanych pionowo
use AdventureWorks2019;
CREATE TABLE Person.Person_part1
(
	BusinessEntityID int NOT NULL,
	FirstName nvarchar(50) NOR NULL
	--pozostale kolumnt
	CONSTRAINT PK_Person_Part1 PRIMARY KEY (BusinessEntityID)
)

CREATE TABLE Person.Person_part2
(
	BusinessEntityID int NOT NULL,
	FirstName nvarchar(50) NOR NULL
	--pozostale kolumnt
	CONSTRAINT PK_Person_Part2 PRIMARY KEY (BusinessEntityID)
	CONSTRAINT FK_Person_Part2 FOREIGN KEY (BusinessEntityID) REFERENCES Person.Person_part1(BusinessEntityID)
)


--przeniesienie danych 
INSERT INTO Person.Person_part1(BusinessEntityID,EmployeeAddress,....)
select BusinessEntityID,EmployeeAddress,PhoneNumber,....
FROM Person.Person


--utworzneie widoku laczacego
CREATE VIEW Person.Person as
SELECT
	p1.BusinessEntityID,
	p1.FirstName,
	p1.LastName,
	p1.EmployeeAddress,
	p1.PhoneNumber,
	.
	.
	.
FROM Person.Person_part1 p1
LEFT JOIN Person.Person_part2 p2 on p1.BusinessEntityID=p2.BusinessEntityID









--Zadanie 3: Partycjonowanie Poziome według Regionu
--Cel: Podziel tabelę Sales.SalesOrderHeader na partycje według kolumny TerritoryID.
--Treść zadania:
--Utwórz schemat partycjonowania dla tabeli Sales.SalesOrderHeader według kolumny TerritoryID.
--Stwórz odpowiednią funkcję partycjonowania.
--Utwórz nową tabelę partycjonowaną, która będzie przechowywać dane z tabeli Sales.SalesOrderHeader.
--Przenieś dane z oryginalnej tabeli do nowej tabeli partycjonowanej.

-- Kroki 1 i 2: Utwórz schemat partycjonowania i funkcję partycjonowania

-- Utwórz schemat partycjonowania
CREATE PARTITION SCHEME SalesPartitionScheme
AS PARTITION SalesPartitionFunction
TO ([PRIMARY], [Secondary]);

-- Utwórz funkcję partycjonowania
CREATE PARTITION FUNCTION SalesPartitionFunction (int)
AS RANGE LEFT FOR VALUES (5, 10, 15, 20);

-- Kroki 3 i 4: Utwórz nową tabelę partycjonowaną i przenieś dane

-- Utwórz nową tabelę partycjonowaną
CREATE TABLE Sales.SalesOrderHeader_Partitioned
(
    SalesOrderID int NOT NULL PRIMARY KEY,
    RevisionNumber int NOT NULL,
    OrderDate datetime NOT NULL,
    DueDate datetime NOT NULL,
    ShipDate datetime NULL,
    Status int NOT NULL,
    OnlineOrderFlag bit NOT NULL,
    SalesOrderNumber nvarchar(25) NOT NULL,
    PurchaseOrderNumber nvarchar(25) NULL,
    AccountNumber nvarchar(15) NULL,
    CustomerID int NULL,
    SalesPersonID int NULL,
    TerritoryID int NULL,
    BillToAddressID int NOT NULL,
    ShipToAddressID int NOT NULL,
    ShipMethodID int NOT NULL,
    CreditCardID int NULL,
    CreditCardApprovalCode varchar(15) NULL,
    CurrencyRateID int NULL,
    SubTotal money NOT NULL,
    TaxAmt money NOT NULL,
    Freight money NOT NULL,
    TotalDue money NOT NULL,
    Comment nvarchar(max) NULL,
    rowguid uniqueidentifier NOT NULL,
    ModifiedDate datetime NOT NULL
)
ON SalesPartitionScheme(TerritoryID); -- Partycjonuj według TerritoryID

-- Przenieś dane z oryginalnej tabeli do nowej tabeli partycjonowanej
INSERT INTO Sales.SalesOrderHeader_Partitioned 
(
    SalesOrderID, RevisionNumber, OrderDate, DueDate, ShipDate, Status, OnlineOrderFlag, 
    SalesOrderNumber, PurchaseOrderNumber, AccountNumber, CustomerID, SalesPersonID, 
    TerritoryID, BillToAddressID, ShipToAddressID, ShipMethodID, CreditCardID, 
    CreditCardApprovalCode, CurrencyRateID, SubTotal, TaxAmt, Freight, TotalDue, Comment, 
    rowguid, ModifiedDate
)
SELECT 
    SalesOrderID, RevisionNumber, OrderDate, DueDate, ShipDate, Status, OnlineOrderFlag, 
    SalesOrderNumber, PurchaseOrderNumber, AccountNumber, CustomerID, SalesPersonID, 
    TerritoryID, BillToAddressID, ShipToAddressID, ShipMethodID, CreditCardID, 
    CreditCardApprovalCode, CurrencyRateID, SubTotal, TaxAmt, Freight, TotalDue, Comment, 
    rowguid, ModifiedDate
FROM Sales.SalesOrderHeader;
