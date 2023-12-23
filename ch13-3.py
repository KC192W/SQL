#第十三章 Python結合SQL Server資料庫的應用

#ch13-1 Python如何連接SQL Server資料庫
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

def Query_Student():
 SQLcmd="select * from 員工表"
 Record=conn.execute(SQLcmd)
 listStudent=list(Record.fetchall())
 print("編號     姓名    部門")
 for row in listStudent:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()

def Query_Class():
 SQLcmd="select * from 產品表"
 Record=conn.execute(SQLcmd)
 listStudent=list(Record.fetchall())
 print("品號       品名      定價")
 for row in listStudent:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()

def Query_RecordDB():
 SQLcmd="select * from 銷售表"
 Record=conn.execute(SQLcmd)
 listStudent=list(Record.fetchall())
 print("編號      品號      數量")
 for row in listStudent:
    for col in row:
        print(col, end="   ")
    print()
 Record.close()
 
while True:
 print("===查詢系統===")
 print("1.查詢員工表")
 print("2.查詢產品表")
 print("3.查詢銷售表")
 print("4.結束系統")
 
 n=eval(input("請選擇功能清單："))
 if n==1:
    Query_Student()
 elif n==2:
    Query_Class()
 elif n==3:
    Query_RecordDB()
 elif n==4:
    print("離開本系統")
    break
 else:
    print("請選擇1~4項功能") 
conn.close()






