create database Ch07;

CREATE TABLE ���u��
(
�s��  CHAR(5) ,
�m�W  NVARCHAR(10) NOT NULL,
����  NVARCHAR (10) NULL,
PRIMARY  KEY(�s��)
) 

CREATE TABLE ���~��
(
�~��  CHAR(5),
�~�W  NVARCHAR (10) NOT NULL,
�w��  INT,
PRIMARY KEY(�~��)
 )

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

ALTER  TABLE ���u��
ADD  �ʧO NCHAR(1) Default '�k';

INSERT INTO ���u��
VALUES ('S0001', '�@��','�P�ⳡ','�k')

INSERT INTO ���u��(�s��,�m�W,����)
VALUES ('S0002', '�G�t','�Ͳ���');

INSERT INTO ���u��
VALUES ('S0003','�T�h', '�P�ⳡ','�k'),
       ('S0004','�|��', '�Ͳ���','�k'),
       ('S0005','����', '�P�ⳡ','�k')



select * from ���u��;

CREATE TABLE ���u��OLD
(
�s��  CHAR(5) ,
�m�W  NVARCHAR(10) NOT NULL,
����  NVARCHAR (10) NULL,
�ʧO NCHAR(1)
PRIMARY  KEY(�s��)
)

INSERT INTO ���u��OLD
VALUES ('S0006','���X', '�P�ⳡ','�k'),
('S0007','�C��', '�P�ⳡ','�k'),
('S0008','�K�w', '�Ͳ���','�k'),
('S0009','�E�p', '�Ͳ���','�k'),
        ('S0010','�Q��', '�Ͳ���','�k') 

select * from ���u��OLD;


INSERT INTO ���u��
SELECT *
FROM ���u��OLD

update ���u��
set ����  = '�Ͳ���'
where �m�W = '���M'

UPDATE ���u��
SET ����= '�Ͳ���'
WHERE �m�W='���X'

update ���u��
set ���� = '�P�ⳡ', �m�W = '���w'
where �s�� = 'S0010'

select * from ���u��;

delete
from ���u��OLD
where �m�W = '�Q��'

select * from ���u��OLD;


select * from ���u��;

select *
from ���u��
where �ʧO='�k'