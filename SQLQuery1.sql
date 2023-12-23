/*use MyDB is important or you will save MyDB under SystemDatabase:master 
use MyDB
go*/

CREATE TABLE 教師資料表
(身份證字號  CHAR(10),
姓名  NVARCHAR(10) NOT NULL,
年資  INT,
學歷別  VARCHAR(10)NOT NULL,
電子郵件  VARCHAR(50)NOT NULL,
電話  VARCHAR(15),
生日  date NOT NULL,
帳號  VARCHAR(50)NOT NULL,
密碼  VARCHAR(50)NOT NULL,
職別  VARCHAR(10)NOT NULL,
始任職時間  date NOT NULL,
PRIMARY  KEY(身份證字號)
)
go

CREATE TABLE 學校資料表
(學校代碼  CHAR(10),
校名  NVARCHAR(20) NOT NULL,
設立別  VARCHAR(10)NOT NULL,
級別  VARCHAR(10)NOT NULL,
縣市  VARCHAR(10)NOT NULL,
區域  VARCHAR(10)NOT NULL,
路名  VARCHAR(10)NOT NULL,
電話  VARCHAR(15),
PRIMARY  KEY(學校代碼)
)
go

CREATE TABLE 活動資料表
(活動編號  CHAR(10),
活動標題  NVARCHAR(20) NOT NULL,
類型  VARCHAR(10)NOT NULL,
PRIMARY  KEY(活動編號)
)
go

CREATE TABLE 學校承辦活動資料表
(
主承辦日期  date NOT NULL,
活動編號  CHAR(10),
學校代碼  CHAR(10),
PRIMARY KEY(活動編號,學校代碼),
FOREIGN KEY(活動編號) REFERENCES 活動資料表(活動編號),
FOREIGN KEY(學校代碼) REFERENCES 學校資料表(學校代碼)
)
go

CREATE TABLE 教師活動參與紀錄
(
報名方式  VARCHAR(20),
時數  float NOT NULL,
階段  CHAR(10),
參加狀態  CHAR(10) NOT NULL,
活動編號  CHAR(10),
身份證字號  CHAR(10),
PRIMARY KEY(活動編號,身份證字號),
FOREIGN KEY(活動編號) REFERENCES 活動資料表(活動編號),
FOREIGN KEY(身份證字號) REFERENCES 教師資料表(身份證字號)
)
go

/*insert data into 教師資料表*/
INSERT INTO 教師資料表
VALUES  
('A123456789', '張三', 5, '博士', 'zhangsan@example.com', '0912345678', '1980-05-15', 'teacher1', 'password1', '專任教師', '2020-01-15'),
('B987654321', '李四', 8, '博士', 'lisi@example.com', '0923456789', '1975-09-20', 'teacher2', 'password2', '兼任講師', '2015-03-10'),
('C111223344', '王五', 3, '博士', 'wangwu@example.com', '0934567890', '1990-12-01', 'teacher3', 'password3', '助理教授', '2022-06-25'),
('D112233445', '蔡六', 6, '博士', 'cailiu@example.com', '0945678901', '1985-08-03', 'teacher4', 'password4', '專任講師', '2019-02-18'),
('E554433221', '陳七', 4, '博士', 'chenqi@example.com', '0956789012', '1988-11-12', 'teacher5', 'password5', '副教授', '2020-09-05'),
('F334455667', '林八', 7, '博士', 'linba@example.com', '0967890123', '1982-04-25', 'teacher6', 'password6', '專任教師', '2018-07-14'),
('G998877665', '吳九', 9, '博士', 'wuj@example.com', '0978901234', '1970-06-08', 'teacher7', 'password7', '教授', '2014-11-30'),
('H776655443', '董十', 5, '博士', 'dongshi@example.com', '0989012345', '1995-03-17', 'teacher8', 'password8', '助理教授', '2021-01-08'),
('I998877665', '朱十一', 8, '博士', 'zhushiyi@example.com', '0990123456', '1983-09-22', 'teacher9', 'password9', '專任教師', '2017-04-03'),
('J112233445', '馬十二', 6, '博士', 'mashier@example.com', '0912345678', '1980-05-15', 'teacher10', 'password10', '副教授', '2018-04-08')
go

INSERT INTO 學校資料表
VALUES 
('S123456789', '溪京大學', '公立', '大學', '台北市', '中正區', '中山路', '02-12345678'),
('S987654321', '南京大學', '私立', '大學', '新北市', '三峽區', '文化路', '02-23456789'),
('S111223344', '中華大學', '公立', '大學', '桃園市', '龍潭區', '中正路', '03-34567890'),
('S112233445', '中海大學', '私立', '大學', '台中市', '西屯區', '文心路', '04-45678901'),
('S554433221', '南投大學', '公立', '大學', '南投縣', '南投市', '中山路', '04-56789012'),
('S334455667', '高雄大學', '公立', '大學', '高雄市', '鳳山區', '文化路', '07-67890123'),
('S998877665', '基隆大學', '公立', '大學', '基隆市', '仁愛區', '中正路', '02-78901234'),
('S776655443', '新竹市立大學', '公立', '大學', '新竹市', '北區', '光復路', '03-89012345'),
('S198977995', '台南師範大學', '公立', '大學', '台南市', '安南區', '育樂街', '06-90123456'),
('S132223445', '東龍大學', '私立', '大學', '基隆市', '信義區', '中山路', '02-12345678')
go

INSERT INTO 活動資料表
VALUES 
('A1234', 'Python 基礎編程工作坊', '工作坊'),
('B5678', '教學技巧提升研討會', '研討會'),
('C9012', '數學教育新趨勢座談會', '座談會'),
('D3456', 'STEM 教育實踐研究班', '研究班'),
('E7890', '資訊科技在語言教學的應用工作坊', '工作坊')
go

INSERT INTO 學校承辦活動資料表
VALUES 
('2022-07-25', 'A1234', 'S198977995'),
('2023-01-12', 'B5678', 'S554433221'),
('2023-04-06', 'C9012', 'S111223344'),
('2023-06-15', 'D3456', 'S334455667'),
('2023-12-22', 'E7890', 'S198977995')
go

INSERT INTO 教師活動參與紀錄
VALUES 
('在線報名', 4.5, '初級', '已報名', 'E7890', 'I998877665'),
('現場報名', 6.0, '中級', '已參加', 'A1234', 'H776655443'),
('電子郵件報名', 3.5, '初級', '已報名', 'E7890', 'G998877665'),
('在線報名', 5.5, '高級', '已參加', 'D3456', 'E554433221'),
('現場報名', 4.0, '初級', '已參加', 'C9012', 'E554433221'),
('在線報名', 7.5, '初級', '已報名', 'E7890', 'J112233445'),
('電子郵件報名', 6.0, '高級', '已參加', 'D3456', 'J112233445'),
('現場報名', 3.5, '進階', '未參加', 'B5678', 'C111223344')
go

select *
from 教師資料表

SELECT A.身份證字號,A.姓名
FROM 教師資料表 AS A LEFT OUTER JOIN 教師活動參與紀錄 AS B
ON A.身份證字號=B.身份證字號
WHERE   B.身份證字號 IS NULL

SELECT A.活動標題 AS 活動名稱,B.活動編號, Count(*) AS 活動參與人數
FROM 活動資料表 AS A LEFT OUTER JOIN 教師活動參與紀錄 AS B
ON A.活動編號=B.活動編號
WHERE   B.身份證字號 IS NULL

SELECT 教師活動參與紀錄.活動編號, Count(*) AS 活動參與人數
FROM 教師活動參與紀錄
GROUP BY 活動編號





Select 姓名 AS 參與教師,電子郵件,活動標題,參加狀態
From 活動資料表,教師活動參與紀錄,教師資料表
Where 教師資料表.身份證字號=教師活動參與紀錄.身份證字號 and 活動資料表.活動編號=教師活動參與紀錄.活動編號
order by 姓名




SELECT 品號, Count(*) AS 銷售員工數
FROM 銷售表
GROUP BY 品號
ORDER BY 品號 DESC

/*
INSERT INTO 銷售表(編號,品號, 數量)
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

delete from 員工表 where 編號='S0001'
go

/*alter table */
use MyDB
go

alter table 銷售表 add constraint 編號
FOREIGN KEY(編號) REFERENCES 員工表(編號) ON UPDATE CASCADE ON DELETE CASCADE
go



