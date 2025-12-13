1.A class is a blueprint for creating objects in Python
class sname:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello, my name is", self.name)
n1 = sname("Alice")
n1.greet()


2.break  Exits the loop completely.
  continue  Skips the current iteration and continues the iteration
  pass  Does nothing .add data if whenever requires 


3.
x = 10
if x > 50:
    print("Greater than 20")
elif x>10 and x<50:
    print("Hai")
else:
    print("bye")


4.It is the constructor method that initializes object attributes when an object is created.

5.def square(num):
    return num * num

print(square(5))  


6.class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
car1 = Car("xyz", "abc")
car2 = Car("Honda", "Civic")

car1.display()
car2.display()


7.
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
even_odd(7)


8.for i in range(1, 11):
    print(f"5 x {i} = {5*i}")


9.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


10.num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10
print("Sum of digits:", sum_digits)


11.for i in range(1, 6):     
    for j in range(i):     
        print("*", end=" ")
    print()                


12.for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


13.
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
elif num % 3 == 0:
    print("Divisible by only 3")
elif num % 5 == 0:
    print("Divisible by only 5")
else:
    print("Not divisible by 3 or 5")


14.for i in range(1, 21):
    if i % 3 == 0:   
        continue
    print(i, end=" ")


15.for i in range(1, 11):
    if i == 7:
        break
    print(i, end=" ")


16.for i in range(1, 11, 2):  
    for j in range(1, i+1):
        if j % 2 == 0:   
            continue
        print(j, end=" ")
    print()



17.class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 50:
            return "B"
        else:
            return "C"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
        print("-" * 20)
s1 = Student("Ravi", 101, 85)
s2 = Student("Anu", 102, 65)
s3 = Student("Kiran", 103, 40)
s1.display()
s2.display()
s3.display()


18.def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def print_primes_upto(n):
    for i in range(2, n+1):
        if is_prime(i):
            print(i, end=" ")
n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is a Prime Number")
    print(f"Prime numbers up to {n}:")
    print_primes_upto(n)
else:
    print(f"{n} is NOT a Prime Number")

