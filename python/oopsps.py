
        


# class Employee:
#     def salary(self):
#         return 30000

# class FullTime(Employee):
#     def __init__(self, name,salary):
#         self.name = name
#         self.salary = salary*(1.20)
    
#     def salary(self):
#         return self.salary

# class PartTime(Employee):
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary//2
    
#     def salary(self):
#         return self.salary

# class Intern(Employee):
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary/4
    
#     def salary(self):
#         return self.salary


# f1 = FullTime('venkat',35000)
# print('FullTime Employee of salary is :',f1.salary)  
# p1=PartTime('Pavan',35000)
# print('PartTime Employee of salary is :',p1.salary)
# i1=Intern('Hari',35000)
# print('Intern of salary is :',i1.salary)





# SIMULATE A BANK SYSTEM WITH METHODS FOR WITHDRAW,CHECK BALNACE AMD DEPOSIT AND INTERSET

class Bank:
    def __init__(self,name,AccNo,AccountType,balance):
        self.name=name
        self.AccountType=AccountType
        self.AccNo=AccNo
        self.balance=balance
        self.balance=35000
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        return self.balance
    def withdraw(self,amount):
        self.amount=amount
        self.balance-=self.amount
        return self.balance
    def checkbalance(self):
        return self.balance
    def borrow(self,interst):
        self.interst=interst
        if self.AccountType=='Current':
           self.interest=interst*(1.3)
           self.balance+=self.interest
           return self.balance
        else:
         self.interest=interst*(1.10)
         self.balance+=self.interest
         return self.balance
b1=Bank('Venkat',101,'Current',35000)
b1.deposit(12000)
print("Your Total Balance is :",b1.deposit(12000))
b1.withdraw(20000)
print("Your Remaining Balance is :",b1.withdraw(12000))
# b1=Bank('Venkat',101,'Saving',35000)
b1.borrow(120000)
print("Your Total Balance is :",b1.borrow(120000))
# b1.withdraw(20000)
# print("Your Remaining Balance is :",b1.withdraw(12000))
# b1.borrow()
