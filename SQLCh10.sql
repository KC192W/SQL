use MyDB
go

CREATE VIEW ���u�˵���
AS
SELECT *
FROM ���u��
go

CREATE TABLE ���X��
(���X  CHAR(5),
����  CHAR(6),
PRIMARY  KEY(���X)
)
go 
INSERT INTO ���X��
VALUES  
('D01','�P�ⳡ'), 
('D02','�Ͳ���'), 
('D03','������')
go

CREATE VIEW ������u�˵���
AS
SELECT A.*,B.���X
FROM  ���u�� AS A,���X�� AS B
WHERE A.���� =B.����
go

INSERT INTO ���u�˵���
VALUES('S0006', '���X','������')
go

Update ���u�˵���
Set �m�W='�G��'
Where �s��='S0001'
go

DROP VIEW ������u�˵���
go


