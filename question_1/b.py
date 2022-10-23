import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_1")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT sname FROM sailors WHERE sid IN (SELECT r.sid FROM boats b,reserves r WHERE r.bid = b.bid AND b.colour = 'red' AND (SELECT extract(month from r.day)='03') UNION SELECT r2.sid FROM boats b2, reserves r2 WHERE r2.bid = b2.bid AND b2.colour = 'green' AND (SELECT extract(month from r2.day)='03'))")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")