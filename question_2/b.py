import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_2")
if con.is_connected() :
    mycursor=con.cursor()
    query="CREATE TRIGGER update_cust_bal BEFORE INSERT ON invoice FOR EACH ROW UPDATE customer cust SET cust.cust_balance = cust.cust_balance+ NEW.inv_amount WHERE cust.cust_num=NEW.cust_num"
    mycursor.execute(query)
else:
    print("Not connected")