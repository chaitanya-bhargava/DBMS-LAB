import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="question_1")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT DISTINCT sname FROM sailors s1, reserves r1, boats b1,reserves r2, boats b2 WHERE s1.sid = r1.sid AND r1.bid = b1.bid AND s1.sid = r2.sid AND r2.bid = b2.bid AND b1.colour = 'red' AND b2.colour = 'green'")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")