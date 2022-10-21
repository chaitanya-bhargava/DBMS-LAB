import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_2")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT cust_fname FROM customer WHERE cust_balance = 0")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")