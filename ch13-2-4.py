#===============程式描述=================
#程式名稱：ch13-2-4.py   
#程式目的：刪除「員工表」記錄
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

SQLcmd="Delete From 員工表 WHERE 編號='S0006'"
conn.execute(SQLcmd)
conn.commit()
print("刪除記錄成功！")
conn.close()
