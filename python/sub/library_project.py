class Student:

    def __init__(self):

        self.books={
               "CSE":["AI","ML","CS","C++","Python","OOPS"],
               "ECE":["EM","EC","ED","NA","STLD","VLSI Design","Control Systems","Microprocessors & MicroControllers"],
               "EEE":["ECA","Electronic fields","Physics","Electronic Devices & Circuits","Signals & Systems"],
               "MECH":["Strength of Materials","Machine Drawing","Heat Transfer","Power Point Engineering"]
        }   


    def info(self):
       self.stu_name=input("Enter your name? :")
       self.dept_name=input("Enter your department? :")
       if self.dept_name.upper() in self.books:
         self.book_name=input(f"Hi {self.stu_name} ,can you tell me what book do you want? :")
         available_books = [b.lower() for b in self.books[self.dept_name.upper()]]
         if  self.book_name.lower() in available_books:
            print(f"yes,this {self.book_name} book is avalible")
         else:
          print("sorry this book is currently not avaliable")  
          print(f"we will try to bring this {self.dept_name} book for next time") 

s1=Student()
s1.info()




