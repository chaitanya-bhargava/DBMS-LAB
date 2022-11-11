import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_2")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("CREATE TABLE customer(cust_num int PRIMARY KEY,cust_lname varchar(30),cust_fname varchar(30) NOT NULL,cust_balance int)")
    mycursor.execute("CREATE TABLE product(prod_num int PRIMARY KEY,prod_name varchar(10) NOT NULL,price int NOT NULL)")
    mycursor.execute("CREATE TABLE invoice(inv_num int PRIMARY KEY,prod_num int,cust_num int,inv_date date NOT NULL,unit_sold int NOT NULL,inv_amount int NOT NULL,PRIMARY KEY(inv_num,prod_num,cust_num,inv_date),FOREIGN KEY (prod_num) REFERENCES product(prod_num),FOREIGN KEY (cust_num) REFERENCES customer(cust_num))")
    mycursor.execute("INSERT INTO customer VALUES(101,'Bhargava','Chaitanya',120000),(102,'Uppal','Saksham',60000),(103,'Kumar','Ankit',10000),(104,'Goyal','Aryan',40000),(105,'Dagar','Harsh',27000),(106,'Raval','Mann',0),(107,'Chhabra','Aayush',90000),(108,'Singh','Aadit',90000)")
    mycursor.execute("INSERT INTO product VALUES(1,'TV',50000),(2,'Washing Machine',30000),(3,'Mobile Phone',80000),(4,'XBOX',20000),(5,'Air Conditioner',45000),(6,'Nintendo 3DS',15000),(7,'Laptop',90000),(8,'PlayStation 5',90000)")
    mycursor.execute("INSERT INTO invoice VALUES(12345,2,101,'2022-10-18',2,60000),(12346,4,102,'2022-10-17',3,60000),(12347,1,103,'2022-10-16',3,80000),(12348,1,104,'2022-10-15',4,200000),(12349,5,105,'2022-10-14',6,270000),(12350,5,108,'2022-09-07',1,60000),(12351,4,107,'2022-10-17',3,80000),(12352,8,101,'2022-10-02',2,60000)")
    con.commit()
else:
    print("Not connected")