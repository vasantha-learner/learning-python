# Write a program to print your name, age, and favorite color.
# name="vassu"
# age=18
# fav_color="green"
# print("name=",name,"age=",age,"favourite color:",fav_color)

# Take two numbers from the user and print their sum, difference, product, and quotient.
# num1=14
# num2=4
# print("sum=",num1+num2)
# print("differenbce=",num1-num2)
# print("Product=",num1*num2)
# print("Quotient=",num1//num2)

# Write a program to check whether a number is even or odd.
# num1=14
# if num1%2==0:
#     print("Even")
# else:
#     print("odd")

# Write a program to find the greatest of three numbers.
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# c=int(input("Enter a number:"))
# if(a>b and a>c):
#  print("a is greater")
# elif(b>c and b>a):
#  print("b is greater")
# else:
#   print("c is greater")

# Write a program to check if a number is positive, negative, or zero.
# number=int(input("Enter a number:"))
# if number>0:
#     print("positive")
# elif number<0:
#     print("Negative")
# else:
#     print("Zero")

# Print numbers from 1 to 50 using a loop.
# i=1
# while  i<51:
#         print(i)
#         i+=1
    
# Print the multiplication table of any number entered by the user.
# num1=int(input("Enter a number:"))
# for i in range(11):
#     num2=num1*i
#     print(f"{num1} x {i} = ",num2)
#     i=i+1

# Find the sum of first 10 natural numbers.
# count=0
# for i in range(11):
#     count+=i
# print("sum of total numbers:",count)

# write a program to count the number of digits in a number.
# num1=input("Enter a number:")
# print("total no.of digits:",len(num1))

# print the following pattern:
# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# Store 10 numbers in a list and print only the even numbers.
# list1=[12,43,56,78,90,54,89,99]
# for i in range(len(list1)):
#     if list1[i]%2==0:
#      print("Even",list1[i])
#      i+=1

# Find the largest and smallest number in a list (without using min/max).
# list1=[12,43,56,78,90,54,89,99]
# smallest=list1[0]
# largest=list1[0]
# for num in list1:
#     if num<smallest:
#         smallest=num
#     if num>largest:
#         largest=num
# print("smallest",smallest)
# print("largest",largest)

# 13.
# list1 = [12, 43, 56, 78, 90, 54, 89, 99]

# reversed_list = []   # empty list to store elements

# # go through list from last to first
# for i in range(len(list1) - 1, -1, -1):
#     reversed_list.append(list1[i])
# print("Reversed list:", reversed_list)

# 
# count=0
# tuple1=(10,20,30,40,50)
# for num in tuple1:
#     count+=num
# print("count:",count)

# tuple1=(10,20,30,40,50)
# new_tuple1=list(tuple1)
# print(new_tuple1)
# print(type(new_tuple1))

# 
# 
# text="Harish Mahadev"
# freq={}
# for ch in text:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)

# 
# dict1={"age":12,"name":"vaasu"}
# # dict2={"add":"cpp","qual":"b.tech"}
# # dict3=dict1.copy()
# # dict3.update(dict2)
# # print(dict3)

# # 
# fruits={"mango":120,"pine apple":300,"dragon fruit":150,"banana":100,"grapes":80}
# fruit=input("Enter what fruit you want?:").lower()
# if fruit in fruits:
#     print(f"the price of {fruit} is {fruits[fruit]}")
# else:
#     print("Sorry this fruit is currently not available.")

# fruits = {"mango":120, "pine apple":300, "dragon fruit":150, "banana":100, "grapes":80}

# fruit = input("Enter what fruit you want?:").lower()   # convert user input to lowercase

# if fruit in fruits:
#     print(f"The price of {fruit} is {fruits[fruit]}")
# else:
#     print("Sorry this fruit is currently not available.")
