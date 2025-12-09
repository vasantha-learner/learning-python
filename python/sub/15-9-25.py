# class animal:
#     def speak(self):
#         print("animals")
# class Dog(animal):
#     def speak(Self):
#         super().speak()
#         print("Barks")
# d1=Dog()
# d1.speak()


# class book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages
#     def __sub__(self,other):
#         return self.pages-other.pages
#     def __mul__(self,other):
#         return self.pages*other.pages
    
# b1=book(400)
# b2=book(200)
# print(b1+b2)
# print(b1-b2)
# print(b1*b2)


# from abc import ABC,abstractmethod  #imported Abc and abstractmethod from abc module

# class vehicle(ABC):
#     @abstractmethod
#     def mileage(self):
#         pass             #we declare a class as abstract by inheriting Abc class inti that class        we wont define 
#     #a  method in abstract class.we jusr declare it. we defone the anstract method uin the normal

# # v=vehicle()
# # v.mileage()

# class car(vehicle):
#     def mileage(self):
#         print("Tesla:300 miles per cherage")

#     def some(Self):
#         print("hlo")   
# v=car()
# v.mileage()



from abc import ABC,abstractmethod
class flowers(ABC):
    @abstractmethod
    def color(self):
      pass
class beauty(flowers):
    def color(self):
        print("do u likes roses?")
        print("yeah,ofcourse i like White roses,they are so beautiful")
f=beauty()
f.color()


