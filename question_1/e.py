import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_1")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT sname FROM sailors WHERE rating > all( SELECT rating FROM SAILORS WHERE sname = 'John')")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")