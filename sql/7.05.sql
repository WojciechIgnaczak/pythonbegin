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