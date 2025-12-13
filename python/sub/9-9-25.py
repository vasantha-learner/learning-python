# class animals:
#     def __init__(self,name,speak):
#       self.name=name
#       self.speak=speak
#       def xyz(self):
#          print(f'{self.name} and {self.speak}')
# animal1=animals("Bow")
# animal2=animals("Meow")


# class animal:
#     def speak(self):
#         print("Animal Speaks")
# obj=animal()
# obj.speak()
# class Dog:
#     def speak(self):
#         print("Barks")
# ob=Dog()
# ob.speak()


# class vehicle:
#     def enginestart(self):
#         print("Vehicle started")
# class car(vehicle):
#     def enginestart(self):
#         print("vehicle stop")
# v=vehicle()
# v.enginestart()
# obj=car()
# obj.enginestart()

# class flowers:
#     def specilaity(self,name):
#         self.name=name
#         print(f'{self.name} indicates peaceful')
# class indicate(flowers):
#     def speciality(self,name):
#         self.name=name
#         print(f'{self.name} indicates happiness')
# v=flowers()
# v.specilaity("White Roses")
# obj=indicate()
# obj.specilaity("Green")


# method overloading

# class maths:
#     def add(Self,a=0,b=0,c=0):
#         return a+b+c
# m=maths()
# print(m.add(2,4))
# print(m.add(2,12,56))
# print(m.add(-2,-12,56))


# class maths:
#     def add(Self,*args):
#         total=sum(args)
#         return total
# m=maths()
# print(m.add(2,4)) 
# print(m.add(2,12,56))
# print(m.add(-2,-12,56))
# print(m.add('-2','-12','56'))

# operator overloading:

# class Book:
#      def __init__(self,pages):
#           self.pages=pages
#      def __add__(self,second):
#            return  self.pages+second.pages
          
  
# b1=Book(300)
# b2=Book(200)
# print(b1+b2)

Duck typing