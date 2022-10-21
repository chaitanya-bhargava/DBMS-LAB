import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_2")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT cust.cust_num,cust.cust_fname,cust.cust_lname,inv.inv_amount FROM customer cust LEFT OUTER JOIN invoice inv ON cust.cust_num =  inv.cust_num")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
    print("\n")
    mycursor.execute("SELECT cust.cust_num,cust.cust_fname,cust.cust_lname,inv.inv_amount FROM customer cust RIGHT OUTER JOIN invoice inv ON cust.cust_num =  inv.cust_num")
    myresult=mycursor.fetchall()
    for i in myresult:
        print(i)
    print("\n")
    mycursor.execute("(SELECT cust.cust_num,cust.cust_fname,cust.cust_lname,inv.inv_amount FROM customer cust LEFT OUTER JOIN invoice inv ON cust.cust_num =  inv.cust_num) UNION (SELECT cust.cust_num,cust.cust_fname,cust.cust_lname,inv.inv_amount FROM customer cust RIGHT OUTER JOIN invoice inv ON cust.cust_num =  inv.cust_num)")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")