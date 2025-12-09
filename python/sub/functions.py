# 1.functions without Arguments:

# def numbers():
#     for i in range(1,21):
#         print(i)
# numbers()

# 2.

# def even_nums():
#     for i in range(1,21):
#         if i%2==0:
#             print(i)
# even_nums()

# functions with parameters:

# 3.

# def add(a,b):
#     print(a+b)
# add(10,20)

# 4.
# def even_nums(a):
#     if a%2==0:
#         print(a,"is Even")
#     else:
#         print(a,"is Odd")
# even_nums(34)











Easy while loops Tasks
1.
i=1
while i<=5:
    print(i)
    i=i+1
2.
i=1
while i<=11:
    if i%2==0:
        print(i,"is Even")
    i=i+1
print()
3.
i=1
total=0
while i<=10:
    total+=i
    i=i+1
print(total)
4.
number=int(input("Enter a number"))
str1=str(number)
i=0
while i<len(str1):
    print(str1[i])
    i=i+1
5.
i=10
while i>=1:
    print(i)
    i-=1
6.
for i in range(1,11):
    print(i)
7.
str1="banana"
for i in range(len(str1)):
    print(str1[i])
    i=i+1
8.
for i in range(1,6):
    print(i**2)
9.
list1=[2,5,8,9,10]
i=1
for i in range(len(list1)):
    if list1[i]%2==0:
        print(list1[i],"is Even")
10.
for i in range(1,21):
    if i%3==0:
        print(i)
11.
for i in range(0,3):
    for j in range(i,i+1):
        print("*"* (i+1))
12.
for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()
13.
for i in range(0,3):
    for j in range(1,i+2):
     print(j,end=' ')
    print()
14.
for i in range(1,11):
    print("2 x ",i,"=",i*2)
print()
15.
words=["hi","ok"]
for word in words:
    for char in word:
        print(char)
print()
16.
for i in range(1,11):
    if i%2==0:
        print(i," is Even Number")
    else:
         print(i,"is odd Number")
print()
17.
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        print(num)
    else:
        print("", end="")
18.
num=0
while num>=0:
        num=int(input("Enter a number (negative to exit)"))
if num<0:
  print("your number is negative.")
print("you are exit")
19.
word=input("Enter a word:")
vowels=['a','i','e','o','u']
for i in range(len(word)):
    if word[i].lower() in vowels:
     print(word[i])
20.
word=input("Enter a word:")
count=0
vowels=['a','i','e','o','u']
for i in range(len(word)):
    if word[i].lower() in vowels:
     count+=1
print(count)
21.
for i in range(5):
    print("Hello")
22.
i=1
for i in range(3):
    if i<=3:
     fav_color=input("Enter Your favourite color:")
print("Have a nice day.")
23.
letters=["A","B","C"]
for i in range(len(letters)):
    for j in range(i+1):
        print(letters[i],end=' ')
    print()

24.
word="banana"
count=0
vowels=['a','i','e','o','u']
for i in range(len(word)):
    if word[i].lower() in vowels:
     count+=1
print(count)
25.
for i in range(1,11):
    if i<5:
        print(i,"is Small")
    else:
        print(i,"is Big")
