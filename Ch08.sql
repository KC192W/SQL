create database Ch08;

CREATE TABLE ���u��
(
�s��  CHAR(5) ,
�m�W  NVARCHAR(10) NOT NULL,
����  NVARCHAR (10) NULL,
PRIMARY  KEY(�s��)
)

INSERT INTO ���u��
VALUES  ('S0001','�@��', '�P�ⳡ'), 
('S0002','�G�t', '�Ͳ���'), 
('S0003','�T�h', '�P�ⳡ'),
        ('S0004','�|��', '�Ͳ���'),
        ('S0005','����', '�P�ⳡ')


select * from ���u��;

CREATE TABLE ���~��
(
�~��  CHAR(5),
�~�W  NVARCHAR (10) NOT NULL,
�w��  INT,
PRIMARY KEY(�~��)
 )

 INSERT INTO ���~��
VALUES ('P0001','���q','30000'),
('P0002','�ƹ�','1000'),
('P0003','���','15000'),
('P0004','�w��','2500'),
('P0005','���','3000'),
('P0006','�վ�','1200')

select * from ���~��;

CREATE TABLE �P���
(
�s��  CHAR(5),
�~��  CHAR(5),
�ƶq  INT NOT NULL,
PRIMARY KEY(�s��,�~��),
FOREIGN KEY(�s��) REFERENCES ���u��(�s��)
ON UPDATE CASCADE
ON DELETE CASCADE,
FOREIGN KEY(�~��) REFERENCES ���~��(�~��)
)

INSERT INTO �P���(�s��,�~��, �ƶq)
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

select * from �P���;

SELECT �m�W, ����
FROM ���u��

SELECT �~�W  AS  ���~�W��,�w��
FROM ���~��

select * from ���~��;

select * from �P���;

SELECT �s��, �ƶq AS �P��ƶq
FROM �P���
WHERE �~��='P0005'

SELECT �s��, �ƶq AS �P��ƶq
FROM �P���
WHERE �~��='P0004'

SELECT �s��, �~��, �ƶq AS �P��ƶq
FROM �P���
WHERE �ƶq<70

SELECT �s��,�ƶq AS �P��ƶq
FROM �P���
WHERE �ƶq>70 And �~��='P0005'

SELECT �s��,�~��,�ƶq AS �P��ƶq
FROM �P���
WHERE �~��='P0001' Or �~��='P0005'

SELECT �s��,�ƶq AS �P��ƶq
FROM �P���
WHERE �~��='P0001' And Not  �ƶq>=70

SELECT �s��, �~��, �ƶq
FROM �P���
WHERE �ƶq IS NULL

SELECT �s��, �~��, �ƶq
FROM �P���
WHERE �ƶq IS NOT NULL

SELECT *
FROM ���u��
WHERE ���� Like '��%'

SELECT *
FROM ���u��
WHERE ���� Like '�P%'

SELECT �s��,�~��,�ƶq AS �P��ƶq
FROM �P���
WHERE �~�� In ('P0001','P0005')

SELECT �s��,�~��,�ƶq AS �P��ƶq
FROM �P���
WHERE �~�� in ('P0001','P0005')

SELECT �s��,�m�W
FROM  ���u��
WHERE �s�� In ('S0001', 'S0002', 'S0003')

SELECT �s��, �~��, �ƶq
FROM �P���
WHERE �ƶq Between 60 And 90

SELECT �s��, �~��, �ƶq
FROM �P���
WHERE �~�� In ('P0001','P0005') and �ƶq Between 60 And 90

SELECT �s��, �~��, �ƶq
FROM �P���
WHERE �ƶq*2 > 73

SELECT Count(*) AS ���q�`�H��
FROM ���u��;

select * from ���u��;

SELECT Count(*) AS �P�ⵧ��
FROM �P���

SELECT AVG(�ƶq) AS �����ƶq
FROM �P���
WHERE �~��='P0005'

SELECT AVG(�ƶq) AS �����ƶq
FROM �P���
WHERE �s��='S0001';

SELECT �s��, AVG(�ƶq) AS �����ƶq
FROM �P���
GROUP BY �s��

SELECT SUM(�ƶq) AS ����`�ƶq
FROM �P���
WHERE �~��='P0005'

SELECT SUM(�ƶq) AS ����`�ƶq
FROM �P���
GROUP BY �s��

SELECT MAX(�ƶq) AS ����̰��ƶq
FROM �P���
WHERE �~��='P0005'

SELECT �s��, �~��, �ƶq AS �P��ƶq�Ƨ�
FROM �P���
ORDER BY �ƶq desc

SELECT *
FROM �P���
ORDER BY �s��,�~��, �ƶq

SELECT *
FROM �P���
ORDER BY �s�� ASC, �ƶq DESC;

SELECT �s��, Count(*) AS �P�ⲣ�~������
FROM �P���
GROUP BY �s��

SELECT �s��, AVG(�ƶq) AS �����ƶq
FROM �P���
GROUP BY �s��

SELECT �~��, Count(*) AS �P����u��
FROM �P���
GROUP BY �~��
ORDER BY �~�� DESC

SELECT  �~��, Count(*) AS �P����u��, MAX(�ƶq) AS �̰��ƶq
FROM �P���
GROUP BY �~��
ORDER BY �~��

SELECT �~��, Count(*) AS �P����u��, AVG(�ƶq) AS �����ƶq
FROM �P���
GROUP BY �~��
ORDER BY �~��

SELECT �s��, AVG(�ƶq) AS �����ƶq
FROM �P���
GROUP BY �s��
HAVING AVG(�ƶq)>=70

SELECT �s��, Count(*) AS �P�ⲣ�~����
FROM �P���
GROUP BY �s��
HAVING COUNT(*)>=2


SELECT DISTINCT �s��
FROM �P���

