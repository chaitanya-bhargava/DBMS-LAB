import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_3")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT count(Employee_ID) FROM employee WHERE hire_date BETWEEN '2015-03-01' AND '2015-03-31'")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")