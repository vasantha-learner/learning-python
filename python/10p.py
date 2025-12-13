# Interview-Style Programming Questions: Basic Math and Logic

# 1. Area of Square
# Question: Calculate the area of a square. - Formula: Area = side × side - Input: - Side = 5 - Output: - Area of square is: 25

# side=int(input("Enter width of side:"))
# print("Area of Square is =",side*side)



# 2. Area of Rectangle
# Question: Calculate the area of a rectangle. - Formula: Area = length × breadth - Input: - Length = 6 - Breadth = 4 - Output: - Area of rectangle is: 24

# length=int(input("Enter Length of a Triangle:"))
# breadth=int(input("Enter breadth of a Triangle:"))
# print("Area of triangle is:",(length*breadth))


# 3. Area of Triangle
# Question: Calculate the area of a triangle using base and height. - Formula: Area = (1/2) × base × height - Input: - Base = 8 - Height = 5 - Output: - Area of triangle is: 20.0

# base=float(input("Enter base value of a Triangle:"))
# height=float(input("enter height value of a Triangle:"))
# print("Area of Triangle is=",(1/2)*(base*height))


# 4. Perimeter of Square
# Question: Calculate the perimeter of a square. - Formula: Perimeter = 4 × side - Input: - Side = 6 - Output: - Perimeter of square is: 24

# side=int(input("Enter side value of a Square:"))
# print("The permiter of a Square is=",4*side)


# 5. Perimeter of Rectangle
# Question: Calculate the perimeter of a rectangle. - Formula: Perimeter = 2 × (length + breadth) - Input: - Length = 5 - Breadth = 3 - Output: - Perimeter of rectangle is: 16


# length=int(input("Enter Length of a Rectangle:"))
# breadth=int(input("Enter breadth of a Rectangle:"))
# print("Area of triangle is:",2*(length*breadth))



# 6. Perimeter of Triangle
# Question: Calculate the perimeter of a triangle. - Formula: Perimeter = side1 + side2 + side3 - Input: - Side1 = 5, Side2 = 6, Side3 = 7 - Output: - Perimeter of triangle is: 18


# side1=int(input("Enter first side of a Triangle:"))
# side2=int(input("Enter second side of a Triangle:"))
# side3=int(input("Enter Third side of a Triangle:"))
# print("Perimeter of a Triangle:",side1+side2+side3)



# 7. Break Amount into 1000s, 500s, and Remaining Change
# Question: Break the total amount into denominations. - Input: - Amount = 3700 - Output: - 1000s: 3 - 500s: 1 - Remaining: 200

# Amount=int(input("Enter your Amount:"))
# Thousands=Amount//1000
# print("1000-",Thousands)
# Amount=Amount%1000
# five_hundreds=Amount//500
# print("500-",five_hundreds)
# Amount=Amount%500
# remaing=Amount
# print("remaaining-",remaing)


# 8. Convert Seconds into Hours, Minutes, and Seconds
# Question: Convert total seconds into hours, minutes, and seconds. - Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12


# seconds=float(input("Enter Seconds:"))
# hour=seconds//3600
# minutes=(seconds%3600)//60
# Seconds=(seconds%3600)%60
# print("Total Seconds=",seconds)
# print("Hours=",hour)
# print('Minutes=',minutes)
# print("Seconds=",Seconds)


# 9. Sum of Marks (Maths, Physics, Chemistry)
# Question: Calculate the sum of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Total marks: 263


# Maths=int(input("Enter Maths subject Marks:"))
# Physics=int(input("Enter Physics Subject Marks:"))
# Chemistry=int(input("Enter Chemistry Subject Marks:"))
# print("Sum_of_marks=",Maths+Physics+Chemistry)



# 10. Average of Marks (Maths, Physics, Chemistry)
# Question: Calculate the average of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67


# Maths=int(input("Enter Maths subject Marks:"))
# Physics=int(input("Enter Physics Subject Marks:"))
# Chemistry=int(input("Enter Chemistry Subject Marks:"))
# print("Sum_of_marks=",(Maths+Physics+Chemistry)/3)



# Interview-Style Questions Based on Conditional Statements

# 1. Check Even or Odd
# Question: Determine whether a number is even or odd. Explanation: A number is even if it is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even number


# num=int(input("Enter a num:"))
# if num%2==0:print("Even")
# else:print("Odd")


# 2. Divisible by 5 but Not by 10
# Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) to check if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: Satisfy


# num=int(input("enter a num:"))
# if num%5==0 and num%10!=0:print("Satisfy")
# else:print("not")


# 3. Biggest Among Two Numbers
# Question: Find the biggest number among two. Explanation: Use comparison operators (>) to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7


# num1=int(input("Enter a num:"))
# num2=int(input("Enter a num:"))
# if num1>num2:print(num1)
# else:print(num2)


# 4. Smallest Among Two Numbers
# Question: Find the smallest number among two. Explanation: Use comparison operators (<) to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4


# num1=int(input("Enter a num:"))
# num2=int(input("Enter a num:"))
# if num1<num2:print(num1)
# else:print(num2)


# 5. Divisible by 2, 3, and 6
# Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy


# num=int(input("enter a number:"))
# if num%2==0 and num%3==0:print("Stisfy")
# else:print("not")


# 6. Voting Eligibility
# Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote


# age=int(input("Enter your age:"))
# if age>=18:print("Eligible")
# else:print("Not eligibbbbbbble")


# 7. Student Pass/Fail Based on All Subjects >= 35
# Question: Check if a student passed all subjects (maths, physics, chemistry). Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail



# m=int(input("Enter mths mrks:"))
# p=int(input("Enter mths mrks:"))
# c=int(input("Enter mths mrks:"))
# if m>=35 and p>=35 and c>=35:print("pass")
# else:print("Fail")


# 8. Student Pass if Passed Any One Subject (>= 35)
# Question: Check if the student passed at least one subject. Explanation: Use logical OR to check if any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass



# m=int(input("Enter mths mrks:"))
# p=int(input("Enter mths mrks:"))
# c=int(input("Enter mths mrks:"))
# if m>=35 or p>=35 or c>=35:print("pass")
# else:print("Fail")


# 9. Student Pass if Passed Any Two Subjects
# Question: Check if the student passed any two out of three subjects. Explanation: Use a counter or logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass


# m=int(input("Enter mths mrks:"))
# p=int(input("Enter mths mrks:"))
# c=int(input("Enter mths mrks:"))
# if m>=35 or p>=35:print("Pass")
# elif m>=35 or c>=35:print("Pass")
# elif p>=35 or c>=35:print("Pass")
# if c>=35 or m>=35:print("Pass")

# 10. Biggest Among Three Numbers
# Question: Find the biggest number among three. Explanation: Compare each pair of numbers using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9


# a=int(input("Enter value1:"))
# b=int(input("Enter value2:"))
# c=int(input("Enter value3:"))
# if a<b and a>c:
#     print(a)
# elif b>c and b>a:
#     print(b)
# else:
#     print(c)


# 11. Smallest Among Three Numbers
# Question: Find the smallest number among three. Explanation: Use comparison logic to determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4



# a=int(input("Enter value1:"))
# b=int(input("Enter value2:"))
# c=int(input("Enter value3:"))
# if a<b and a<c:
#     print(a)
# elif b<c and b<a:
#     print(b)
# else:
#     print(c)


# 12. Perfect Square or Not
# Question: Check if a number is a perfect square. Explanation: A number is a perfect square if the square of its square root equals the number. - Input: Number = 49 - Output: Perfect square


# num=int(input("Enter a number:"))
# sq=num**(0.5)
# if sq*sq==num:
#     print("Perfect square")
# else:
#     print("not")


# 13. Cars Required for Members (Max 5 per car)
# Question: Calculate how many cars are needed for a given number of people. Explanation: Divide total people by 5 and round up using ceiling logic. - Input: Members = 17 - Output: Cars needed = 4
# num=int(input("Enter a number how many people going:"))
# if num%5==0:
#     cars=num//5
#     print(cars)
# else:
#     cars=num//5
#     num1=(num//5)%5
#     if num1<5:
#      cars+=1
#      print(cars)

# 14. Second Biggest Among Three Numbers
# Question: Find the second largest number among three inputs. Explanation: Use sorting or nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - Output: Second biggest: 18

# a=int(input("Enter value1:"))
# b=int(input("Enter value2:"))
# c=int(input("Enter value3:"))
# if a>b and b<c:
#     print(a)
# elif b>c and b<a:
#     print(b)
# else:
#     print(c)


# # 15. Leap Year or Not
# Question: Check if a given year is a leap year. Explanation: A year is a leap year if it is divisible by 4, and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - Output: Leap year
# year=int(input("Enter a Year:"))
# if year%4==0 and year%100!=0:
#     print("Leap year")
# else:
#     print("no")


# Interview-Style Programming Questions: Loops, Strings, and Number Operations

# 1. Print Numbers from 1 to n
# Question: Write a program to print numbers from 1 to n. Explanation: Use a loop starting from 1 to n and print each number. - Input: n = 5 - Output: 1 2 3 4 5


# n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(i)


# 2. Print Numbers from m to n
# Question: Write a program to print numbers from m to n. Explanation: Loop from m to n and print values. - Input: m = 3, n = 7 - Output: 3 4 5 6 7



# m=int(input("Enter a start number"))
# n=int(input("enter a number last:"))
# for i in range(m,n+1):
#     print(i)


# 3. Print Numbers from n to 1 in Reverse
# Question: Write a program to print numbers in reverse from n to 1. Explanation: Use a loop starting from n and decrement to 1. - Input: n = 5 - Output: 5 4 3 2 1


# n=int(input("Enter a number:"))
# for i in range(n,0,-1):
#     print(i)

# 4. Print Numbers from n to m in Reverse
# Question: Write a program to print numbers from n to m in reverse. Explanation: Start from n and go down to m. - Input: n = 10, m = 6 - Output: 10 9 8 7 6

# n=int(input("Enter a number:"))
# m=int(input("Enter a number:"))
# for i in range(m,n,-1):
#     print(i)


# 5. Sum of n Natural Numbers
# Question: Write a program to calculate the sum of first n natural numbers. Explanation: Use formula or loop to sum from 1 to n. - Input: n = 5 - Output: 15


# numbers=[1,2,3,4,5,6,7,8]
# count=0
# for i in numbers:
#     count+=i
# print(count)


# 6. Factorial of a Number
# Question: Write a program to find the factorial of a number. Explanation: Multiply all numbers from 1 to n. - Input: n = 5 - Output: 120



# 7. Sum of m to n Numbers
# Question: Write a program to find the sum of all numbers from m to n. Explanation: Loop from m to n and add values. - Input: m = 3, n = 6 - Output: 18

# 8. Product of m to n Numbers
# Question: Write a program to find the product of numbers from m to n. Explanation: Loop from m to n and multiply values. - Input: m = 2, n = 4 - Output: 24

# 9. Print Factors of a Number
# Question: Write a program to print all factors of a given number. Explanation: Check divisibility of number from 1 to n. - Input: n = 6 - Output: 1 2 3 6

# 10. Count of Factors
# Question: Write a program to count how many factors a number has. Explanation: Increment count when divisible. - Input: n = 6 - Output: 4

# 11. Prime Number Check
# Question: Check if a number is prime. Explanation: A number is prime if it has exactly 2 factors. - Input: n = 7 - Output: Prime

# 12. Even Numbers from m to n
# Question: Print all even numbers between m and n. Explanation: Use loop and check if divisible by 2. - Input: m = 3, n = 10 - Output: 4 6 8 10

# 13. Odd Numbers from m to n
# Question: Print all odd numbers between m and n. Explanation: Check if number % 2 != 0. - Input: m = 3, n = 10 - Output: 3 5 7 9

# 14. Count of Even and Odd Numbers
# Question: Count how many even and odd numbers are in the range m to n. Explanation: Use counters for even and odd. - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3

# 15. Reverse a String
# Question: Reverse a given string. Explanation: Use slicing or loop. - Input: “hello” - Output: “olleh”

# 16. Check for Palindrome String
# Question: Check if a string is a palindrome. Explanation: Compare string with its reverse. - Input: “madam” - Output: Palindrome

# 17. Sum of Digits
# Question: Calculate the sum of digits of a number. Explanation: Use loop and % 10 to extract digits. - Input: 123 - Output: 6

# 18. Product of Digits
# Question: Calculate the product of digits. Explanation: Multiply digits extracted from number. - Input: 123 - Output: 6

# 19. Armstrong Number Check
# Question: Check if a number is an Armstrong number. Explanation: Sum of cube of digits equals the number. - Input: 153 - Output: Armstrong number

# 20. Reverse a Number
# Question: Reverse the digits of a number. Explanation: Use loop with % and // to reverse. - Input: 123 - Output: 321

# 21. Palindrome Number Check
# Question: Check if a number is a palindrome. Explanation: Compare number with its reverse. - Input: 121 - Output: Palindrome

# 22. Count Vowels in String
# Question: Count number of vowels in a string. Explanation: Loop and check for a, e, i, o, u. - Input: “apple” - Output: 2

# 23. Count Consonants in String
# Question: Count consonants in a string. Explanation: Check for alphabetic characters not vowels. - Input: “apple” - Output: 3

# 24. Count Vowels and Consonants
# Question: Count vowels and consonants in input string. Explanation: Maintain two counters. - Input: “apple” - Output: Vowels = 2, Consonants = 3


# str1="apple"
# v_count=0
# c_count=0
# vowels="aeiouAEIOU"
# for ch in str1:
#     if ch in vowels:
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)



# 25. Perfect Number Check
# Question: Check if a number is perfect. Explanation: Sum of proper divisors equals the number. - Input: 28 - Output: Perfect number



# 26. Neon Number Check
# Question: Check if a number is a neon number. Explanation: Square the number, sum digits, match original. - Input: 9 - Output: Neon number

# num=9
# sq=num**2
# sum=0
# digits=sq%10

# 27. Strong Number Check
# Question: Check if a number is a strong number. Explanation: Sum of factorial of digits equals the number. - Input: 145 - Output: Strong number

# 28. Harshad Number Check
# Question: Check if a number is divisible by the sum of its digits. Explanation: Calculate digit sum and check divisibility. - Input: 18 - Output: Harshad number

# 29. Fibonacci Series
# Question: Print the Fibonacci series up to n terms. Explanation: Start with 0, 1 and continue with sum of last two. - Input: n = 5 - Output: 0 1 1 2 3

# 30. Check for Neon Number (Repeated)
# Question: Again, check for a neon number (example). Explanation: Square number and sum digits. - Input: 9 - Output: Neon number


