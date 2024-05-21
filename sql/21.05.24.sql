-- do restore trzeba zamknąć wszystkie połączenia w options


-- sprawdzenie wszystkich backup-ów
use msdb
select * from backupset
order by backup_start_date desc

-- 
-- BACKUP'Y
BACKUP DATABASE [AdventureWorks2019] --full
TO  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backup3.bak' 
WITH NOFORMAT, NOINIT,  NAME = N'AdventureWorks2019-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO

BACKUP DATABASE [AdventureWorks2019] --differential
TO  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backup3.bak' 
WITH  DIFFERENTIAL , NOFORMAT, NOINIT,  NAME = N'AdventureWorks2019-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO

BACKUP LOG [AdventureWorks2019] --LOGI
TO  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backup3.bak' 
WITH NOFORMAT, NOINIT,  NAME = N'AdventureWorks2019-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO

-- RESTORE'Y
USE [master]
RESTORE DATABASE [AdventureWorks2019] 
FROM  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backup3.bak' 
WITH  FILE = 1,  NORECOVERY,  NOUNLOAD,  STATS = 5

RESTORE DATABASE [AdventureWorks2019] 
FROM  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backup3.bak' 
WITH  FILE = 7,  NORECOVERY,  NOUNLOAD,  STATS = 5

RESTORE LOG [AdventureWorks2019] 
FROM  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backup3.bak' 
WITH  FILE = 8,  NOUNLOAD,  STATS = 5
GO
