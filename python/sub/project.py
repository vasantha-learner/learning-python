class Student:
    
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        self._marks={}
    def add_mark(self,subject,mark):
       if 0<= mark<=100:
           self._marks[subject]=mark
       else:
           print("invaild marks.",subject)
    def calculate_total(self):
        return sum(self._marks.values())
    def calculate_average(self):
        if len(self._marks)==0:
            return 0
        return self.calculate_total()/len(self._marks)
        
class HighSchoolStudent(Student):
    print("__Report Card(High school)__")
    def get_report(self):
        total=self.calculate_total()
        avg=self.calculate_average()
        print(f"Student name: {self.name}")
        print(f"roll_number: {self.roll_number}")
        for sub,mark in self._marks.items():
            print(f"{sub} : {mark}")
        print(f"total:",total)
        print(f"average:",avg)
        if avg>=90 and avg <=100:
            print("Grade: A")
        elif avg >=75 and avg <=90:
            print("Grade: B")
        elif avg >=50 and avg <=74:
            print("Grade: C")
        else:
            print("Failed")

class CollegeStudent(Student):
  
    def get_report(self):
        total=self.calculate_total()
        avg=self.calculate_average()
        print(f"Student name: {self.name}")
        print(f"roll_number: {self.roll_number}")
        print(f"total: ",total)
        print(f"average: ",avg)
        if  avg >=85 and avg <=100:
            print(" Grade : Distinction")
        elif avg >=70 and avg <=84:
            print("Grade : First Class")
        elif  avg >=50 and avg <=50 :
            print("Grade : Pass")
        else:
            print("Grade : Failed")

s1=HighSchoolStudent("Alice",101)
s1.add_mark("Math:",95)
s1.add_mark("Science:",88)
s1.add_mark("English:",76)
s1.get_report()
print("__Report Card(College)__")

s2=CollegeStudent("Bob",202)
s2.add_mark("Math:",82)
s2.add_mark("Data Science:",91)
s2.add_mark("AI:",87)
s2.get_report()