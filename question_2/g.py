import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_2")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("ALTER TABLE customer ADD COLUMN cust_dob date")
else:
    print("Not connected")