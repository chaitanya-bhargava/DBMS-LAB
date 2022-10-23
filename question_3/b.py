import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_3")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT * FROM employee GROUP BY Salary ORDER BY Salary DESC LIMIT 1")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")