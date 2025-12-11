import pymysql
try:
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="8801"
    )
    print("Connection success.")
except Exception as e:
    print("Error",e)
cursor=conn.cursor()
try:
    cursor.execute("Create DataBase if not Exists `66r_68r` ")
    print("DataBase Created successfully!")
except Exception as e:
    print("This Database exists!")

def createTable():
    try:
        cursor.execute("use `66r_68r` ")
        cursor.execute(""" create table if not exists Students 
                       (id int primary key auto_increment,
                       name varchar(40),age int,gender varchar(20),
                       email varchar(50))
                       
                """)  
        print("Table Created successfully!") 
    except Exception as e:
        print("Something Went wrong!",e)   
def insertData():
    try:
        name=input("enter Student Name:")
        age=int(input("Enter Student Age:"))
        gender=input("enter gender:")
        email=input("enter Gmail:")
        cursor.execute("use `66r_68r` ")
        query = "INSERT INTO Students(name, age, gender, email) VALUES (%s, %s, %s, %s)"
        values = (name, age, gender, email)
        cursor.execute(query,values)
        print("Data Inserted Successfully!")
    except Exception as e:
        print("Error occured",e)


def insertmanydata():
    try:
     cursor.execute("use `66r_68r` ")
     query = "INSERT INTO Students(name, age, gender, email) VALUES (%s, %s, %s, %s)"
     values = [('Harish',25,'Male','Harish@gmail.com'),('Gowri',27,'Male','Gowri@gmail.com'),
        ('Laxmi',30,'Female','Lucky@gmail.com'),('Vassu',21,'Female','Vasu@gmail.com')
     ]
     cursor.executemany(query,values)
     print("Data inserted successfully!")
    except Exception as e:
        print("Something went worng",e)

def updateStudentNamebyid():
    try:
        cursor.execute("use `66r_68r` ")
        stud_id=int(input("Enter Student id:"))
        Name=input("Enter Student Name:")
        query="""update students set Name=%s where  id=%s"""
        values=(Name,stud_id)
        cursor.execute(query,values)
        print("Record Updated successfully!")
    except Exception as e:
        print("something went Wrong1",e)

def updatestudentagebyid():
    try:
     cursor.execute("use `66r_68r` ")
     stud_id=int(input("Enter Student id:"))
     age=int(input("Enter new age:"))
     query="""update students set age=%s where  id=%s"""
     values=(age,stud_id)
     cursor.execute(query,values)
     print("Record Updated successfully!")
    except Exception as e:
        print("something went Wrong1",e)
        

def deletedata():
    try:
        cursor.execute("use `66r_68r` ")
        stud_id=int(input("Enter Student id:"))
        query="delete from students where id=%s "
        values=(stud_id,)
        cursor.execute(query,values)
        print("Data Removed successfully!")
    except Exception as e:
        print("Error occured!",e)

def menu():
    print("choose 1 for creating New Table")
    print("choose 2 for insert data")
    print("choose 3 for insert Muliple data")
    print("choose 4 for update student name by id")
    print("choose 5 for update student age by id")
    print("choose 6 for delete data")
    ip=int(input("Enter choice number:"))
    if ip==1:
        createTable()
    elif ip==2:
        insertData()
    elif ip==3:
        insertmanydata()
    elif ip==4:# update studentage by id,delete
        updateStudentNamebyid()
    elif ip==5:
        updatestudentagebyid()
    elif ip==6:
        deletedata()
    else:
        print("Enter Correct choice")
menu()    
conn.commit()
cursor.close()
conn.close()                                              






