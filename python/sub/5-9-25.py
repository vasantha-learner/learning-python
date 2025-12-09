# class Dog():
#     species='mammals' #class variable
#     def __init__(self,name,breed):
#         self.name=name         #object variables
#         self.breed=breed
#     def details(self):
#         print(f'The {self.name} of breed {self.breed} is {self.species}')

# Dog1=Dog('bunty','indie')
# Dog1.details()
# Dog2=Dog('bittu','pomerian')
# Dog2.details()


# class state():
#     reading='jntu university'    #class variable
#     def __init__(self,name,from_state):
#         self.name=name
#         self.from_state=from_state             #object variable
#     def AP(self):
#         print(f'{self.name} is coming from {self.from_state} ,joining in {self.reading}.')
    
# state1=state("Aruna","Telangana")
# state2=state("Kamala","Andhra")
# # state1.AP()
# state2.AP()


# class Account():
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
#     def deposit(self,ammount):
#          self.__balance+=ammount    
#     def withdraw(self,ammount):
#         self.__balance-=ammount

#     def checkBalance(self):
#         print(f'ur remaining balance {self.__balance}')   
# customer1=Account('koushik',5000)
# customer1.deposit(2000)
# customer1.withdraw(6900)
# customer1.checkBalance()


# class student:
#     def __init__(self,name,qualification,married):
#         self.name=name
#         self.qualification=qualification
#         self._married=married
#     def completed(self,yes):
#          self._married=yes
#     def completed(self,no):
#          self._married=no
#     def status(self):   
#          print(f'{self.name} is completed his {self.qualification} and {self._married}  he got married.')

#     # def notcompleted(self,no):
#     #     self._married=no
#     #     print(f'{self.name} is not completed his {self.qualification}  and he is {self._status} married.')

#     # def job(self):
#     #     print(f'{self.name} is completed {self.qualification} he got TCS job')   

# student1=student('Hari','Degree','yes')
# student2=student('Sathish','Degree','no')
# # student3=student('Lucky','B.tech')
# student1.status()
# # student2.notcompleted()
# # student3.job()
# print(self._married)

class car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def enfinestart(self):
        print("")
car1=car("Royal","emo")
car2=car("infield","yeah")