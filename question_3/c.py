import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_3")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT sum(Salary),Department_ID FROM employee GROUP BY Department_ID")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")