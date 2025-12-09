# try:
#     age=int(input("Enter Your age:"))
#     if age<18:
#         raise ValueError("Age must be >18")
#     print("YOu are eligible")
# except ValueError as error:
#     print(error)


# class Error(Exception):
#     pass
# raise Error('I am raising this error out of no reason')


# Creating custom Exceptions:
# We create custonm exceptions so that we can debug large projects efficiently
# we can craete   class exception by creating  class which inherits the exception class.

# WAP such that if my list is emptty then a custon exception must be raised.
# class listerror(Exception):
#     pass
# try:
#     # list1=['abc','def','ghi','jkl']
#     list1=[]
#     if len(list1)<=0:
#         raise listerror('List cannot be empty')
#     print(list1)
# except listerror as e:
#     print(e)


# class Balance_Error(Exception):
#     pass
# try:
#     Balance=int(input("Enter your Balance:"))
#     if Balance<500:
#         raise Balance_Error('Your balance must be >500')
#     print(Balance)
# except Balance_Error as error:
#     print(error)


# class Balance_Error(Exception):

#     pass
# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#         if self.balance<500:
#          raise Balance_Error('Your balance must be >500')
#         print(self.balance)
#     def check(self):
#          return self.balance
# try:
#     b1=Bank(400)
#     print(b1.check) 
# except Balance_Error as error:
    # print(error)





# try:
#     name="hello frnds     "
#     # if len(name)<10:
#     assert len(name)>10,'name must have atleasr 10 characters'
#     print(name)
# except AssertionError as error:
#      print(error)

# try:
#     name="hello frnds     "
#     # if '@' not in name:
#     assert '@' not in name,'name must have @ characters'
#     # print(name)
# except AssertionError as error:
#  print(error)


# WAP to check the validity of usename and password,if username is wrong raise an customized usename error and if password is wrong then raise custonized exception Passworderror





# class usernameerror(Exception):
#     pass
# class passworderror(Exception):
#     pass
# try:
#     username=input("Enter Your name:")
#     if username!="Hello":
#         raise usernameerror('message')
#     try:
#         password=input("Enter Your password:")
#         if password!=12345:
#             raise passworderror('message')



