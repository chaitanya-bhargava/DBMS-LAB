import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_3")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("CREATE TABLE department(Department_id int PRIMARY KEY,Name varchar(25) NOT NULL,Location_ID int NOT NULL)")
    mycursor.execute("CREATE TABLE job(Job_ID int PRIMARY KEY,Function varchar(30) NOT NULL)")
    mycursor.execute("CREATE TABLE employee(Employee_ID int PRIMARY KEY,name varchar(30) NOT NULL,DOB date,Job_ID int NOT NULL,Manager_ID int,Hire_Date date NOT NULL,Salary int NOT NULL,department_id int NOT NULL,FOREIGN KEY (Job_ID) REFERENCES job(Job_ID),FOREIGN KEY (department_id) REFERENCES department(Department_id))")
    mycursor.execute("INSERT INTO department VALUES(1,'Admin',11),(2,'Accounts',12),(3,'HR',11),(4,'Sales',12),(5,'Software',13),(6,'Production',14),(7,'PR',15),(8,'Engineering',13)")
    mycursor.execute("INSERT INTO job VALUES(101,'HOD'),(102,'job in Admin'),(103,'job in Accounts'),(104,'job in Software'),(105,'job in Engineering'),(106,'job in Production'),(107,'job in PR'),(108,'job in Sales'),(109,'job in HR')")
    mycursor.execute("INSERT INTO employee VALUES(1001,'Chaitanya','2003-07-21',105,1000,'2017-04-12',250000,2),(1002,'Aryan','1997-05-11',108,1000,'2015-05-14',110000,4),(1003,'Ankit','1993-03-15',107,1000,'2017-01-10',55000,7),(1004,'Saksham','1999-02-05',102,1000,'2016-02-19',75000,1),(1005,'Abhishek','1995-06-25',104,1000,'2015-03-09',63000,5),(1006,'Tom','1996-02-19',105,1000,'2016-09-05',69000,8),(1007,'Jerry','1994-09-05',106,1000,'2015-03-23',65000,6),(1008,'Dimple','2000-07-22',109,1000,'2018-07-17',71000,3)")
    con.commit()
else:
    print("Not connected")