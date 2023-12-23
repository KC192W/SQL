use MyDB
go

CREATE VIEW 員工檢視表
AS
SELECT *
FROM 員工表
go

CREATE TABLE 部碼表
(部碼  CHAR(5),
部門  CHAR(6),
PRIMARY  KEY(部碼)
)
go 
INSERT INTO 部碼表
VALUES  
('D01','銷售部'), 
('D02','生產部'), 
('D03','企劃部')
go

CREATE VIEW 完整員工檢視表
AS
SELECT A.*,B.部碼
FROM  員工表 AS A,部碼表 AS B
WHERE A.部門 =B.部門
go

INSERT INTO 員工檢視表
VALUES('S0006', '六合','企劃部')
go

Update 員工檢視表
Set 姓名='二心'
Where 編號='S0001'
go

DROP VIEW 完整員工檢視表
go


