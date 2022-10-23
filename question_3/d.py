import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_3")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT Department_ID FROM employee GROUP BY Department_ID ORDER BY sum(Salary) DESC LIMIT 1")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")