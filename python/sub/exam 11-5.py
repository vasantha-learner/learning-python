class car:
    def __init__(self,Brand,Model):
        self.Brand=Brand
        self.Model=Model
    def car_info(self):
        print(f'the car brand name is {self.Brand}  and model is: {self.Model} ')
car1=car("Royal","Toyoto")
car2=car("xyz","Abc")
car3=car("thar","europe")
car1.car_info()
car2.car_info()
car3.car_info()


class BankAccount:
    def __init__(self,balance):
          self.__balance=balance
    def deposit(self,amount):
          self.amount=amount
          self.__balance+=amount
          print(f'your total amount is {self.__balance}')
    def withdraw(self,amount):
         self.__balance-=amount
         print(f'your remaining amount is {self.__balance}')

get_balance=BankAccount(900)
get_balance.deposit(600)
get_balance.withdraw(300)



class Student:
    def __init__(self,marks):
        self.__marks=marks
    def getter(self,marks):
        self.__marks=marks
    def setter(self,marks):
        if marks<=100 and marks>=0:
            print("restricred")
        else:
            print("Invalid marks")
s1=Student("")
s2=Student("")
s3=Student("")
s1.setter(-20)
s3.setter(-300)


class animals:
    def Name(self,name,sound):
        self.name=name
        self.sound=sound
        print(f'{self.name} sounds like {self.sound}')
class sounds(animals):
    def Name(self,name,sound):
        self.name=name
        self.sound=sound
        print(f'{self.name} sounds like {self.sound}')
v=animals()
v.Name("Dog","Bow")
obj=sounds()
obj.Name("cat","Meow")



class person:
        def introduce(self):
          print("I'm a person")
class Employee(person):
    def introduce(self):
         super.introduce()
         print(" ")
    
s=Employee()    
s.introduce()
