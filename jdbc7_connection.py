import jaydebeapi as jdbc



conn = jdbc.connect("oracle.jdbc.driver.OracleDriver","jdbc:oracle:thin:@192.168.63.144:1521:orcl",["B1259","B1259"],"C:\Program Files\Java\jre1.8.0_201\lib\ext\ojdbc7.jar")
print("Connected!!")

curs = conn.cursor()


curs.execute("select * from students")

a = curs.fetchall()

for i in a:
	print(i)