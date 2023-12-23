create database Ch07;

CREATE TABLE 員工表
(
編號  CHAR(5) ,
姓名  NVARCHAR(10) NOT NULL,
部門  NVARCHAR (10) NULL,
PRIMARY  KEY(編號)
) 

CREATE TABLE 產品表
(
品號  CHAR(5),
品名  NVARCHAR (10) NOT NULL,
定價  INT,
PRIMARY KEY(品號)
 )

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

ALTER  TABLE 員工表
ADD  性別 NCHAR(1) Default '男';

INSERT INTO 員工表
VALUES ('S0001', '一心','銷售部','男')

INSERT INTO 員工表(編號,姓名,部門)
VALUES ('S0002', '二聖','生產部');

INSERT INTO 員工表
VALUES ('S0003','三多', '銷售部','女'),
       ('S0004','四維', '生產部','男'),
       ('S0005','五福', '銷售部','女')



select * from 員工表;

CREATE TABLE 員工表OLD
(
編號  CHAR(5) ,
姓名  NVARCHAR(10) NOT NULL,
部門  NVARCHAR (10) NULL,
性別 NCHAR(1)
PRIMARY  KEY(編號)
)

INSERT INTO 員工表OLD
VALUES ('S0006','六合', '銷售部','女'),
('S0007','七賢', '銷售部','女'),
('S0008','八德', '生產部','男'),
('S0009','九如', '生產部','女'),
        ('S0010','十全', '生產部','男') 

select * from 員工表OLD;


INSERT INTO 員工表
SELECT *
FROM 員工表OLD

update 員工表
set 部門  = '生產部'
where 姓名 = '六和'

UPDATE 員工表
SET 部門= '生產部'
WHERE 姓名='六合'

update 員工表
set 部門 = '銷售部', 姓名 = '李安'
where 編號 = 'S0010'

select * from 員工表;

delete
from 員工表OLD
where 姓名 = '十全'

select * from 員工表OLD;


select * from 員工表;

select *
from 員工表
where 性別='女'