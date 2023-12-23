#系統主畫面
import pyodbc
driver="{SQL Server}"
server="LAPTOP-9MVOJAMR"
database="教育資訊資料庫"
username=""
password=""
conn=pyodbc.connect("DRIVER=" + driver
                    + ";SERVER=" + server
                    + ";DATABASE=" + database
                    + ";UID=" + username
                    + ";PWD=" + password)

b=0
#主畫面
#------------------------------------------------------
def tc_Manager():  
 print("===「教師」管理系統===")
 print("1.新增教師記錄")
 print("2.修改教師記錄")
 print("3.刪除教師記錄")
 print("4.查詢教師記錄")
 print("5.回主畫面")
 n=eval(input("請選擇「教師」功能清單："))
 if n==1:
   Insert_tc()
 elif n==2:
   Update_tc()
 elif n==3:
   Delete_tc()   
 elif n==4:
   Query_tc()
 elif n==5:
    Main_Menu()
 else:
    print("請選擇1~5項功能")

def Check_Sid(Sid):
  SQLcmd="select * from 教師資料表 where 身份證字號='{}'".format(Sid)  
  cursor=conn.execute(SQLcmd)
  return cursor.fetchone()


def Insert_tc():
 Sid=input("身份證字號：")
 if Check_Sid(Sid)!=None:
    print("身份證字號:{}重複了".format(Sid))
    return
 A=input("姓名：")
 B=input("年資(年)：")
 C=input("學歷別：")
 D=input("電子郵件：")
 E=input("電話(手機)：")
 F=input("生日(YYYY-MM-DD)：")
 G=input("帳號：")
 H=input("密碼：")
 I=input("職別：")
 J=input("始任職時間(YYYY-MM-DD)：")
 SQLcmd="INSERT INTO 教師資料表 VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Sid,A,B,C,D,E,F,G,H,I,J)
 conn.execute(SQLcmd)
 conn.commit()
 print("新增教師記錄！")
 tc_Manager()

def Update_tc():
 Sid=input("身份證字號：")
 if Check_Sid(Sid)==None:
    print("查無此教師:{}".format(Sid))
    return
 A=input("姓名：")
 B=input("年資(年)：")
 C=input("學歷別：")
 D=input("電子郵件：")
 E=input("電話(手機)：")
 F=input("生日(YYYY-MM-DD)：")
 G=input("帳號：")
 H=input("密碼：")
 I=input("職別：")
 J=input("始任職時間(YYYY-MM-DD)：")
 SQLcmd="UPDATE 教師資料表 SET 姓名='{}',年資={},學歷別='{}',電子郵件='{}',電話='{}',生日='{}',帳號='{}',密碼='{}',職別='{}',始任職時間='{}' Where 身份證字號='{}'".format(A,B,C,D,E,F,G,H,I,J,Sid)
 conn.execute(SQLcmd)
 conn.commit()
 print("更新教師記錄！")
 tc_Manager()


def Delete_tc():
 Sid=input("身份證字號：")
 if Check_Sid(Sid)==None:
    print("查無此教師:{}".format(Sid))
    return
 SQLcmd="Delete From 教師資料表 WHERE 身份證字號='{}'".format(Sid)
 conn.execute(SQLcmd)
 conn.commit()
 print("刪除記錄成功！")
 tc_Manager()


def Query_tc():
 SQLcmd="select * from 教師資料表"
 Record=conn.execute(SQLcmd)
 listtc=list(Record.fetchall())
 column_names = ["身份證字號", "姓名", "年資", "學歷別", "電子郵件", "電話", "生日", "帳號", "密碼", "職別", "始任職時間"]
 print(f"{column_names[0]:<6} {column_names[1]:^3} {column_names[2]:^2} {column_names[3]:^4} {column_names[4]:^20} {column_names[5]:^10} {column_names[6]:^10} {column_names[7]:^10} {column_names[8]:^10} {column_names[9]:^5} {column_names[10]:^10}")
# 打印分隔線
 print("-" * 130)
# 打印數據行
 for row in listtc:
    print(f"{row[0]:^10} {row[1]:^4} {row[2]:^2} {row[3]:^5} {row[4]:^30} {row[5]:^10} {row[6]:^10} {row[7]:^10} {row[8]:^10} {row[9]:^5} {row[10]:^10}")
 Record.close()
 tc_Manager()
 
#------------------------------------------------------
def sc_Manager():  
 print("===「學校」管理系統===")
 print("1.新增學校記錄")
 print("2.修改學校記錄")
 print("3.刪除學校記錄")
 print("4.查詢學校記錄")
 print("5.回主畫面")
 n=eval(input("請選擇「學校」功能清單："))
 if n==1:
   Insert_sc()
 elif n==2:
   Update_sc()
 elif n==3:
   Delete_sc()   
 elif n==4:
   Query_sc()
 elif n==5:
    Main_Menu()
 else:
    print("請選擇1~5項功能")

def Check_Sid2(Sid2):
  SQLcmd="select * from 學校資料表 where 學校代碼='{}'".format(Sid2)  
  cursor=conn.execute(SQLcmd)
  return cursor.fetchone()


def Insert_sc():
 Sid2=input("學校代碼：")
 if Check_Sid2(Sid2)!=None:
    print("學校代碼:{}重複了".format(Sid2))
    return
 A=input("校名：")
 B=input("設立別：")
 C=input("級別：")
 D=input("縣市：")
 E=input("區域：")
 F=input("路名：")
 G=input("電話：")
 SQLcmd="INSERT INTO 學校資料表 VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(Sid2,A,B,C,D,E,F,G)
 conn.execute(SQLcmd)
 conn.commit()
 print("新增學校記錄！")
 sc_Manager()

def Update_sc():
 Sid2=input("學校代碼：")
 if Check_Sid2(Sid2)==None:
    print("查無此學校:{}".format(Sid2))
    return
 A=input("校名：")
 B=input("設立別：")
 C=input("級別：")
 D=input("縣市：")
 E=input("區域：")
 F=input("路名：")
 G=input("電話：")
 SQLcmd="UPDATE 學校資料表 SET 校名='{}',設立別='{}',級別='{}',縣市='{}',區域='{}',路名='{}',電話='{}' Where 學校代碼='{}'".format(A,B,C,D,E,F,G,Sid2)
 conn.execute(SQLcmd)
 conn.commit()
 print("更新學校記錄！")
 sc_Manager()


def Delete_sc():
 Sid2=input("學校代碼：")
 if Check_Sid2(Sid2)==None:
    print("查無此學校:{}".format(Sid2))
    return
 SQLcmd="Delete From 學校資料表 WHERE 學校代碼='{}'".format(Sid2)
 conn.execute(SQLcmd)
 conn.commit()
 print("刪除記錄成功！")
 sc_Manager()


def Query_sc():
 SQLcmd="select * from 學校資料表"
 Record=conn.execute(SQLcmd)
 listtc=list(Record.fetchall())
 print("學校代碼        校名     設立別 級別   縣市     區域     路名       電話          ")
 for row in listtc:
    print("{:^10} {:^10} {:^2} {:^3} {:^5} {:^5} {:^5} {:^15}".format(*row))
 Record.close()
 sc_Manager()


#------------------------------------------------------
def act_Manager():  
 print("===「活動」管理系統===")
 print("1.新增活動記錄")
 print("2.修改活動記錄")
 print("3.刪除活動記錄")
 print("4.查詢活動記錄")
 print("5.回主畫面")
 n=eval(input("請選擇「活動」功能清單："))
 if n==1:
   Insert_act()
 elif n==2:
   Update_act()
 elif n==3:
   Delete_act()   
 elif n==4:
   Query_act()
 elif n==5:
    Main_Menu()
 else:
    print("請選擇1~5項功能")

def Check_Sid3(Sid3):
  SQLcmd="select * from 活動資料表 where 活動編號='{}'".format(Sid3)  
  cursor=conn.execute(SQLcmd)
  return cursor.fetchone()


def Insert_act():
 Sid3=input("活動編號：")
 if Check_Sid3(Sid3)!=None:
    print("活動編號:{}重複了".format(Sid3))
    return
 A=input("活動標題：")
 B=input("類型：")
 SQLcmd="INSERT INTO 活動資料表 VALUES ('{}','{}','{}')".format(Sid3,A,B)
 conn.execute(SQLcmd)
 conn.commit()
 print("新增活動記錄！")
 act_Manager()

def Update_act():
 Sid3=input("活動編號：")
 if Check_Sid3(Sid3)==None:
    print("查無此活動:{}".format(Sid3))
    return
 A=input("活動標題：")
 B=input("類型：")
 SQLcmd="UPDATE 活動資料表 SET 活動標題='{}',類型='{}' Where 活動編號='{}'".format(A,B,Sid3)
 conn.execute(SQLcmd)
 conn.commit()
 print("更新活動記錄！")
 act_Manager()


def Delete_act():
 Sid3=input("活動編號：")
 if Check_Sid3(Sid3)==None:
    print("查無此活動:{}".format(Sid3))
    return
 SQLcmd="Delete From 活動資料表 WHERE 活動編號='{}'".format(Sid3)
 conn.execute(SQLcmd)
 conn.commit()
 print("刪除記錄成功！")
 act_Manager()


def Query_act():
 SQLcmd="select * from 活動資料表"
 Record=conn.execute(SQLcmd)
 listtc=list(Record.fetchall())
 print("活動編號    活動標題                    類型")
 for row in listtc:
    print("{:<10} {:<20} {:<5}".format(*row))
 Record.close()
 act_Manager()



#------------------------------------------------------
def aj_Selection():
 print("===「活動參與」記錄系統===")
 print("1.增加活動參與記錄")
 print("2.刪除活動參與記錄")
 print("3.查詢活動的參與記錄")
 print("4.查詢教師的參與記錄")
 print("5.回主畫面")
 n=eval(input("請選擇「活動參與」管理清單："))
 if n==1:
   Insert_aj()
 elif n==2:
   Delete_aj() 
 elif n==3:
   Query_aj1()
 elif n==4:
   Query_aj2()
 elif n==5:
    Main_Menu()
 else:
    print("請選擇1~5項功能")

def Checkaj_NO(Sid,No):  
  SQLcmd="select * from 教師活動參與紀錄 where 活動編號='{}' and 身份證字號='{}'".format(Sid,No)  
  cursor=conn.execute(SQLcmd)
  return cursor.fetchone()

def Insert_aj():
 print("=====請記錄活動參與資料=====") 
 Sid=input("活動編號：")
 No=input("身份證字號：")
 
 if Checkaj_NO(Sid,No)!=None:
    print("活動編號:{}和身份證字號:{}已經記錄過了！".format(Sid,No))
    return
 A=input("報名方式：")
 B=input("時數：")
 C=input("階段：")
 D=input("參加狀態：")
 SQLcmd="INSERT INTO 教師活動參與紀錄 VALUES ('{}','{}','{}','{}','{}','{}')".format(A,B,C,D,Sid,No)
 conn.execute(SQLcmd)
 conn.commit()
 print("記錄活動參與成功！")
 aj_Selection()

def Delete_aj():
 print("=====請退選=====") 
 Sid=input("活動編號：")
 No=input("身份證字號：")
 if Checkaj_NO(Sid,No)==None:
    print("查無此紀錄--活動編號:{} & 身份證字號:{}".format(Sid,No))
    return
 SQLcmd="Delete From 教師活動參與紀錄 WHERE 活動編號='{}' and 身份證字號='{}'".format(Sid,No)
 conn.execute(SQLcmd)
 conn.commit()
 print("活動參與紀錄刪除成功！")
 aj_Selection()


def Query_aj1():
 Sid=input("活動編號：")
 if Sid=='*':
     SQLcmd="select A.活動編號,A.活動標題,A.類型,C.姓名,B.報名方式,B.時數,B.階段,B.參加狀態 "
     SQLcmd=SQLcmd + "from 活動資料表 AS A,教師活動參與紀錄 AS B,教師資料表 AS C "
     SQLcmd=SQLcmd + "Where A.活動編號=B.活動編號 and B.身份證字號=C.身份證字號 "
 else:
     SQLcmd="select A.活動編號,A.活動標題,A.類型,C.姓名,B.報名方式,B.時數,B.階段,B.參加狀態 "
     SQLcmd=SQLcmd + "from 活動資料表 AS A,教師活動參與紀錄 AS B,教師資料表 AS C "
     SQLcmd=SQLcmd + "Where A.活動編號=B.活動編號 and B.身份證字號=C.身份證字號 "
     SQLcmd=SQLcmd + "And A.活動編號='{}'".format(Sid)
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("活動編號      活動標題               類型    參與教師    報名方式       時數   階段   參加狀態")
 for row in listProduct:
    print("{:<10} {:<20} {:<5} {:<5} {:<8} {:<4} {:<2} {:<5}".format(*row))
 Record.close()
 aj_Selection()
def Query_aj2():
 NO=input("身份證字號：")
 if NO=='*':
     SQLcmd="select C.姓名,B.報名方式,B.時數,B.階段,B.參加狀態,A.活動編號,A.活動標題,A.類型 "
     SQLcmd=SQLcmd + "from 活動資料表 AS A,教師活動參與紀錄 AS B,教師資料表 AS C "
     SQLcmd=SQLcmd + "Where A.活動編號=B.活動編號 and B.身份證字號=C.身份證字號 "
     SQLcmd=SQLcmd + "order by C.姓名 "
 else:
     SQLcmd="select C.姓名,B.報名方式,B.時數,B.階段,B.參加狀態,A.活動編號,A.活動標題,A.類型 "
     SQLcmd=SQLcmd + "from 活動資料表 AS A,教師活動參與紀錄 AS B,教師資料表 AS C "
     SQLcmd=SQLcmd + "Where A.活動編號=B.活動編號 and B.身份證字號=C.身份證字號 "
     SQLcmd=SQLcmd + "And C.身份證字號='{}'".format(NO)
     SQLcmd=SQLcmd + "order by C.姓名 "
 
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 column_names = ["參與教師", "報名方式", "時數", "階段", "參加狀態","活動編號", "活動名稱", "類型"]
 print(f"{column_names[0]:^5} {column_names[1]:^4} {column_names[2]:^3} {column_names[3]:^5} {column_names[4]:^5} {column_names[5]:^6} {column_names[6]:^20} {column_names[7]:^5}")
# 打印分隔線
 print("-" * 90)

# 打印數據行
 for row in listProduct:
    print(f"{row[0]:^5} {row[1]:^7} {row[2]:^3} {row[3]:^2} {row[4]:^3} {row[5]:^5} {row[6]:^15} {row[7]:^5}")
 Record.close()
 aj_Selection()
#------------------------------------------------------
def ajb_Selection():
 print("===「承辦活動」記錄系統===")
 print("1.增加承辦活動記錄")
 print("2.刪除承辦活動記錄")
 print("3.查詢活動的承辦記錄")
 print("4.查詢學校的承辦記錄")
 print("5.回主畫面")
 n=eval(input("請選擇「承辦活動」管理清單："))
 if n==1:
   Insert_ajb()
 elif n==2:
   Delete_ajb() 
 elif n==3:
   Query_ajb1()
 elif n==4:
   Query_ajb2()
 elif n==5:
    Main_Menu()
 else:
    print("請選擇1~5項功能")

def Checkajb_NO(Sid,No):  
  SQLcmd="select * from 學校承辦活動資料表 where 活動編號='{}' and 學校代碼='{}'".format(Sid,No)  
  cursor=conn.execute(SQLcmd)
  return cursor.fetchone()

def Insert_ajb():
 print("=====請記錄承辦活動資料=====") 
 Sid=input("活動編號：")
 No=input("學校代碼：")
 
 if Checkajb_NO(Sid,No)!=None:
    print("活動編號:{}和學校代碼:{}已經記錄過了！".format(Sid,No))
    return
 A=input("主承辦日期(YYYY-MM-DD)：")
 SQLcmd="INSERT INTO 教師活動參與紀錄 VALUES ('{}','{}','{}')".format(A,Sid,No)
 conn.execute(SQLcmd)
 conn.commit()
 print("記錄承辦活動成功！")
 ajb_Selection()

def Delete_ajb():
 print("=====請退選=====") 
 Sid=input("活動編號：")
 No=input("學校代碼：")
 if Checkajb_NO(Sid,No)==None:
    print("查無此紀錄--活動編號:{} & 學校代碼:{}".format(Sid,No))
    return
 SQLcmd="Delete From 學校承辦活動資料表 WHERE 活動編號='{}' and 學校代碼='{}'".format(Sid,No)
 conn.execute(SQLcmd)
 conn.commit()
 print("承辦活動紀錄刪除成功！")
 ajb_Selection()

def Query_ajb1():
 Sid=input("活動編號：")
 if Sid=='*':
     SQLcmd="select C.校名,B.主承辦日期,A.活動編號,A.活動標題,A.類型 "
     SQLcmd=SQLcmd + "from 活動資料表 AS A,學校承辦活動資料表 AS B,學校資料表 AS C "
     SQLcmd=SQLcmd + "Where A.活動編號=B.活動編號 and B.學校代碼=C.學校代碼 "
 else:
     SQLcmd="select C.校名,B.主承辦日期,A.活動編號,A.活動標題,A.類型 "
     SQLcmd=SQLcmd + "from 活動資料表 AS A,學校承辦活動資料表 AS B,學校資料表 AS C "
     SQLcmd=SQLcmd + "Where A.活動編號=B.活動編號 and B.學校代碼=C.學校代碼 "
     SQLcmd=SQLcmd + "And A.活動編號='{}'".format(Sid)
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("承辦學校       日期      活動編號      活動標題                       類型    ")
 for row in listProduct:
    print("{:<8} {:<10} {:<10} {:<20} {:<5}".format(*row))
 Record.close()
 ajb_Selection()
def Query_ajb2():
 NO=input("學校代碼：")
 if NO=='*':
     SQLcmd="select C.校名,B.主承辦日期,A.活動編號,A.活動標題,A.類型 "
     SQLcmd=SQLcmd + "from 活動資料表 AS A,學校承辦活動資料表 AS B,學校資料表 AS C "
     SQLcmd=SQLcmd + "Where A.活動編號=B.活動編號 and B.學校代碼=C.學校代碼 "
 else:
     
     SQLcmd="select C.校名,B.主承辦日期,A.活動編號,A.活動標題,A.類型 "
     SQLcmd=SQLcmd + "from 活動資料表 AS A,學校承辦活動資料表 AS B,學校資料表 AS C "
     SQLcmd=SQLcmd + "Where A.活動編號=B.活動編號 and B.學校代碼=C.學校代碼 "
     SQLcmd=SQLcmd + "And C.學校代碼='{}'".format(NO)
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("承辦學校       日期      活動編號      活動標題                       類型    ")
 for row in listProduct:
    print("{:<8} {:<10} {:<10} {:<20} {:<5}".format(*row))
 Record.close()
 ajb_Selection()

def ot():
 print("=====進階查詢=====")
 print("1.所有未參加活動的教師")
 print("2.所有活動的參與人數")
 print("3.回主畫面")
 n=eval(input("請選擇功能清單："))
 if n==1:
   ot1()
 elif n==2:
   ot2()
 elif n==3:
    Main_Menu()
def ot1():
    SQLcmd="SELECT A.身份證字號,A.姓名 FROM 教師資料表 AS A LEFT OUTER JOIN 教師活動參與紀錄 AS B ON A.身份證字號=B.身份證字號 WHERE   B.身份證字號 IS NULL"
    Record=conn.execute(SQLcmd)
    listProduct=list(Record.fetchall())
    print("身份證字號  姓名   ")
    for row in listProduct:
       print("{:<10} {:<4}".format(*row))
    Record.close()
    ot()
def ot2():
    SQLcmd="SELECT 教師活動參與紀錄.活動編號, Count(*) AS 活動參與人數 FROM 教師活動參與紀錄 GROUP BY 活動編號"
    Record=conn.execute(SQLcmd)
    listProduct=list(Record.fetchall())
    print("活動編號   活動參與人數")
    for row in listProduct:
       print("{:<10} {:<3}".format(*row))
    Record.close()
    ot()
def Main_Menu():  
 print("=====教育資訊系統=====")
 print("1.「教師」管理系統")
 print("2.「學校」管理系統")
 print("3.「活動」管理系統") 
 print("4.「活動參與」記錄系統")
 print("5.「承辦活動」記錄系統")
 print("6. 進階查詢")
 print("7. 結束系統")
 n=eval(input("請選擇功能清單："))
 if n==1:
   tc_Manager()
 elif n==2:
   sc_Manager()
 elif n==3:
   act_Manager()  
 elif n==4:
   aj_Selection()
 elif n==5:
   ajb_Selection()
 elif n==6:
   ot()
 elif n==7:
   global b
   b=1

while b==0:
  Main_Menu()  #呼叫主選單畫面

print("離開本系統")
conn.close()