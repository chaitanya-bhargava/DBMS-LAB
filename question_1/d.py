import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_1")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT sid FROM sailors WHERE sid NOT IN (SELECT sid FROM reserves WHERE day>= '2018-01-01')")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")