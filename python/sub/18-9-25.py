# Hierachical - in this type of one parent and more childs
# class A:
#   def all(self):
#     print("All vehicles use fuels")
# class B(A):
#   def  all(self):
#     print("this car uses petrol")
# class C(A):
#   def all(self):
#     a.all()
#     b.all()
#     print("nonee")
# a=A()
# b=B()
# c=C()
# c.all()

# class Family:
#     def mother(self):
#         print("she has 2 childrens")
# class younger(Family):
#     def daughter(self):
#         print("Daughter is studying 9th standard.")
# class elder(Family):
#     def Son(self):
#         print("son is working in MNC company.")
# y=younger()
# y.mother()
# y.daughter()
# E=elder()
# E.Son()

# HTBRID INHERITANCE --  it is the implementatiion of more than one type of inheritance in one program

# METHOD RESOLUTION ORDER--it defines

# class School:
#     def Childhood(self):
#         print("In childhood we enjoyed a lot and those days are so memorable.")

# class College(School):
#     def Teenage(self):
#         print("In theese days most of students attraction.....")
# class coaching(School):
#     def technicals(self):
#         print("after colleges students go to hyd to learn technical skills..")


# class tenkcoders:
#     def jobs(self):
#         print("They are providing opportunities.")
# class final(School,tenkcoders):
#     def success(self):
#         print("we get a job in future")

# f=final()
# f.Childhood()

# c=College()
# c.Teenage()
# C=coaching()
# C.technicals()

# f.jobs()
# f.success()


# class frnds:
#     def frnd1(self):
#         print("who will be paid?")
# class Frnd2:
#     def frnd1(self):
#         print("money evaru first theeste vaade.")
# class Frnd3(Frnd2,frnds):
#     def frnd3(self):
#         print("yeah")
# f=Frnd3()
# f.frnd1()
# f.frnd3()
# # print(Frnd3.__mro__)



## SUPER ()--KEYWORD   --it is used to implement meyhods and constructors pf parent class in child class

# class parent:
#     def __init__(self,School):
#      self.School=School
#     def school(self):
#         print(f"Amma nenu {self.School} school ki ponu")
# class child(parent):
#     def college(self):
#        super().school()
#     print(f"amma nenu college ki potha daily (because of fun)")
# c=child("E")
# c.college()


# class animal:
#     def __init__(self,species):
#         self.species=species

#     def sound(self):
#         print("all animals make sound")
# class Dog(animal):
#     def __init__(self,species,breed):
#         super().__init__(species)
#         self.breed=breed
#         print(species,breed)

#     def sound(self):
#        super().sound()
#        print("barks") 
# dog1=Dog("Mammal","labrador")
# dog1.sound()

