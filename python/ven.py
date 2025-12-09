
#conditional Statements:

#conditonal stmts allow us to make decisions based on a certain condition
# syntax:conditional stmts invoves teo keywords
# if,else
#     if(condition):
#         block od Code 
#     else:
# job=False
# if job==True:
#     print("go to job")
# else:
#     print("go to coaching")
# if you hvae more than one conditin,we involve ine more keyword called elif which is  short form else if
# money=True
# job=True
# money=True
# if(money==True and job==True ):
#     print("you are good")
#     print("Start ur business")
# elif job==True:
#     print("go to job")
# elif money==True:
#     print("go to tour")
# elif skills==True:
#     print("start a company")
# else:
#     print("go to coaching")


# money=int(input("Enter ur money:"))
# if(money==10):
#   print("You can take a  water")
# elif(money>=100):
#   print("You can take a cup of tea")
# else:
#   print("take a cup of coffee")
# age=int(input("Enter ur age"))
# if(age>18):
#     print("u r eligible")
# else:
#     print("u r not eligible")


# perc=int(input("Enter ur precentage:"))
# if (perc >= 90):
#     print("O grade is obtained")
# elif(perc >=80):
#     print("A grade is obtained")
# elif(perc >=75):
#     print("B grade is obtained")
# elif(perc>=60):
#     print("C grade is obtained")
# elif(perc>=50):
#     print("D grade is obtained")
# else:
#     print("F grade is obtained")


# age=int(input("Enter your age:"))
# if(age>=18):
#      license=input("do you have license?:")
#      if(license=="yes"):
#       print("eligible to dive")
#      else:
#       print("get license")
# else:
#  print("minor")

# marks=int(input("enter your marks:"))
# if(marks>=35):
#     if(marks>=90):
#      print(" good,you are qualified")
#     elif(marks>=75):
#        print("you need some practice")
#     elif(marks>=65):
#       print("try to do hardwork")
#     elif(marks>=55):
#        print("ok but need  more and more pratice")
#     elif(marks>=45):
#        print("ok try to next level")
#     elif(marks>=35):
#        print("just pass")
# else:
#     print("you are not qualified")

#TASK:
# Number=int(input("Enter a number: "))
# if(Number>0):
#   print("given number is positive")
#   if(Number>50):
#     print("It is greater than 50")
#     if(Number%2==0):
#       print("Given number is even")
#     else:
#      print("Given number is odd")
#   else:
#     print("it is less than  50")
# else:
#   print("Given number is negative")

# age=int(input("Enter your age:"))
# license=input("do you have license?:")
# if(age>=18 and  license=="yes"):
#      print("eligible to dive")
# else:
#       print(" u are a monor get license")
      
#print(eligible if age>=18 else "not eligible")    //ternary operator
# num=int(input("enter a number"))
# print("even" if num%2==0 else "odd")

# list1=[1,2,3,4,5,6,7,8,9,10]
# for i in list1:
#     print("hello world ",i)


# list1=list(range(1,51))
# print(list1) 
# for i in list1:
#     print("hello ",i)     
#                                    
# for i in range(1,11,3):
#     print(i)

# for i in range(12,1,-1):
#   print(i)

# list1=list(range(1,51))
# print(len(list1)) 

# list1=["apples","mangoes","grapes","bananas","oranges"]
# for i in range(len(list1)):
#     print(i,list1[i])

# str1="vassu"
# for i in range(len(str1)):
#     print(i,str1[i])


# for i in range(5):
#     for j in range(5):
#         print('i value:',i,'j value:',j)



# list1=["pinninti"]
# list2=["vassu","gowri","laxmi"]
# for i in list1:
#     for j in list2:
#      print(i,j)


# i=10
# while i>0:
#     print('vassu','ram')
#     i=i-8

# while True:
#     print("hello")




# a=int(input("Enter a number:"))
# while a>10:
#      while a<20:
#          print("hlo")
#          a=a+1
# else:
#      print("given num is less than 10")
     

# LOOP CONTROL STATEMENTS: 
#  BREAK,CONTINUE,PASS
# Break:it is used to exit a loop when a certain condition is met
#CONTINUE:it is used to stop the current iteration and start new iteration
# PASS:it is used to perform nothing,to reserve space for furter use.

# i=0
# while True:
#     print(i)
#     if i==1000:
#         break
#     i=i+1
    
# list1=[1,2,3,4,5,6,7,8,9]
# for i in list1:
#     print(i)
#     if i==5:
#         break
#     i=i+1

# i=1
# while(i<=50):
#     if i==23: 
#       i=i+1  
#       continue
#     print(i)  
#     i=i+1


# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)
#     i=i+1

# i=0
# while(i<=10):
#     if i==5:
#         i=i+1
#         continue
#     print(i)
#     i=i+1
# i=0
# while(i<=10):
#      i=i+1
#      if i==5:
#         pass
#      print(i)
#      i=i+1

# num=input("Enter a number")
# sum=0
# for i in range(len(num)):
#      digits=int(num[i])
#      sum=sum+digits
# print("sum_of_digits",sum)

# for i in range(1,100):
#     print(i)
#     if i%57==0:
#       print("Current number is divisible by 57")
#       break      
# print(i)
     
# while True:
#     string1=input("Enter a value(enter 'exit') to exit the loop:")  
#     if string1.lower()=='exit':
#         print("Have a nice day")
#         break
#     print(string1)

# for i in range(1,51):
#     if i%2==0:
#         continue
#     print(i)

# vowel=['a','i','e','o','u']
# i=0
# str1=input("Enter a string")
# if str1[i]==vowel:
#       print()
#    i=i+1
# break

# str1=input("Enter a string")
# vowels='aeiou'
# for i in str1:
#     if i.lower() in vowels:
#         continue
#     print(i,end='')

# list1=['exit','quit']
# while True:
#     string1=input("Enter a string:")
#     if string1.lower() in list1:
#         print("Have a good day")
#         break
#     print(string1)