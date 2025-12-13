Print Numbers Except Multiples of 3

for i in range(1,51):
    if i%3==0:
        continue
    print(i)
    i=i+1


First Multiple of 11

while True:
    Num=input("Enter a number  (or enter 'exit')")
    Num1=int(Num)
    if Num.lower()==exit:
        break
    elif Num1%11==0:
        print(Num)
        print("The currnet number is divisible by 11")
        print("you are exit from this loop")
        break
    else:
        print("Hello")

2.Count Vowels in a string

str1=input("Enter a string:")
vowels=['a','e','i','o','u']
str2=str1.lower()
count=0
for i in range(len(str2)):
    if str2[i] in vowels:
     count+=1
print("total:",count)


3.Reverse Even Numbers

i=100
while i>=1:
    if(i%2==0):
     print(i)
    i=i-1


4.Password verification
while True:
    password=input("Enter your password:")
    if password=="admin123":
        print("Password is correct")
        break
    else:
        print("Please enter a correct password")
    

5.Multiplication of a number

Num=int(input("Enter a number:"))
for i in range(1,11):
  print(f"{Num} x {i} = {Num * i}")
    

6.Skip Negative numbers

print("Enter 10 numbers:")
for i in range(10):
     num = int(input(f"Enter number {i+1}: ")) 
     if num<0:
        continue
     else:
      print("positive numbers",num)

7.sum of odd  numbers

n = int(input("Enter a number N: "))
sum = 0

for i in range(1, 2 * n, 2):  # Generates first N odd numbers: 1, 3, 5, ..., (2n - 1)
    sum += i

print("Sum of first", n, "odd numbers is:", sum)



8.List Prime Numbers from 1 to 50

print("Prime numbers from 1 to 50:")
for num in range(1, 51):
    if num < 2:
        continue  # skip 0 and 1, which are not prime
    for i in range(2, num):
        if num % i == 0:
            break  # not prime
    else:
        print(num)


9.Running Total Until Zero

count = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    count += num
print("Total sum:", count)