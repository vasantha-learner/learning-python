1. Swap two numbers

a=20
b=50
temp=a
a=b
b=temp
print("a value:",a)
print("b value:",b)

2.Identify Data Types

values1=int(input("input a values:"))
values2=input("Enter your name:")
values3=input("Enter your village:")
print(type(values1))
print(type(values2))
print(type(values3))

3. Simple calculator
 is:",type(str2))

a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
print("a//b=",a//b)
print("a%b=",a%b)
print("a**b=",a**b)

4. Salary Hike

Salary=int(input("Enter your salary:"))
NewSalary=Salary+(15%100)
print("Old Salary=",Salary)
print("New Salary=",NewSalary)

5.Area and Perimeter of circle

r=int(input("Enter radius of a circle:"))
perimeter=2*3.14159*r
print("perimeter of a circle:",perimeter)
area=3.14149*r**2
print("Area of a circle:",area)

6.Ascii charcater
ch1=input("Enter a character:")
print(ord(ch1))

7.check Even or Odd
number=int(input("Enter a number:"))
if number%2==0:
    print("Even")
else:
    print("odd")

8.Compound Assignament Practice
a=45
print(a)
a+=1
print(a)
a-=1
print(a)
a*=3
print(a)
a//=15
print(a)
a%=1
print(a)

9. Boolean and logical check
Age=int(input("Enter your age:"))
Name=input("Enter your name:")
if(Age>=18 and Name=="vassu"):
    print(True)
else:
    print(False)
 
10. Bitwise Shift Practice
a=1<<2
print(a)
b=1>>2
print(b)

11.Bitwise AND,OR,XOR,NOT
a=12
b=5
print("a&b value:",a&b)
print("a|b value:",a|b)
print("a^b value:",a^b)
print("~b value:",~b)
print("~a value:",~a)


12.Data Type Conversion
str1="1234"
f=23.70
str2=int(str1)
f2=str(f)
int1=45454
int2=bool(int1)
print("type of str2 result is:",type(str2))
print("type of f2 result is:",type(f2))
print("type of int2 result is:",type(int2))


Temperature Conversion

convert = input("Enter which conversion you want: 1. celsius to fahrenheit or 2. fahrenheit to celsius: ")
if convert == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit:", fahrenheit)
elif convert == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Celsius:", round(celsius, 2))
else:
    print("Please enter either 1 or 2")



14.Quotient and Remainder
Number1=int(input("Enter your first number:"))
Number2=int(input("Enter your second number:"))
remainder=Number1%Number2
quotient=Number1//Number2
print("remainder is:",remainder)
print("quotient is:",quotient)


15.String Operations
Str1=input("Enter a your name:")
print(Str1.upper())
print(Str1.lower())
print(len(Str1))
print("a" in Str1)


16.Sum of Digits
num=int(input("Enter a number:"))
sum=0
while num > 0:
     digit=num%10
     sum=sum+digit
     num = num // 10
print("Total sum of digits:",sum)



17.Identity vs Equality
a=["Apple","Ball","cat","Duck"]
b=["Apple","Ball","cat","Duck"]
print(a==b)
print(a is b)



18.Age in Months and Days
Age=int(input("Enter your age:"))
age_in_months=Age*12
age_in_days=Age*365
print("Age in months:",age_in_months)
print("Age in Days:",age_in_days)



19.Type Guessing
x=10+3.5
y="Age"+str(30)
z=True+False+2
print(type(x))
print(type(y))
print(type(z))


20.Bitwise Practice
n=int(input("Enter a number:"))
print("~n value:",~n)
print("n<<1 value:",n<<1)
print("n>>2 value:",n>>2)