import mysql.connector as c
con=c.connect(host="localhost",user="root",password="",database="question_1")
if con.is_connected() :
    mycursor=con.cursor()
    mycursor.execute("CREATE TABLE sailors(sid varchar(2) PRIMARY KEY,sname varchar(20) NOT NULL,rating int NOT NULL,date_of_birth DATE NOT NULL)")
    mycursor.execute("CREATE TABLE boats(bid varchar(3) PRIMARY KEY,bname varchar(10) NOT NULL,colour varchar(6) NOT NULL)")
    mycursor.execute("CREATE TABLE reserves(sid varchar(2),bid varchar(3),day date,time_slot int,PRIMARY KEY(sid,bid,day,time_slot),FOREIGN KEY (sid) REFERENCES sailors(sid),FOREIGN KEY (bid) REFERENCES boats(bid))")
    mycursor.execute("INSERT INTO sailors VALUES('1','Chaitanya',7,'2003-07-21'),('2','John',8,'1997-05-11'),('3','Aryan',9,'1993-03-20'),('4','Ankit',9,'1995-06-25'),('5','Saksham',6,'1999-02-28'),('6','David',7,'1996-03-19'),('7','Michael',8,'2002-07-22'),('8','Scott',9,'1994-09-05')")
    mycursor.execute("INSERT INTO boats VALUES('11','Liberty','blue'),('12','Gale','red'),('13','Zephyr','green'),('14','Saphire','red'),('15','Titanic','black'),('16','Wanderlust','blue'),('17','Noah','green'),('18','Neptune','orange')")
    mycursor.execute("INSERT INTO reserves VALUES('1','11','2017-11-01',2),('1','12','2018-02-19',3),('1','13','2017-09-23',1),('1','14','2017-11-01',1),('1','15','2017-11-01',3),('1','16','2017-11-01',2),('1','17','2018-02-19',1),('1','18','2017-07-15',1),('2','11','2017-11-07',2),('3','12','2016-03-11',1),('3','15','2019-11-07',2),('4','18','2019-11-07',1),('5','14','2017-11-07',1),('6','13','2016-03-11',2),('7','17','2017-03-11',3),('8','12','2017-11-01',4)")
    con.commit()
else:
    print("Not connected")