-- wypisz wszystkich pracownikow FirstName, SecondName z Jobtitle gdzie HireDate pozniejsz niz 1 stycznia  2017 humanresources.employeee oraz person.person
USE AdventureWorks2019;
SELECT p.FirstName, p.LastName, e.JobTitle FROM  HumanResources.Employee e
INNER JOIN Person.Person p ON p.BusinessEntityID =e.BusinessEntityID
WHERE e.HireDate > '01.01.2007';

-- znajdz srednia cene produktow ListPrice dla kazdej kategorii Name z tabeli Production.production i production.productcategory
SELECT pc.Name, AVG(p.ListPrice) Average FROM Production.Product p
INNER JOIN Production.ProductSubcategory as ps ON p.ProductSubcategoryID =ps.ProductSubcategoryID
INNER JOIN Production.ProductCategory pc ON pc.ProductCategoryID=pc.ProductCategoryID 
GROUP BY pc.Name

-- Nazwy produktow ktore nigdy nie zostaly zamowione tabela Sales.salesorderdetail i production.product
SELECT p.Name FROM Production.Product p
LEFT JOIN Sales.SalesOrderDetail s ON p.ProductID =s.ProductID
WHERE s.ProductID IS NULL;

--Utworz indeks na kolumnie HireDate w tabeli HumanResources.Employee w celu optymalizacji zapytan po tej kolumnie
CREATE INDEX Indeks_zajecia ON HumanResources.Employee (HireDate);

-- wszystkie zamowienia dl aklienta o CustomerID =1 , kroe maja wiecej niz 5 roznych produktow. Sales.salesorderheader, sales.salesorderdetail
SELECT h.SalesOrderID,COUNT(d.ProductID) ilosc_produktow  FROM Sales.SalesOrderHeader h
INNER JOIN Sales.SalesOrderDetail d ON h.SalesOrderID =d.SalesOrderID
WHERE h.CustomerID=11000
GROUP BY h.SalesOrderID
HAVING COUNT(DISTINCT  d.ProductID) >0;

--Znajdź wszystkich klientów (CustomerID) z tabeli Sales.OrderHeader, którzy złożyli zamówienie w 2019 roku. Zwróć uwagę na wydajność zapytania.
SELECT DISTINCT CustomerID FROM Sales.SalesOrderHeader
WHERE YEAR(OrderDate) ='2011';

--Wypisz nazwiska (LastName) i imiona (FirstName) pracowników, którzy zostali zatrudnieni po roku 2015 i pracują na stanowisku 'Sales Representative'.
SELECT p.FirstName, p.LastName FROM  HumanResources.Employee e
INNER JOIN Person.Person p ON p.BusinessEntityID =e.BusinessEntityID
WHERE e.HireDate >= '01.01.2005' AND JobTitle ='Sales Representative';


----Oblicz średnią cenę produktów w każdej kategorii produktów. [Production.Product] i [Production.ProductCategory]
SELECT c.Name, AVG(p.ListPrice) Average FROM Production.Product p
INNER JOIN Production.ProductCategory c ON p.ProductSubcategoryID=c.ProductCategoryID 
GROUP BY c.Name

--Utwórz zapytanie, które wyświetla ranking sprzedawców w
-- oparciu o łączną kwotę sprzedaży. [Sales.SalesOrderHeader] [Sales.SalesPerson]
-- utworz widok zmaterializowany

--jak ominac order by w widoku- nalezy uzyc top 100 precent
CREATE VIEW nazwa AS
SELECT TOP 100 PERCENT sp.BusinessEntityID, SUM(h.TotalDue) as all_sales_quota FROM Sales.SalesPerson sp
INNER JOIN Sales.SalesOrderHeader h ON sp.BusinessEntityID =h.SalesPersonID
WHERE sp.SalesQuota IS NOT NULL
GROUP BY sp.BusinessEntityID
ORDER BY all_sales_quota desc;
GO
select * from nazwa;
drop view nazwa;

