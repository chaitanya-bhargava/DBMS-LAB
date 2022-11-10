import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_3")
if con.is_connected() :
    mycursor=con.cursor()
    query="CREATE TRIGGER age BEFORE INSERT ON employee FOR EACH ROW BEGIN IF TIMESTAMPDIFF(YEAR,NEW.DOB,NOW()) < 25 THEN SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Minimum age must be 25 years'; END IF; END"
    mycursor.execute(query)
else:
    print("Not connected")