use AdventureWorks2019;
--Wypisz wszystkich pracownik�w (FirstName, LastName) wraz z ich stanowiskiem (JobTitle) 
--z tabeli HumanResources.Employee oraz Person.Person, gdzie data zatrudnienia (HireDate)
--jest p�niejsza ni� 1 stycznia 2007 roku.
select FirstName, LastName, e.JobTitle from HumanResources.Employee e
join Person.Person p on p.BusinessEntityID=e.BusinessEntityID
where e.HireDate > '2007-01-01'

--Znajd� �redni� cen� produkt�w (ListPrice) dla ka�dej kategorii produkt�w (Name) z 
--tabel Production.Product oraz Production.ProductCategory.
select AVG(p.ListPrice) as average_price, pc.Name from Production.Product p
join Production.ProductSubcategory ps on ps.ProductSubcategoryID=p.ProductSubcategoryID
join Production.ProductCategory pc on pc.ProductCategoryID=ps.ProductCategoryID
group by pc.Name

--Wypisz nazwy produkt�w, kt�re nigdy nie zosta�y zam�wione
--(wykorzystaj tabele Sales.SalesOrderDetail i Production.Product).
select Name from Production.Product p
left join Sales.SalesOrderDetail sod on sod.ProductID=p.ProductID
where sod.ProductID is Null;


--Utw�rz zapytanie  indeks na kolumnie HireDate w tabeli HumanResources.Employee 
--w celu optymalizacji zapyta� filtruj�cych po tej kolumnie.
create index idx_HireDate on HumanResources.Employee(HireDate);

-- Znajd� wszystkie zam�wienia dla klienta o CustomerID r�wnym 1, kt�re zawieraj� 
--wi�cej ni� 5 r�nych produkt�w. U�yj tabel Sales.SalesOrderHeader i Sales.SalesOrderDetail.
select soh.SalesOrderID, count(distinct sod.ProductID) as all_order from Sales.SalesOrderHeader soh
inner join Sales.SalesOrderDetail sod on soh.SalesOrderID=sod.SalesOrderID
where soh.CustomerID=11000
group by  soh.SalesOrderID
having  count(distinct sod.ProductID)>1;

--Znajd� wszystkich klient�w (CustomerID) z tabeli Sales.OrderHeader, 
--kt�rzy z�o�yli zam�wienie w 2019 roku. Zwr�� uwag� na wydajno�� zapytania.
create index idx_order_zajecia on Sales.SalesOrderHeader (CustomerID)

select * from Sales.SalesOrderHeader
where YEAR(OrderDate)='2013';


--Wypisz nazwiska (LastName) i imiona (FirstName) pracownik�w, 
--kt�rzy zostali zatrudnieni po roku 2015 i pracuj� na stanowisku 'Sales Representative'.
select LastName, FirstName from Person.Person pp
inner join HumanResources.Employee hre on hre.BusinessEntityID=pp.BusinessEntityID
where YEAR(hre.HireDate)>'2010' and hre.JobTitle='Sales Representative';

--Oblicz �redni� cen� produkt�w w ka�dej kategorii produkt�w. [Production.Product] i [Production.ProductCategory]
select pc.Name,AVG(pp.ListPrice) average_price from Production.Product pp
inner join Production.ProductSubcategory pps on pps.ProductSubcategoryID=pp.ProductSubcategoryID
inner join Production.ProductCategory pc on pc.ProductCategoryID=pps.ProductCategoryID
group by pc.Name


--Utw�rz zapytanie, kt�re wy�wietla ranking sprzedawc�w w
-- oparciu o ��czn� kwot� sprzeda�y. [Sales.SalesOrderHeader] [Sales.SalesPerson]
-- utworz widok zmaterializowany
create view name_view as
select top 100 percent sp.BusinessEntityID,sum(soh.TotalDue) total from Sales.SalesOrderHeader soh
inner join Sales.SalesPerson sp on soh.SalesPersonID=sp.BusinessEntityID 
group by sp.BusinessEntityID
order by total desc

select * from name_view;
drop view name_view;

--Utw�rz nowego u�ytkownika z autentykacj� SQL.
--Przypisz u�ytkownika do roli serwera sysadmin
--Przypisz u�ytkownika do roli bazy danych db_datareader w AdventureWorks2019.
--Przydziel u�ytkownikowi uprawnienia do odczytu z wybranej tabeli w AdventureWorks2019.
--Przydziel u�ytkownikowi uprawnienia do odczytu tylko wybranych kolumn w tabeli Person.Person

-- Utw�rz nowego u�ytkownika
CREATE LOGIN [NowyUzytkownik] WITH PASSWORD = 'silne_haslo';
-- Przypisz u�ytkownika do roli sysadmin na poziomie serwera
ALTER SERVER ROLE sysadmin ADD MEMBER [NowyUzytkownik];
-- Przypisz u�ytkownika do roli db_datareader w bazie danych AdventureWorks2019
USE AdventureWorks2019;
CREATE USER [NowyUzytkownik] FOR LOGIN [NowyUzytkownik];
ALTER ROLE db_datareader ADD MEMBER [NowyUzytkownik];
----Przydziel u�ytkownikowi uprawnienia do odczytu z wybranej tabeli w AdventureWorks2019
grant select on Sales.SalesPerson to NowyUzytkownik
--Przydziel u�ytkownikowi uprawnienia do odczytu tylko wybranych kolumn w tabeli Person.Person
grant select on Person.person (FirstName, LastName) to NowyUzytkownik



--Zadanie
--Utworzenie U�ytkownika:
--Utw�rz u�ytkownika SQL Analyst z silnym has�em. U�ytkownik ten b�dzie s�u�y� do analizy danych z bazy AdventureWorks2019.
create login SQL_Analyst with password='silnehaslo123!';
create user SQL_Analyst for login SQL_Analyst;
grant select on database::AdventureWorks2019 to SQL_Analyst;

--Przydzielenie Roli:
--Przydziel u�ytkownikowi Analyst rol� db_datareader, kt�ra pozwoli na czytanie 
--wszystkich tabel w bazie danych AdventureWorks2019.
use AdventureWorks2019;
alter role db_datareader add member SQL_Analyst

--Ograniczenie Uprawnie�:
--Mimo �e u�ytkownik Analyst ma uprawnienia do czytania z wszystkich tabel, wymagane jest, 
--aby mia� ograniczony dost�p tylko do niekt�rych kolumn w tabeli Person.Person. 
--Przydziel u�ytkownikowi uprawnienia do odczytu tylko kolumn FirstName, LastName, i EmailAddress.
deny select on Person.Person to SQL_Analyst;
grant select on Person.Person (FirstName, LastName,EmailPromotion) to SQL_Analyst;


--Uprawnienia do Wykonywania Procedur Sk�adowanych:
--W bazie danych AdventureWorks2019 znajduje si� procedura sk�adowana uspGetManagerEmployees. 
--Przydziel u�ytkownikowi Analyst uprawnienia do jej wykonywania.
grant execute on uspGetManagerEmployees to SQL_Analyst;

--Historia:
--Dzia� sprzeda�y AdventureWorks2019 chce przydzieli� dost�p do danych sprzeda�owych dla nowego analityka, Marka. 
--Marek musi mie� mo�liwo�� przegl�dania danych sprzeda�owych, ale nie powinien mie� dost�pu do informacji o kosztach zakupu produkt�w.
--Zadania:
--Utw�rz u�ytkownika SQL MarkSalesAnalyst z bezpiecznym has�em.
--Przydziel u�ytkownikowi dost�p do bazy danych AdventureWorks2019 jako db_datareader.
--Ogranicz uprawnienia Marka, aby nie m�g� on wykonywa� zapyta� do kolumny StandardCost w tabeli Production.Product.
--Przydziel Markowi uprawnienia do wykonania procedury uspGetWhereUsedProductID, kt�ra pozwoli mu analizowa�, gdzie produkty s� u�ywane.
create login marek with password='silnehaslo123!';
CREATE USER marek for login marek;
use AdventureWorks2019;
alter role db_datareader add member marek;
deny select on Production.Product (StandardCost) to marek;
grant execute on uspGetWhereUsedProductID to marek;

--Historia:
--Zesp� sprzeda�y AdventureWorks2019 potrzebuje szybszego dost�pu do raport�w sprzeda�y. 
--Obecny czas dost�pu do danych jest niezadowalaj�cy, a zadaniem IT jest optymalizacja tego procesuZadania:
--Utw�rz u�ytkownika SQL SalesReportUser z bezpiecznym has�em.
--Przydziel uprawnienia do wykonania istniej�cej procedury sk�adowanej uspGetSalesReport dla SalesReportUser.
--Zasugeruj zmian� w strukturze indeks�w, kt�ra mog�aby poprawi� wydajno�� procedury uspGetSalesReport, nie zmieniaj�c jej kodu.
create login SalesReportUser with password='silnehaslo123!';
create user SalesReportUser for login SalesReportUser;
grant execute on uspGetSalesReport to SalesReportUser;
-- tworzenie indeksow dla danej procedury
