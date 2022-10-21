import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_2")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT inv_date,sum(unit_sold) as total_sales FROM invoice GROUP BY inv_date")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")