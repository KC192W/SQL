#===============程式描述=================
#程式名稱：ch13-2-1.py   
#程式目的：查詢「員工表」記錄
#=======================================
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

SQLcmd="select * from 員工表"
Record=conn.execute(SQLcmd)
ListStudent=list(Record.fetchall())
print("編號     姓名    部門")
print("-----------------------")
for row in ListStudent:
    for col in row:
        print(col, end="   ")
    print()
Record.close()
conn.close()

