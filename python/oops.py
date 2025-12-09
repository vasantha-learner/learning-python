# class shape:
#     def area():
#         print("sorry! we couldn't find area")
# class circle(shape):
#     def area(self,Area,r):
#         self.Area=Area
#         self.r=r
#         Area=2*3.14*(self.r*self.r)
#         print("Area of a cicle is",Area)
# class rect(shape):
#     def area(self,RectArea,b,a):
#         self.RectArea=RectArea
#         self.b=b
#         self.a=a
#         RectArea=2*(a+b)
#         print("Area of a cicle is",RectArea)
# class Triangle(shape):
#     def area(self,TriangleArea,b,a):
#         self.TriangleArea=TriangleArea
#         self.b=b
#         self.a=a
#         RectAreaArea=2*(a+b)
#         print("Area of a cicle is",TriangleArea)
        
# c1=circle(3)
# c1=rect(2,3)
# c1=Triangle(3,4,5)
# c1=shape()

# class shape:
#     def area(self):
#         print("Sorry!")
# class circle(shape):
#     def __init__(self,radius):
#       self.radius=radius
#     def area(self):
#         circleArea=3.14*(self.radius*self.radius)
#         print("circleArea is",circleArea)
# class rect(shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         rectarea=self.l+self.b
#         print("the rectangular area is:",rectarea)
# class trian(shape):
#     def __init__(self,b,h):
#         self.b=b
#         self.h=h
#     def area(self):
#         trianglearea=(0.5)*(self.b)*(self.h)
#         print("traingle area is:",trianglearea)
# c1=circle(5)
# c1.area()
# c2=trian(4,5)
# c2.area()
# c3=rect(5,6)
# c3.area()

# class student:
#     def __init__(self,name,marks,):
#         self.name=name
#         self.marks=marks
#         self.total=sum(self.marks)
#         self.average=self.total/len(self.marks)
#         self.grade=self.c_grade()

#     def c_grade(self):
#          if self.average>=90:
#             return'A'
#          elif self.average>=70:
#              return'B'
#          elif self.average>=40:
#              return'C'
#          else:
#             return 'Fail'
#     def details(self):
#            print(f'{self.name} has scored {self.total} ,his average is {self.average} and his grade is{self.grade}')
# s1=student('Venkat',[76,65,34,89])
# s1.details()

# write  a program to book a room in a hote; using oopes
# to show the available rooms
# check in'check out
# price calculation for stay
