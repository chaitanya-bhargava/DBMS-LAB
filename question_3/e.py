import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_3")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("CREATE VIEW delhi_workers AS SELECT count(Employee_ID) FROM employee,department WHERE Location_ID = 11")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")