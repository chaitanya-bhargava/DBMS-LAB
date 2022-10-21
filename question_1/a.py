import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_1")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT sname FROM sailors WHERE sid IN (SELECT sid FROM reserves)")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")