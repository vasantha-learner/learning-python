# ###    INHERITANCE


# inheriting data,methods and constructors from  parent class to child class.
# types of inhetitance 


# single inheritance   - here only one chicld class inherits  the method and data of one parent class.
# Syntax :

# class parent:
    # data
    # methods
# class child(parent):
    # data
    # methods

# multiple inheritance  
# multilevel inheritance
# Hierachical inheritance
# Hybrid inheritance


# class Parent:
#     def vehicle(self):
#         print("This is a care")
# class Child(Parent):
#     def some(self):
#         print("This is a van")
# C=Child()
# C.vehicle()
# C.some()

# class laptop:
#     def vasu(self):
#         print("this is vasu's laptop.")
# class Hari(laptop):
#     def hari(self):
#         print("yes i asked to her for my work.")
# Hari1=Hari()
# Hari1.vasu()
# Hari1.hari()


### Multiple inheritance: here one child inherits features from multipple paret classes


# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):    
#         return self.a+self.b
# class operation1:
#     def mul(self):
#         return self.a*self.b
# class child(calculator,operation1):
#     def sub(self):
#         return self.a-self.b
# c=child(20,4)
# print("The addition of a,b is=",c.add())
# print("The multiplication of a,b is=",c.mul())
# print("The subtraction of a,b is=",c.sub())



# class frnd1:
#     def work(self):
#         print("she is very innocent")
# class frnd2:
#     def work(self):
#         print("she is very crazy")
# class frnd3(frnd1,frnd2):
#     def work(self):
#         f1.work()
#         f2.work()
#         print("i am very happy to spend with them")
# f1=frnd1()
# f2=frnd2()
# f3=frnd3()
# f3.work()



### Multilevel Inheritance


# class Plants:
#     def some(self):
#         print("plants are in fields")
# class Zoo(Plants):
#     def some(self):
#         print("animals are in zoo")
# class House(Zoo):
#     def some(self):
#         a.some()
#         p.some()
#         print("i'm in class but we are living on earth")
# a=Plants()
# p=Zoo()
# c=House()
# c.some()



# class school:
#     def knowledge(self):
#         print("agnyanam")
# class college(school):
#     def skills(self):
#         print("bunk")
# class Institute(college):
#     def realskills(self):
#         print("python")
# student1=Institute()
# student1.knowledge()
# student1.skills()
# student1.realskills()



# class school:
#     def learnt(self):
#         print("Playing games and asking money to parents to go to school every day.")

# class college(school):
#     def learnt(self):
#         print("To spend with frnds and chill with bench mates")

# class institute(college):
#     def learnt(self):
#         a.learnt()
#         b.learnt()
#         print("focus on career")

# a=school()
# b=college()

# vasu=institute()
# vasu.learnt()


