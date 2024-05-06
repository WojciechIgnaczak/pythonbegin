use AdventureWorks2019;
go
-- wyswietl klientow z sales.customer, sortujac nazwisko lastname malejaca
select * from Sales.Customer sc
inner join Person.Person pp on pp.BusinessEntityID=sc.PersonID
order by pp.LastName desc

-- list proce produktow dla kazddej kategorii produktow z tabeli production.prosuct
select  ppc.Name,AVG(pp.ListPrice)as avg_price from Production.Product pp
inner join Production.ProductSubCategory ppsc on pp.ProductSubcategoryID=ppsc.ProductSubcategoryID
inner join Production.ProductCategory ppc on ppsc.ProductCategoryID=ppc.ProductCategoryID
group by ppc.Name

--z tabeli person.person wybierz osoby krorych firstname zaczyna sie na A uzyj Left()
select * from Person.Person
where left(FirstName,1)='A'

-- wybierz wszystkie produkty ktore nie zostalu zamowione z production.product i sales.salesorderdetail
select * from Production.Product pp
left join Sales.SalesOrderDetail sod on sod.ProductID=pp.ProductID
where sod.ProductID is null;

--wszystkie nazwiska LastName pracowników i nazwy dzialow Name, w ktorych pracuja korzystajac z humanresources.emploee person.person i humanresources.department
select pp.LastName, hrd.Name from HumanResources.Employee hre
inner join Person.Person pp on pp.BusinessEntityID=hre.BusinessEntityID
inner join HumanResources.EmployeeDepartmentHistory hredh on hredh.BusinessEntityID=hre.BusinessEntityID
inner join HumanResources.Department hrd on hrd.DepartmentID= hredh.DepartmentID

--wybierz nazwy dzialow i liczbe pracownikow w kazdym dziale z tabeli hr.department i hr.empdephist, grupujac po nazwie dzialow
select hrd.Name, count(1) as number_of_employee from HumanResources.Employee hre
inner join Person.Person pp on pp.BusinessEntityID=hre.BusinessEntityID
inner join HumanResources.EmployeeDepartmentHistory hredh on hredh.BusinessEntityID=hre.BusinessEntityID
inner join HumanResources.Department hrd on hrd.DepartmentID= hredh.DepartmentID
group by hrd.Name
order by number_of_employee desc

-- z tabeli person.person first,lastname oraz fullname utworz, ktora bedzie zawierac  imie nazwisko oddzielone spacja
select FirstName, LastName, concat(FirstName,' ',LastName) FullName from Person.Person

--napisz zapytanie ktore dodaje nowego pracownika do humanresources.employeem a nastepnie aktualizuje jego jobtitle wszystko w ramach 1 transakcji


--wybierz productid i orderqty z tabeli sales.salesorderdetail dla salesorderid <1000 i zapisz w tabeli tymczasowej. nastepnie wybierz rekordy wszystkie z tej tabeli tymczasowej
select ProductID,OrderQty INTO #TempOrder
from Sales.SalesOrderDetail
where SalesOrderID>1000;

select * from #TempOrder

--napisz skrypt ktory dynamicznie tworzy i wykonuje zapytanie sql wybierajace wszystkie kolumny z tabeli person.adree i sort wg city;
DECLARE @query as NVARCHAR(MAX);
SET @query= 'SELECT * FROM Person.Address ORDER BY City';
Exec sp_executesql @query

-- z tabeli sales.sales orderheader kolumny salesorderid i  orderdate, uzyj try convert do przekonwertowania order date na yyyy-mm-dd
select SalesOrderID, TRY_CONVERT(date,OrderDate) AS OrderDate from Sales.SalesOrderHeader

--wyswietl buissnesentityid i  liczbe dni ktore uplynel od hiredate do dzisiaj dla kazdego pracownika z tabeli humanresources.employee
select BusinessEntityID, datediff(d,HireDate,getdate()) as ilosc_dni_zatrudnienia from HumanResources.Employee
--wybierz orderdate z tabeli sales.salesorderheader i sformatuj daty w formaccie mm-dd-yyyy
select FORMAT(OrderDate, 'MM-dd-yyyy') as newdate from Sales.SalesOrderHeader
--z tab person.person wybierz buisnesentutyid, forstname,lastname oras kolumne isfemale ktora bedzi true jesli gender='f' w przeciwnym false
select pp.BusinessEntityID, pp.FirstName, pp.LastName, CASE WHEN emp.Gender = 'F' THEN 1 ELSE 0 END AS IsFemale  from Person.Person pp
inner join HumanResources.Employee emp on emp.BusinessEntityID=pp.BusinessEntityID

--znajdz wszystkie duplikaty emailadreess w tabeli person.person
select EmailAddress from Person.EmailAddress
group by EmailAddress
having count(*)>1


--Utwórz widok V_EmployeeDepartment, który wyœwietla imiona i nazwiska pracowników oraz nazwy ich 
--dzia³ów z tabel HumanResources.Employee, Person.Person i HumanResources.Department.
create view V_EmployeeDepartment as
select pp.FirstName,pp.LastName,dep.Name from HumanResources.Employee emp
join Person.Person pp on emp.BusinessEntityID=pp.BusinessEntityID
join HumanResources.EmployeeDepartmentHistory edh on emp.BusinessEntityID=edh.BusinessEntityID
join HumanResources.Department dep on dep.DepartmentID=edh.DepartmentID;

drop view V_EmployeeDepartment
-- przerzucenie wyniku zapytania do json
select  SalesOrderID,OrderDate from Sales.SalesOrderHeader
for json path

--pliki ktore wykorzystuje baza
select f.name,
f.size/128 as current_sizeMB,
f.growth/128 as growthSizeMB from sys.database_files f
size/128.0 - CAST(FILEPROPERTY(name,'SpaceUsed') as int
where f.type_desc='ROWS'