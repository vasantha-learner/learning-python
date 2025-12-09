# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def engine(self):
#         print(f'{self.brand} the car has started')    
      
#     def enginestop(self):
#         print('The car has stopped')

# car1=car("audi","a6")
# car2=car('Lamborgini','Avendator')
# car2.engine()
# print(f'The car brand is {car1.brand} and model is {car1.model}')

# print(f'The car brand is {car2.brand} and model is {car2.model}')


# class Class:
#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
#     def guest_lec(self):
#         print(f'{self.name} sir started new classes.')
# Class1=Class('venkat','python')
# Class2=Class('Harish','Database')
# Class2.guest_lec()
# print(f'{Class1.name} sir deals with {Class1.subject} classes.')
# print(f'{Class2.name} sir deals with {Class2.subject} classes.')




# class student:
#     def __init__(self,name,qualification):
#         self.name=name
#         self.qualification=qualification

#     def completed(self):
#         print(f'{self.name} is completed his {self.qualification}.')

#     def notcompleted(self):
#         print(f'{self.name} is not completed his {self.qualification}.')

#     def job(self):
#         print(f'{self.name} is completed {self.qualification} he got TCS job')   

# student1=student('Hari','Degree')
# student2=student('Sathish','Degree')
# student3=student('Lucky','B.tech')
# student1.completed()
# student2.notcompleted()
# student3.job()




# class animal:
#     def __init__(self,name,food):
#         self.name=name
#         self.food=food
#     def state(self):
#         print(f'{self.name} is taking food like {self.food} etc.')
#     def stat(self):
#         print(f'{self.name} and {self.food} pet animals.')   
# animal1=animal("DOG","Chicken")
# animal2=animal("Cat","Milk")
# animal1.state()
# animal2.stat()





class state():
    reading='jntu university'    #class variable
    def __init__(self,name,from_state):
        self.name=name
        self.from_state=from_state             #object variable
    def AP(self):
        print(f'{self.name} is coming from {self.from_state} ,joining in {self.reading}.')
    
state1=state("Aruna","Telangana")
state2=state("Kamala","Andhra")
# state1.AP()
state2.AP()
