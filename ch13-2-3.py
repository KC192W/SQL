#===============程式描述=================
#程式名稱：ch13-2-3.py   
#程式目的：修改「員工表」記錄
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

SQLcmd="UPDATE 員工表 SET 部門= '生產部' WHERE 編號='S0006'"
conn.execute(SQLcmd)
conn.commit()
print("更新員工記錄！")
conn.close()
