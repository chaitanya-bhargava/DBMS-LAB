import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_1")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT sname FROM sailors s WHERE NOT EXISTS(SELECT * FROM boats b WHERE NOT EXISTS(SELECT * FROM reserves r WHERE r.sid = s.sid AND r.bid = b.bid))")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")