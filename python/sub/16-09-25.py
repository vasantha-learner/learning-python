#Hiding unnecessary details and only showing esential fetaues to the user.
# from abc import ABC
# from abc import ABC,abstractmethod
# class Shape(ABC):
#       @abstractmethod
#       def area(self):
#        pass            
#       def info(self):
#           print("this one is considered as a shape.")
# class Rectangle(Shape):
#      def __init__(self,a,b):
#          self.a=a
#          self.b=b
#      def area(self):
#          print(f"The area of rectangle is")
#          return self.a*self.b
# R=Rectangle(2,9)
# R.info()
# print(R.area()) 


# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod

#     def Traingle_area(self):
#         pass
#     @abstractmethod
    
#     def Square_area(self):
#         pass
#     @abstractmethod

#     def Circle_area(self):
#         pass
#     @abstractmethod

#     def info(self):
#         print("Areas for Particular shapes")

# class Triangle(Shape):

#     def __init__(self,height,breadth):
#         self.height=height
#         self.breadth=breadth

#     def Traingle_area(self):
#        return (self.height*self.breadth)*0.5
    
#     def Square_area(self,side):
#         self.side=side
#         return side*side
    
#     def Circle_area(self,r):
#         self.r=r
#         return 3.14*self.r*self.r
    
# t=Triangle()                                            #################################################DOUBT###############################
# t.info()
# print("the area of triangle is",t.Traingle_area(8,9))
# print("the area of square is",t.Square_area(3))
# print("the area of circle is",t.Circle_area(4))      



# if it walks like a duck,quaks like a duck the it is a duck


# class Dog:
#     def walk(self):
#         print("it can walk")
#     def speak(self):
#         print("it barks")
# class Horse:
#     def walk(self):
#         print("Horse can Walk")
#     def speak(self):
#         print("it Whines")
# class venu:
#     def walk(self):
#         print("chance............")
#     def speak(self):
#         print("class ...............")

# d=Dog()
# h=Horse()
# v=venu()

# def checking(being):
#     being.walk()
#     being.speak()
#     print("yes")
# checking(d)
# checking(h)
# checking(v)


# class Parrot:
#     def talk(self):
#         print("it can talk")
#     def fly(self):
#         print("it can fly")
# class Koyila:
#     def talk(self):
#         print("it sings")
#     def fly(self):
#         print("it can fly")
# class Human:
#     def talk(self):
#         print("can")
#     def fly(self):
#         print("can")
# P=Parrot()
# K=Koyila()
# S=Human()

# def check(bird):
#     bird.talk()
#     bird.fly()
#     print("yes these are animals.")
#     print("But snake is.............")
# check(P)
# check(K)
# check(S)

# it is caregorizing object based on its featues irrsepective of its ttype
