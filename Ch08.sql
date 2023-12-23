create database Ch08;

CREATE TABLE 員工表
(
編號  CHAR(5) ,
姓名  NVARCHAR(10) NOT NULL,
部門  NVARCHAR (10) NULL,
PRIMARY  KEY(編號)
)

INSERT INTO 員工表
VALUES  ('S0001','一心', '銷售部'), 
('S0002','二聖', '生產部'), 
('S0003','三多', '銷售部'),
        ('S0004','四維', '生產部'),
        ('S0005','五福', '銷售部')


select * from 員工表;

CREATE TABLE 產品表
(
品號  CHAR(5),
品名  NVARCHAR (10) NOT NULL,
定價  INT,
PRIMARY KEY(品號)
 )

 INSERT INTO 產品表
VALUES ('P0001','筆電','30000'),
('P0002','滑鼠','1000'),
('P0003','手機','15000'),
('P0004','硬碟','2500'),
('P0005','手錶','3000'),
('P0006','耳機','1200')

select * from 產品表;

CREATE TABLE 銷售表
(
編號  CHAR(5),
品號  CHAR(5),
數量  INT NOT NULL,
PRIMARY KEY(編號,品號),
FOREIGN KEY(編號) REFERENCES 員工表(編號)
ON UPDATE CASCADE
ON DELETE CASCADE,
FOREIGN KEY(品號) REFERENCES 產品表(品號)
)

INSERT INTO 銷售表(編號,品號, 數量)
VALUES ('S0001','P0001','56'),
('S0001','P0005','73'),
('S0002','P0002','92'),
('S0002','P0005','63'),
('S0003','P0004','92'),
('S0003','P0005','70'),
('S0004','P0003','75'),
('S0004','P0004','88'),
('S0004','P0005','68'),
('S0005','P0005','95')

select * from 銷售表;

SELECT 姓名, 部門
FROM 員工表

SELECT 品名  AS  產品名稱,定價
FROM 產品表

select * from 產品表;

select * from 銷售表;

SELECT 編號, 數量 AS 銷售數量
FROM 銷售表
WHERE 品號='P0005'

SELECT 編號, 數量 AS 銷售數量
FROM 銷售表
WHERE 品號='P0004'

SELECT 編號, 品號, 數量 AS 銷售數量
FROM 銷售表
WHERE 數量<70

SELECT 編號,數量 AS 銷售數量
FROM 銷售表
WHERE 數量>70 And 品號='P0005'

SELECT 編號,品號,數量 AS 銷售數量
FROM 銷售表
WHERE 品號='P0001' Or 品號='P0005'

SELECT 編號,數量 AS 銷售數量
FROM 銷售表
WHERE 品號='P0001' And Not  數量>=70

SELECT 編號, 品號, 數量
FROM 銷售表
WHERE 數量 IS NULL

SELECT 編號, 品號, 數量
FROM 銷售表
WHERE 數量 IS NOT NULL

SELECT *
FROM 員工表
WHERE 部門 Like '生%'

SELECT *
FROM 員工表
WHERE 部門 Like '銷%'

SELECT 編號,品號,數量 AS 銷售數量
FROM 銷售表
WHERE 品號 In ('P0001','P0005')

SELECT 編號,品號,數量 AS 銷售數量
FROM 銷售表
WHERE 品號 in ('P0001','P0005')

SELECT 編號,姓名
FROM  員工表
WHERE 編號 In ('S0001', 'S0002', 'S0003')

SELECT 編號, 品號, 數量
FROM 銷售表
WHERE 數量 Between 60 And 90

SELECT 編號, 品號, 數量
FROM 銷售表
WHERE 品號 In ('P0001','P0005') and 數量 Between 60 And 90

SELECT 編號, 品號, 數量
FROM 銷售表
WHERE 數量*2 > 73

SELECT Count(*) AS 公司總人數
FROM 員工表;

select * from 員工表;

SELECT Count(*) AS 銷售筆數
FROM 銷售表

SELECT AVG(數量) AS 平均數量
FROM 銷售表
WHERE 品號='P0005'

SELECT AVG(數量) AS 平均數量
FROM 銷售表
WHERE 編號='S0001';

SELECT 編號, AVG(數量) AS 平均數量
FROM 銷售表
GROUP BY 編號

SELECT SUM(數量) AS 手錶總數量
FROM 銷售表
WHERE 品號='P0005'

SELECT SUM(數量) AS 手錶總數量
FROM 銷售表
GROUP BY 編號

SELECT MAX(數量) AS 手錶最高數量
FROM 銷售表
WHERE 品號='P0005'

SELECT 編號, 品號, 數量 AS 銷售數量排序
FROM 銷售表
ORDER BY 數量 desc

SELECT *
FROM 銷售表
ORDER BY 編號,品號, 數量

SELECT *
FROM 銷售表
ORDER BY 編號 ASC, 數量 DESC;

SELECT 編號, Count(*) AS 銷售產品種類數
FROM 銷售表
GROUP BY 編號

SELECT 編號, AVG(數量) AS 平均數量
FROM 銷售表
GROUP BY 編號

SELECT 品號, Count(*) AS 銷售員工數
FROM 銷售表
GROUP BY 品號
ORDER BY 品號 DESC

SELECT  品號, Count(*) AS 銷售員工數, MAX(數量) AS 最高數量
FROM 銷售表
GROUP BY 品號
ORDER BY 品號

SELECT 品號, Count(*) AS 銷售員工數, AVG(數量) AS 平均數量
FROM 銷售表
GROUP BY 品號
ORDER BY 品號

SELECT 編號, AVG(數量) AS 平均數量
FROM 銷售表
GROUP BY 編號
HAVING AVG(數量)>=70

SELECT 編號, Count(*) AS 銷售產品種類
FROM 銷售表
GROUP BY 編號
HAVING COUNT(*)>=2


SELECT DISTINCT 編號
FROM 銷售表

