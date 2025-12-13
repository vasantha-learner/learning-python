# class Convert:
#     def __init__(self,kilometers):
#         self.kilometers=kilometers
#     def centimeters(self):
#         return self.kilometers*100000
#     def meters(self):
#         return self.kilometers*1000
# C1=Convert(5.54)
# print(C1.centimeters())
# print(C1.meters())


# class Emp:
#     def __init__(self,name,empid,basicpay):
#         self.name=name
#         self.empid=empid
#         self.basicpay=basicpay
#     def netpy(self):
#         # netpay=self.basicpay+self.incensitives-pf
#         self.pf=self.basicpay*(0.3)
#         self.incensitives=self.basicpay*(0.15)
#         self.netpay=self.basicpay+self.incensitives-self.pf
#         return self.netpay
# e1=Emp('Venkat',101,30000)
# print(e1.name)
# print(f'Total Netapay of {e1.name} is :{e1.netpy()}')
# print(e1.netpay())


# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def price_update(self,new_price):
#         self.new_price=new_price
#         if self.price>0:
#             self.upadated=self.price+self.new_price
#             return self.upadated
#         else:
#             return self.price
# p1=product('pens',20)
# print(p1.price_update(200))



# class Passwords:
#     def __init__(self,password=123):
#         self.password=password
#     def check(self,pasword):
#         # self.password=password
#         if self.__password==self.password:
#             print("Your Password is correct.")
#         else:
#             print("You Entered Incorrect Password")
#     def update(self,up_password):
#              self.__up_password=up_password
#              return self.up_password
# p1=Passwords()
# p1.check(123)
# p1.update(456)
# print("Your Password Updated Successfully.")
# print("Your updated password is:",p1.update(456))




