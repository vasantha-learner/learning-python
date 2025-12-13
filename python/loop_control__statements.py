#  LOOP CONTROL STATEMENTS: 
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