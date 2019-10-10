import os
import cx_Oracle


# connection = cx_Oracle.connect("orcl", 'B1259', "jdbc:oracle:thin:@192.168.63.144:1521:orcl", encoding="UTF-8")

conn_str = u'B1259/B1259@192.168.63.144:1521/orcl'
connection = cx_Oracle.connect(conn_str)

cur = connection.cursor()
cur.execute("SELECT * from students")
col = cur.fetchall()
cur.close()
connection.close()

for i in col:
    print(i)