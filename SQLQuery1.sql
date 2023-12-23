/*use MyDB is important or you will save MyDB under SystemDatabase:master 
use MyDB
go*/

CREATE TABLE �Юv��ƪ�
(�����Ҧr��  CHAR(10),
�m�W  NVARCHAR(10) NOT NULL,
�~��  INT,
�Ǿ��O  VARCHAR(10)NOT NULL,
�q�l�l��  VARCHAR(50)NOT NULL,
�q��  VARCHAR(15),
�ͤ�  date NOT NULL,
�b��  VARCHAR(50)NOT NULL,
�K�X  VARCHAR(50)NOT NULL,
¾�O  VARCHAR(10)NOT NULL,
�l��¾�ɶ�  date NOT NULL,
PRIMARY  KEY(�����Ҧr��)
)
go

CREATE TABLE �Ǯո�ƪ�
(�ǮեN�X  CHAR(10),
�զW  NVARCHAR(20) NOT NULL,
�]�ߧO  VARCHAR(10)NOT NULL,
�ŧO  VARCHAR(10)NOT NULL,
����  VARCHAR(10)NOT NULL,
�ϰ�  VARCHAR(10)NOT NULL,
���W  VARCHAR(10)NOT NULL,
�q��  VARCHAR(15),
PRIMARY  KEY(�ǮեN�X)
)
go

CREATE TABLE ���ʸ�ƪ�
(���ʽs��  CHAR(10),
���ʼ��D  NVARCHAR(20) NOT NULL,
����  VARCHAR(10)NOT NULL,
PRIMARY  KEY(���ʽs��)
)
go

CREATE TABLE �Ǯթӿ쬡�ʸ�ƪ�
(
�D�ӿ���  date NOT NULL,
���ʽs��  CHAR(10),
�ǮեN�X  CHAR(10),
PRIMARY KEY(���ʽs��,�ǮեN�X),
FOREIGN KEY(���ʽs��) REFERENCES ���ʸ�ƪ�(���ʽs��),
FOREIGN KEY(�ǮեN�X) REFERENCES �Ǯո�ƪ�(�ǮեN�X)
)
go

CREATE TABLE �Юv���ʰѻP����
(
���W�覡  VARCHAR(20),
�ɼ�  float NOT NULL,
���q  CHAR(10),
�ѥ[���A  CHAR(10) NOT NULL,
���ʽs��  CHAR(10),
�����Ҧr��  CHAR(10),
PRIMARY KEY(���ʽs��,�����Ҧr��),
FOREIGN KEY(���ʽs��) REFERENCES ���ʸ�ƪ�(���ʽs��),
FOREIGN KEY(�����Ҧr��) REFERENCES �Юv��ƪ�(�����Ҧr��)
)
go

/*insert data into �Юv��ƪ�*/
INSERT INTO �Юv��ƪ�
VALUES  
('A123456789', '�i�T', 5, '�դh', 'zhangsan@example.com', '0912345678', '1980-05-15', 'teacher1', 'password1', '�M���Юv', '2020-01-15'),
('B987654321', '���|', 8, '�դh', 'lisi@example.com', '0923456789', '1975-09-20', 'teacher2', 'password2', '�ݥ����v', '2015-03-10'),
('C111223344', '����', 3, '�դh', 'wangwu@example.com', '0934567890', '1990-12-01', 'teacher3', 'password3', '�U�z�б�', '2022-06-25'),
('D112233445', '����', 6, '�դh', 'cailiu@example.com', '0945678901', '1985-08-03', 'teacher4', 'password4', '�M�����v', '2019-02-18'),
('E554433221', '���C', 4, '�դh', 'chenqi@example.com', '0956789012', '1988-11-12', 'teacher5', 'password5', '�Ʊб�', '2020-09-05'),
('F334455667', '�L�K', 7, '�դh', 'linba@example.com', '0967890123', '1982-04-25', 'teacher6', 'password6', '�M���Юv', '2018-07-14'),
('G998877665', '�d�E', 9, '�դh', 'wuj@example.com', '0978901234', '1970-06-08', 'teacher7', 'password7', '�б�', '2014-11-30'),
('H776655443', '���Q', 5, '�դh', 'dongshi@example.com', '0989012345', '1995-03-17', 'teacher8', 'password8', '�U�z�б�', '2021-01-08'),
('I998877665', '���Q�@', 8, '�դh', 'zhushiyi@example.com', '0990123456', '1983-09-22', 'teacher9', 'password9', '�M���Юv', '2017-04-03'),
('J112233445', '���Q�G', 6, '�դh', 'mashier@example.com', '0912345678', '1980-05-15', 'teacher10', 'password10', '�Ʊб�', '2018-04-08')
go

INSERT INTO �Ǯո�ƪ�
VALUES 
('S123456789', '�˨ʤj��', '����', '�j��', '�x�_��', '������', '���s��', '02-12345678'),
('S987654321', '�n�ʤj��', '�p��', '�j��', '�s�_��', '�T�l��', '��Ƹ�', '02-23456789'),
('S111223344', '���ؤj��', '����', '�j��', '��饫', '�s���', '������', '03-34567890'),
('S112233445', '�����j��', '�p��', '�j��', '�x����', '��ٰ�', '��߸�', '04-45678901'),
('S554433221', '�n��j��', '����', '�j��', '�n�뿤', '�n�륫', '���s��', '04-56789012'),
('S334455667', '�����j��', '����', '�j��', '������', '��s��', '��Ƹ�', '07-67890123'),
('S998877665', '�򶩤j��', '����', '�j��', '�򶩥�', '���R��', '������', '02-78901234'),
('S776655443', '�s�˥��ߤj��', '����', '�j��', '�s�˥�', '�_��', '���_��', '03-89012345'),
('S198977995', '�x�n�v�d�j��', '����', '�j��', '�x�n��', '�w�n��', '�|�ֵ�', '06-90123456'),
('S132223445', '�F�s�j��', '�p��', '�j��', '�򶩥�', '�H�q��', '���s��', '02-12345678')
go

INSERT INTO ���ʸ�ƪ�
VALUES 
('A1234', 'Python ��¦�s�{�u�@�{', '�u�@�{'),
('B5678', '�оǧޥ����ɬ�Q�|', '��Q�|'),
('C9012', '�ƾǱШ|�s�Ͷծy�ͷ|', '�y�ͷ|'),
('D3456', 'STEM �Ш|����s�Z', '��s�Z'),
('E7890', '��T��ަb�y���оǪ����Τu�@�{', '�u�@�{')
go

INSERT INTO �Ǯթӿ쬡�ʸ�ƪ�
VALUES 
('2022-07-25', 'A1234', 'S198977995'),
('2023-01-12', 'B5678', 'S554433221'),
('2023-04-06', 'C9012', 'S111223344'),
('2023-06-15', 'D3456', 'S334455667'),
('2023-12-22', 'E7890', 'S198977995')
go

INSERT INTO �Юv���ʰѻP����
VALUES 
('�b�u���W', 4.5, '���', '�w���W', 'E7890', 'I998877665'),
('�{�����W', 6.0, '����', '�w�ѥ[', 'A1234', 'H776655443'),
('�q�l�l����W', 3.5, '���', '�w���W', 'E7890', 'G998877665'),
('�b�u���W', 5.5, '����', '�w�ѥ[', 'D3456', 'E554433221'),
('�{�����W', 4.0, '���', '�w�ѥ[', 'C9012', 'E554433221'),
('�b�u���W', 7.5, '���', '�w���W', 'E7890', 'J112233445'),
('�q�l�l����W', 6.0, '����', '�w�ѥ[', 'D3456', 'J112233445'),
('�{�����W', 3.5, '�i��', '���ѥ[', 'B5678', 'C111223344')
go

select *
from �Юv��ƪ�

SELECT A.�����Ҧr��,A.�m�W
FROM �Юv��ƪ� AS A LEFT OUTER JOIN �Юv���ʰѻP���� AS B
ON A.�����Ҧr��=B.�����Ҧr��
WHERE   B.�����Ҧr�� IS NULL

SELECT A.���ʼ��D AS ���ʦW��,B.���ʽs��, Count(*) AS ���ʰѻP�H��
FROM ���ʸ�ƪ� AS A LEFT OUTER JOIN �Юv���ʰѻP���� AS B
ON A.���ʽs��=B.���ʽs��
WHERE   B.�����Ҧr�� IS NULL

SELECT �Юv���ʰѻP����.���ʽs��, Count(*) AS ���ʰѻP�H��
FROM �Юv���ʰѻP����
GROUP BY ���ʽs��





Select �m�W AS �ѻP�Юv,�q�l�l��,���ʼ��D,�ѥ[���A
From ���ʸ�ƪ�,�Юv���ʰѻP����,�Юv��ƪ�
Where �Юv��ƪ�.�����Ҧr��=�Юv���ʰѻP����.�����Ҧr�� and ���ʸ�ƪ�.���ʽs��=�Юv���ʰѻP����.���ʽs��
order by �m�W




SELECT �~��, Count(*) AS �P����u��
FROM �P���
GROUP BY �~��
ORDER BY �~�� DESC

/*
INSERT INTO �P���(�s��,�~��, �ƶq)
VALUES 
('S0001','P0001','56'),
('S0001','P0005','73'),
('S0002','P0002','92'),
('S0002','P0005','63'),
('S0003','P0004','92'),
('S0003','P0005','70'),
('S0004','P0003','75'),
('S0004','P0004','88'),
('S0004','P0005','68'),
('S0005','P0005','95')
go
delete from*/
use MyDB
go

delete from ���u�� where �s��='S0001'
go

/*alter table */
use MyDB
go

alter table �P��� add constraint �s��
FOREIGN KEY(�s��) REFERENCES ���u��(�s��) ON UPDATE CASCADE ON DELETE CASCADE
go



