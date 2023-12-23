#===============程式描述=================
#程式名稱：ch13-2-2.py   
#程式目的：新增「員工表」記錄
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


SQLcmd="INSERT INTO 員工表 VALUES ('S0006','六合','銷售部')"
conn.execute(SQLcmd)
conn.commit()
print("新增員工記錄！")
conn.close()