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

print("連接MyDBMS資料庫---成功")
conn.close()
print("關閉MyDBMS資料庫")