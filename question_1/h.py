import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_1")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT rating,MIN(TIMESTAMPDIFF(YEAR,date_of_birth,NOW())) AS min_age FROM sailors GROUP BY rating HAVING count(*)>=2")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")