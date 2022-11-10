import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_2")
if con.is_connected() :
    mycursor=con.cursor()
    query="CREATE TRIGGER gold AFTER UPDATE ON customer FOR EACH ROW INSERT INTO gold_customer(SELECT cust_num,cust_lname,cust_fname FROM customer WHERE cust_num = NEW.cust_num AND cust_balance > 1000000 AND cust_num NOT IN(SELECT cust_num FROM gold_customer))"
    mycursor.execute(query)
else:
    print("Not connected")