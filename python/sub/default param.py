
1. Cube of a number

def cube(n):
    return n ** 3
print(cube(3)) 


2. Average of two numbers

def average(a, b):
    return (a + b) / 2
print(average(10, 20))  


3. Return square and square root

import math
def square_and_root(n):
    return n ** 2, math.sqrt(n)
print(square_and_root(9))  


4. Check if number is odd

def is_odd(n):
    return n % 2 != 0
print(is_odd(5))  
print(is_odd(10)) 


5. Sum of digits of a number

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
print(sum_digits(1234))  



6. Greeting function

def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())         
print(greet("Navya"))  

7. Power function

def power(base, exponent=2):
    return base ** exponent

print(power(5))       
print(power(2, 3))    


8. Total bill calculator

def total_bill(item="Sandwich", quantity=1, price=50):
    return f"Total for {quantity} {item}(s): {quantity * price} Rs"
print(total_bill())                       
print(total_bill("Pizza", 2, 150))


9. Employee information

def employee_info(name, age=30, department="HR"):
    return f"Employee: {name}, Age: {age}, Department: {department}"
print(employee_info("Navya"))  


10. Circle area calculator

def circle_area(radius=1):
    return 3.14 * radius * radius

print(circle_area())      
print(circle_area(7))    



11. Sum of all even numbers up to a given number

def sum_even(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

print(sum_even(10))  



12. Largest number from a list

def largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print(largest_number([5, 12, 7, 30, 18]))  



13. Min and Max from a list

def min_max(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return minimum, maximum
print(min_max([5, 12, 7, 30, 18]))  # Output: (5, 30)




14. Student summary (name, total marks, average marks)

def student_summary(name, marks):
    total = sum(marks)
    average = total / len(marks)
    return name, total, average

print(student_summary("Navya", [80, 90, 70, 60, 85]))




def calculate(num1, num2, operator="+"):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Invalid operator"

print(calculate(10, 5))        
print(calculate(10, 5, "-"))   
print(calculate(10, 5, "*"))   
print(calculate(10, 5, "/"))   
print(calculate(10, 0, "/"))   

