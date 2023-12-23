#13-3-6 員工銷售系統主畫面
import pyodbc
driver="{SQL Server}"
server="LAPTOP-9MVOJAMR"
database="MyDB"
username=""
password=""
conn=pyodbc.connect("DRIVER=" + driver
                    + ";SERVER=" + server
                    + ";DATABASE=" + database
                    + ";UID=" + username
                    + ";PWD=" + password)

b=0
#「員工」管理系統之主畫面
#------------------------------------------------------
def Staff_Manager():  
 print("===「員工」管理系統===")
 print("1.新增員工記錄")
 print("2.修改員工記錄")
 print("3.刪除員工記錄")
 print("4.查詢員工記錄")
 print("5.回主畫面")
 n=eval(input("請選擇「員工」功能清單："))
 if n==1:
   Insert_Staff()
 elif n==2:
   Update_Staff()
 elif n==3:
   Delete_Staff()   
 elif n==4:
   Query_Staff()
 elif n==5:
    Main_Menu()
 else:
    print("請選擇1~5項功能")

def Check_Sid(Sid): #檢查編號是否存在於員工表中之副程式
  SQLcmd="select * from 員工表 where 編號='{}'".format(Sid)  
  cursor=conn.execute(SQLcmd)
  return cursor.fetchone()  #若無記錄則傳回None


def Insert_Staff(): #新增員工記錄
 Sid=input("編號：")
 if Check_Sid(Sid)!=None:
    print("編號:{}重複了".format(Sid))
    return
 Sname=input("姓名：")
 Dept=input("部門：")
 SQLcmd="INSERT INTO 員工表 VALUES ('{}','{}','{}')".format(Sid,Sname,Dept)
 conn.execute(SQLcmd)
 conn.commit()
 print("新增員工記錄！")
 Staff_Manager() #返回到「員工」管理系統之主畫面

def Update_Staff():  #修改員工記錄
 Sid=input("編號：")
 if Check_Sid(Sid)==None:
    print("查無此編號:{}".format(Sid))
    return
 Sname=input("姓名：")
 Dept=input("部門：")
 SQLcmd="UPDATE 員工表 SET 姓名='{}',部門='{}' Where 編號='{}'".format(Sname,Dept,Sid)
 conn.execute(SQLcmd)
 conn.commit()
 print("更新員工記錄！")
 Staff_Manager()   #返回到「員工」管理系統之主畫面


def Delete_Staff(): #刪除員工記錄
 Sid=input("編號：")
 if Check_Sid(Sid)==None:
    print("查無此編號:{}".format(Sid))
    return
 SQLcmd="Delete From 員工表 WHERE 編號='{}'".format(Sid)
 conn.execute(SQLcmd)
 conn.commit()
 print("刪除記錄成功！")
 Staff_Manager()  #返回到「員工」管理系統之主畫面


def Query_Staff():  #查詢員工記錄
 SQLcmd="select * from 員工表"
 Record=conn.execute(SQLcmd)
 listStaff=list(Record.fetchall())
 print("編號    姓名    部門")
 for row in listStaff:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 Staff_Manager()  #返回到「員工」管理系統之主畫面
 
 
#「產品」管理系統之主畫面
#------------------------------------------------------
def Product_Manager():  #「產品」管理系統之主畫面
 print("===「產品」管理系統===")
 print("1.新增產品記錄")
 print("2.修改產品記錄")
 print("3.刪除產品記錄")
 print("4.查詢產品記錄")
 print("5.回主畫面")
 n=eval(input("請選擇「產品」功能清單："))
 if n==1:
   Insert_Product()  #新增產品記錄
 elif n==2:
   Update_Product()  #修改產品記錄
 elif n==3:
   Delete_Product()  #刪除產品記錄
 elif n==4:
   Query_Product()   #查詢產品記錄
 elif n==5:
    Main_Menu()      #回主畫面
 else:
    print("請選擇1~5項功能")


def CheckProduct_NO(No):
  SQLcmd="select * from 產品表 where 品號='{}'".format(No)  
  cursor=conn.execute(SQLcmd)
  return cursor.fetchone()  #若無記錄則傳回None

def Insert_Product():   #新增產品記錄
 No=input("品號：")
 if CheckProduct_NO(No)!=None:
    print("編號:{}重複了".format(No))
    return
 Cname=input("品名：")
 Credits=input("定價：")
 SQLcmd="INSERT INTO 產品表 VALUES ('{}','{}','{}')".format(No,Cname,Credits)
 conn.execute(SQLcmd)
 conn.commit()
 print("新增產品記錄！")
 Product_Manager()  #返回到「產品」管理系統之主畫面

def Update_Product():  #修改產品記錄
 No=input("品號：")
 if CheckProduct_NO(No)==None:
    print("查無此品號:{}".format(No))
    return
 Cname=input("品名：")
 Credits=input("定價：")
 SQLcmd="UPDATE 產品表 SET 品名='{}',定價='{}' Where 品號='{}'".format(Cname,Credits,No)
 conn.execute(SQLcmd)
 conn.commit()
 print("更新產品記錄！")
 Product_Manager()  #返回到「產品」管理系統之主畫面


def Delete_Product():  #刪除產品記錄
 No=input("品號：")
 if CheckProduct_NO(No)==None:
    print("查無此品號:{}".format(No))
    return
 SQLcmd="Delete From 產品表 WHERE 品號='{}'".format(No)
 conn.execute(SQLcmd)
 conn.commit()
 print("刪除記錄成功！")
 Product_Manager()  #返回到「產品」管理系統之主畫面

def Query_Product():  #查詢產品記錄
 SQLcmd="select * from 產品表"
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("品號    品名    定價")
 for row in listProduct:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 Product_Manager() #返回到「產品」管理系統之主畫面

#「銷售」管理系統之主畫面
#------------------------------------------------------
def Sales_Selection(): #「銷售」管理系統之主畫面
 print("===「銷售」管理系統===")
 print("1.增加銷售歷程記錄")
 print("2.刪除銷售歷程記錄")
 print("3.查詢銷售歷程記錄")
 print("4.回主畫面")
 n=eval(input("請選擇「銷售」管理清單："))
 if n==1:
   Insert_Sales()  #增加銷售歷程記錄
 elif n==2:
   Delete_Sales()  #刪除銷售歷程記錄   
 elif n==3:
   Query_Sales()   #查詢銷售歷程記錄
 elif n==4:
    Main_Menu()     #回主畫面
 else:
    print("請選擇1~5項功能")

def CheckSales_NO(Sid,No):  
  SQLcmd="select * from 銷售表 where 編號='{}' and 品號='{}'".format(Sid,No)  
  cursor=conn.execute(SQLcmd)
  return cursor.fetchone()  #若無記錄則傳回None

def Insert_Sales():  #增加銷售歷程記錄
# Query_Product_2()  #查詢目前的產品
 print("=====請記錄銷售資料=====") 
 Sid=input("編號：")
 No=input("品號：")
 Count=input("數量：")
 if CheckSales_NO(Sid,No)!=None:
    print("品號:{}重複選了".format(No))
    return
 SQLcmd="INSERT INTO 銷售表 VALUES ('{}','{}','{}')".format(Sid,No,Count)
 conn.execute(SQLcmd)
 conn.commit()
 print("記錄銷售成功！")
 Sales_Selection() #返回到「銷售」管理系統之主畫面

def Delete_Sales(): #刪除銷售歷程記錄
# Query_Product_2()  #查詢目前的產品
 print("=====請退選=====") 
 Sid=input("編號：")
 No=input("品號：")
 if CheckSales_NO(Sid,No)==None:
    print("查無此品號:{}".format(No))
    return
 SQLcmd="Delete From 銷售表 WHERE 編號='{}' and 品號='{}'".format(Sid,No)
 conn.execute(SQLcmd)
 conn.commit()
 print("退銷成功！")
 Sales_Selection() #返回到「銷售」管理系統之主畫面


def Query_Sales():  #查詢銷售歷程記錄
 Sid=input("編號：")
 SQLcmd="select A.編號,A.姓名,C.品號,品名,定價,B.數量 "
 SQLcmd=SQLcmd + "from 員工表 AS A,銷售表 AS B,產品表 AS C "
 SQLcmd=SQLcmd + "Where A.編號=B.編號 and B.品號=C.品號 "
 SQLcmd=SQLcmd + "And A.編號='{}'".format(Sid)
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("編號      姓名     品號     品名    定價       數量")
 for row in listProduct:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 Sales_Selection() #返回到「銷售」管理系統之主畫面



#「查詢」銷售記錄系統之主畫面
#------------------------------------------------------
def Query_Product_Record():
 print("===「查詢」銷售記錄===")
 print("1.查詢各位員工銷售種類數")
 print("2.查詢每種產品銷售數")
 print("3.查詢每位員工銷售平均數量")
 print("4.查詢每種產品平均銷售數")
 print("5.查詢員工銷售記錄資料")
 print("6.查詢必推銷品(全部選)")
 print("7.回主畫面")
 n=eval(input("請選擇「查詢」銷售清單："))
 if n==1:
   Query1()      #呼叫「查詢各位員工銷售種類數」
 elif n==2:
   Query2()      #呼叫「查詢每種產品銷售數」
 elif n==3:
   Query3()      #呼叫「查詢每位員工銷售平均數量」
 elif n==4:
   Query4()      #呼叫「查詢每種產品平均銷售數」
 elif n==5:
   Query5()      #呼叫「查詢員工銷售記錄資料」
 elif n==6:
   Query6()      #呼叫「查詢必推銷品(全部選)」
 elif n==7:
    Main_Menu()  #呼叫「回主畫面」
 else:
    print("請選擇1~7項功能")

def Query1():  #定義「查詢各位員工銷售種類數」之副程式
 SQLcmd="SELECT A.編號,姓名,Count(*) AS 銷售種類數 "
 SQLcmd=SQLcmd + "FROM 員工表 AS A,銷售表 AS B "
 SQLcmd=SQLcmd + "Where A.編號=B.編號 "
 SQLcmd=SQLcmd + "GROUP BY A.編號,姓名"
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("編號   姓名   銷售種類數")
 print("------------------------")
 for row in listProduct:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 Query_Product_Record()   #返回到查詢銷售記錄主畫面

def Query2(): #定義「查詢每種產品銷售數」之副程式
 SQLcmd="SELECT A.品號,品名,Count(*) AS 銷售數 "
 SQLcmd=SQLcmd + "FROM 產品表 AS A,銷售表 AS B "
 SQLcmd=SQLcmd + "Where A.品號=B.品號 "
 SQLcmd=SQLcmd + "GROUP BY A.品號,品名"
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("品號   品名   銷售數")
 print("------------------------")
 for row in listProduct:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 Query_Product_Record()   #返回到查詢銷售記錄主畫面

def Query3(): #定義「查詢每位員工銷售平均數量」之副程式
 SQLcmd="SELECT A.編號,姓名,Count(*) AS 選科目數,AVG(數量) AS 銷售平均數量 "
 SQLcmd=SQLcmd + "FROM 員工表 AS A,銷售表 AS B "
 SQLcmd=SQLcmd + "Where A.編號=B.編號 "
 SQLcmd=SQLcmd + "GROUP BY A.編號,姓名"
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("編號   姓名   種類   平均數量")
 print("------------------------")
 for row in listProduct:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 Query_Product_Record()   #返回到查詢銷售記錄主畫面


def Query4(): #定義「查詢每種產品平均銷售數」之副程式
 SQLcmd="SELECT A.品號,品名,Count(*) AS 選修人數,AVG(數量) AS 平均銷售數 "
 SQLcmd=SQLcmd + "FROM 產品表 AS A,銷售表 AS B "
 SQLcmd=SQLcmd + "Where A.品號=B.品號 "
 SQLcmd=SQLcmd + "GROUP BY A.品號,品名"
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("品號   品名   員工數  平均銷售數")
 print("------------------------")
 for row in listProduct:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 Query_Product_Record()   #返回到查詢銷售記錄主畫面


def Query5():  #定義「查詢員工銷售記錄資料」之副程式
 SQLcmd="SELECT A.編號,姓名,品名,數量 "
 SQLcmd=SQLcmd + "FROM 員工表 AS A,銷售表 AS B,產品表 AS C "
 SQLcmd=SQLcmd + "Where A.編號=B.編號 And C.品號=B.品號 "
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("編號   姓名    品名   數量")
 print("-----------------------------")
 for row in listProduct:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 Query_Product_Record()   #返回到查詢銷售記錄主畫面

def Query6(): #定義「查詢必推銷品」之副程式
 SQLcmd="SELECT 品名 "
 SQLcmd=SQLcmd + "FROM 產品表 As C "
 SQLcmd=SQLcmd + "WHERE NOT EXISTS(  "
 SQLcmd=SQLcmd + "SELECT * "
 SQLcmd=SQLcmd + "FROM 員工表 As A "
 SQLcmd=SQLcmd + "WHERE NOT EXISTS( "
 SQLcmd=SQLcmd + "SELECT * "
 SQLcmd=SQLcmd + "FROM 銷售表 As B " 
 SQLcmd=SQLcmd + "WHERE C.品號=B.品號 AND A.編號=B.編號))"
 Record=conn.execute(SQLcmd)
 listProduct=list(Record.fetchall())
 print("品名")
 print("---------")
 for row in listProduct:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 Query_Product_Record()  #返回到查詢銷售記錄主畫面


def Main_Menu():  
 print("=====員工銷售系統=====")
 print("1.「員工」管理系統")
 print("2.「產品」管理系統")
 print("3.「銷售」管理系統") 
 print("4.「查詢」銷售記錄")
 print("5. 結束系統")
 n=eval(input("請選擇功能清單："))
 if n==1:
   Staff_Manager()        #呼叫「員工」管理系統
 elif n==2:
   Product_Manager()        #呼叫「產品」管理系統
 elif n==3:
   Sales_Selection()       #呼叫「銷售」管理系統   
 elif n==4:
   Query_Product_Record()   #呼叫「查詢」銷售記錄
 elif n==5:
   global b
   b=1

while b==0:
  Main_Menu()  #呼叫主選單畫面

print("離開本系統")
conn.close()