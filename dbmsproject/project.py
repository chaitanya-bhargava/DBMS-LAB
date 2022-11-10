import mysql.connector as c
def menu():
    print("-----------MENU-----------\n1.Search for a user.\n2.Search for message.\n3.Search for a comment using username.\n4.Make a new account.\n5.Follow a new person.\n6.Remove a friend.\n7.Delete a comment\n--------------------------")
def userSearch():
    s=input("Enter first letters of username:")
    a=mycursor.execute("SELECT username FROM user WHERE username LIKE '"+s+"%'")
    myresult=mycursor.fetchall()
    if(len(myresult)==0):
        print("No user found!")
    for j in myresult:
        print(j)
def msgSearch():
    s=input("Enter first letters of message:")
    mycursor.execute("SELECT * FROM message WHERE msg_body LIKE '"+s+"%'")
    myresult=mycursor.fetchall()
    if(len(myresult)==0):
        print("No message found!")
    for j in myresult:
        print(j)
def commentSearch():
    username=input("Enter username:")
    mycursor.execute("SELECT post_id,comment_body FROM comments WHERE username='"+username+"'")
    myresult=mycursor.fetchall()
    if(len(myresult)==0):
        print("No comment found!")
    for j in myresult:
        print(j)
def newAccount():
    username=input("Enter your username:")
    fname=input("Enter your first name:")
    mname=input("Enter your middle name:")
    lname=input("Enter your last name:")
    mob=input("Enter your mobile no.:")
    email=input("Enter your email:")
    password=input("Enter your password:")
    mycursor.execute("INSERT INTO user VALUES('"+username+"','"+fname+"','"+mname+"','"+lname+"','"+mob+"','"+email+"','"+password+"')")
    con.commit()
def newFollow():
    username=input("Enter your username:")
    follow=input("Enter username of person you want to follow:")
    mycursor.execute("INSERT INTO followers VALUES('"+follow+"','"+username+"')")
    con.commit()
def removeFriend():
    username=input("Enter your username:")
    friend=input("Enter username of friend to be removed:")
    mycursor.execute("DELETE FROM friend WHERE username='"+username+"' AND friend='"+friend+"'")
    mycursor.execute("DELETE FROM friend WHERE username='"+friend+"' AND friend='"+username+"'")
    con.commit()
def deleteComment():
    id=input("Enter comment_id:")
    mycursor.execute("DELETE FROM comments WHERE comment_id="+id)
    con.commit()
con=c.connect(host="localhost",user="root",password="",database="socialmedia")
mycursor=con.cursor()
if con.is_connected() :
    menu()
    x=int(input("Choose action:"))
    if(x==1):
        userSearch()
    elif(x==2):
        msgSearch()
    elif(x==3):
        commentSearch()
    elif(x==4):
        newAccount()
    elif(x==5):
        newFollow()
    elif(x==6):
        removeFriend()
    elif(x==7):
        deleteComment()
    else:
        print("Please enter a valid value!")
else:
    print("Not connected")