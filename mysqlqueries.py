import mysql.connector as c
import datetime
con=c.connect(host="localhost",user="root",password="",database="csai")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("SELECT empid,empname,address,Dname,DATE_FORMAT(DDOB,'%d-%m-%Y'),DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),DDOB)),'%Y')+0 AS no_of_years,DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),DDOB)),'%c')+0 AS no_of_months,DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),DDOB)),'%d')+0 AS no_of_days FROM Employee NATURAL JOIN Dependants ORDER BY empid")
    myresult=mycursor.fetchall()
    for j in myresult:
        print(j)
else:
    print("Not connected")