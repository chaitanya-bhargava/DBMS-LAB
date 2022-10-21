import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_1")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT sname,TIMESTAMPDIFF(YEAR,date_of_birth,NOW()) AS age FROM SAILORS WHERE date_of_birth <= ALL(SELECT date_of_birth FROM sailors)")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")