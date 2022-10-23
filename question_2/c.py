import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_2")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT cust_num,cust_fname FROM customer WHERE cust_num IN (SELECT cust_num FROM invoice GROUP BY cust_num,inv_date, prod_num HAVING sum(unit_sold) > 3)")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")