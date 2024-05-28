use AdventureWorks2019
-- procedura do wyciagniecia info o sprzedazy produktów
-- przyjmuje id produktu jako wejscie i zwraca szczegułowe info o sprzedazy, tj. liczba sprzedanych sztuk,calkowita wartosc sprzedazy,srednia cena sprzedazy oraz data pierwszej i ostatniej sprzedazy
create procedure InfoProduct
	@ProductID int
	as
begin
select 
	count(sod.OrderQty) IloscSztuk,
	SUM(sod.UnitPrice)CalkowitaWartosc,
	SUM(sod.UnitPrice)/count(sod.ProductID) SredniaCena,
	MIN(soh.OrderDate) DataPierwszejSprzedazy,
	MAX(soh.OrderDate) DataOstatniejSprzedazy
	
from Sales.SalesOrderHeader soh
join Sales.SalesOrderDetail sod on sod.SalesOrderID=soh.SalesOrderID
where sod.ProductID=@ProductID

end

drop procedure InfoProduct
exec InfoProduct 778



-- FUNCKJA DO OBLICZANIA WIEKU PRACOWNIKA
	-- napisz funkcje po id pracownika i zwraca jego wiek na podstawie daty urodzenia
create function WiekPracownika(
	@PracownikID int
)
returns int
as
begin
	declare @wiek int
	set @wiek=(select Datediff(MONTH,BirthDate,GETDATE())/12 as wiek from HumanResources.Employee
	where BusinessEntityID=@PracownikID)
	return @wiek
end;

Select dbo.WiekPracownika(511) as wiek
drop function dbo.WiekPracownika

select Datediff(MONTH,BirthDate,GETDATE())/12 as wiek from HumanResources.Employee
where BusinessEntityID=123



-- procedura do generowania raopry o stanie magazynowym
-- procedura generuje raport o stanie magazynowym dl adanego magazynu. powinien zawierac info o nazwie produktu, dostepnej ilosci,sredniej cenie zakupu i calkowitej wartosci zapasow
create procedure InfoMagazyn
	@MagazynID int
	as
begin
select pp.ProductID,pp.Name,pi.Shelf,SUM(pi.Quantity) iloscSztuk, SUM(pp.StandardCost)/SUM(pi.Quantity) SredniaCenaZakupu, SUM(pp.StandardCost)*SUM(pi.Quantity) WartoscZapasow from  Production.ProductInventory pi
join Production.Product pp on pp.ProductID=pi.ProductID
where pi.LocationID=@MagazynID
group by pp.ProductID,pp.Name,pi.Shelf
end;


exec InfoMagazyn 50

drop procedure InfoMagazyn

-- prcedua do aktualizacji danych kontaktowych klient
--procedura przyjmuje id klienta, oraz nowe dane kontaktowe(mail,numer telefony) i aktualizuje odpowiednie rekordy w bazie danych

select * from Person.PersonPhone
create procedure UpdateContact
	@PersonID int,
	@emailAdress nvarchar(50),
	@phoneNumber Phone
	as
begin
update Person.EmailAddress 
set EmailAddress=@emailAdress
where BusinessEntityID=@PersonID;

update Person.PersonPhone
set PhoneNumber=@phoneNumber
where BusinessEntityID=@PersonID;
end;



-- funkcja do obliczania liczby zamowien zlozonych przez klienta w danym roku
-- orzyjmuje id oraz rok i zwraca liczbe zamowien zlozonych w danym roku
create function LiczbaZamowienRoku(
	@CustomerID int,
	@Year int
)
returns int
begin
declare @OrderCount int
select @OrderCount=count(SalesOrderID) from Sales.SalesOrderHeader
where CustomerID=@CustomerID and Year(OrderDate) =@Year
return @OrderCount
end;

select dbo.LiczbaZamowienRoku(29825,2011)
drop function LiczbaZamowienRoku

--gen raport o wydajnosci sprzedazy przedstawiciela handlowego
-- przyjmuje id SalesPersonID, i zrwaca liczbe zamowien,laczna wartosc,srednia wartosc zamowienia
create procedure RaportSprzedazyPrzedstawiciela
	@IdSalesPerson int
as
begin
select count(*) liczbaZamowien, SUM(totalDue) lacznaWartosc,SUM(totalDue)/count(*) sredniaWartosc   from Sales.SalesOrderHeader
where SalesPersonID=@IdSalesPerson
end;

exec RaportSprzedazyPrzedstawiciela 279
drop procedure RaportSprzedazyPrzedstawiciela




-- sprawdza w jakiej tabeli jest kolumna SalesPersonID
SELECT c.name,t.name,s.name
from sys.columns c
join sys.tables t on c.object_id=t.object_id
join sys.schemas s on t.schema_id=s.schema_id
where c.name='SalesPersonID'