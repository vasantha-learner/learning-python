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
    cursor.execute("Create DataBase if not Exists `Contact_List` ")
    print("DataBase Created successfully!")
except Exception as e:
     print("This Database exists!")



def To_Show_contact():
    pass


def Create_Table():
    try:
        cursor.execute("use `Contact_List`")
        cursor.execute(""" create table if not exists My_Contacts
                       (id int primary key auto_increment,
                       name varchar(40),Mobile_NO char(10)  ) 
                """)  
        print("Table Created successfully!") 
    except Exception as e:
        print("Something Went wrong!",e) 


def contact_Update():
    try:
        cursor.execute("use `Contact_List`")
        Contact_id=int(input("enter Contact id:"))
        new_Mobile_NO=int(input("Enter New Mobile Number:"))
        query="updte My_contacts set Mobile_NO=%s where id=%s"
        values=(new_Mobile_NO,Contact_id)
        cursor.execute(query,values)
        print("Contact Updated successfully!")
    except Exception as e:
        print("Something went wrong",e)


def Contact_Search():
    try:
        cursor.execute("use `Contact_List`")
        name=input("Enter Contact Name to search:")
        query="select 8 from My_contacts where name=%s"
        values=(name,)
        cursor.execute(query,values)
        result=cursor.fetchall()
        if name in result:
            print("This contact is found")
        else:
            print("contact Not Found")
    
    except Exception as e:
        print("something went wrong",e)
        
def Contact_Delete():
    try:
        cursor.execute("use `Contact_List`")
        contact_id=int(input("Enter Contact id to delete:"))
        query="delete from My_contacts where id=%s"
        values=(contact_id,)
        cursor.execute(query,values)
        print("contact deleted Successfully!")
    except Exception as e:s
        print("Something Went worng",e)



def Create_Contact():
    try:
        name=input("Enter Contact Name:")
        Mobile_NO=int(input("Enter Your 10 digit Mobile number:"))
        cursor.execute("use `Contact_List` ")
        query="Insert into My_contacts(name,Mobile_NO) values(%s,%s)"
        values=(name,Mobile_NO)
        cursor.execute(query,values)
        print("contact created successfully!")
    except Exception as e:
         print("Something went wrong",e)



def Create_ManyContacts():
    try:
        cursor.execute("use `Contact_List`")
        query="Insert into My_contacts(name,Mobile_NO) values(%s,%s)"
        values=[('Harish','8801123456'),('Gowri','8801987654'),('vassu','9618413117')]
        cursor.executemany(query,values)
        print("Contacts Created successfully!")
    except Exception as e:
        print("Something Went Wrong !",e)

def menu():
    print("Enter 1 for To show Contact")
    print("Enter 2 for Create Table")
    print("Enter 3 for Create Contact")
    print("enter 4 for create many contacts")
    print("Enter 5 for Search Contact")
    print("Enter 6 for update the contact")
    print("Enter 7 for Delete contact")
    print("Enter 8 for Exit")
    ip=int(input("Enter your Choice Number:"))
    if ip==1:
        To_Show_contact()
    elif ip==2:
        Create_Table()
    elif ip==3:
        Create_Contact()
    elif ip==4:
        Create_ManyContacts()
    elif ip==5:
        Contact_Search()
    elif ip==6:
        contact_Update()
    elif ip==7:
        Contact_Delete()
    elif ip==8:
        exit()
    else:
        print("Please Enter Correct Choice!")
menu()    
conn.commit()
cursor.close()
conn.close()                                              

