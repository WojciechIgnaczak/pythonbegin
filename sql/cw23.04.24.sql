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

--wybierz productid i orderqty z tabeli sales.salesorderdetail dla salesorderid <1000 i zapisz w tabeli tymczasowej. nastepnie wybierz rekordy wszystkie z tej tabeli tymczasowej
select ProductID,OrderQty INTO #TempOrder
from Sales.SalesOrderDetail
where SalesOrderID>1000;

select * from #TempOrder