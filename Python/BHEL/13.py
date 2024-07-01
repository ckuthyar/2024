import mysql.connector as mc

conn1=mc.connect(
    host="localhost",
    user="root",
    password="root",
    database="4mw20cs"
)
cr1=conn1.cursor()
cr1.execute("select * from employee")
rows=cr1.fetchall()
print(rows)
cr1.close()
conn1.close()

