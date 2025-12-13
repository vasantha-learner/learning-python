# try:
#     num=int(input("Enter a  num:"))
#     div=num/0
#     print(div)
# except:
#     print("Zero Division Error")

#     # i dont know the excetion but i want the program to tell me what is the exception through message
#     # except=we write the code for whqarq should happen when an execution os occured.
#     # try=we write the code which 

# # Write a program to store % numbers into a list
# list1=[]
# n=int(input("Enter a number"))
# for i in range((n)):
#     list1+=[i]
#     print(list1)
# indexe=int(input("Enter an index number:"))

# for i in range(n):
#     if i==indexe:
#         print(list1[i])

# try:
#     list1=[]
#     num=int(input("Enter a number:"))
#     for i in range(num):
#         val=int(input("Enter list vlue:"))
#         list1+=[val]
#     indval=int(input("enter index value:"))
#     print(list1[indval])
# except ValueError as msg:
#     print(msg)
# except IndexError as msg:
#     print(msg)
# else:
#     print("No exception is raised.")

# # the else block is executed only when no exception is raised.
# # Finally:This block is executed whether  exception occures or not.



# try:
#     def add(a,b):
#         return a+b
#     print(add(2,9))

# except TypeError as msg:
#     print(msg)

# except ValueError as msg:
#     print(msg)
# else:
#     print("Your code has no exceptions...")
# finally:
#     print("Thank you for visiting.")

# try:
#  sum=0
#  num=int(input("Enter a number:"))
#  for i in range(1,num+1):
#     sum+=i
#  num1=int(input("Enter a number:"))
#  sum+=num1
#  print(sum)
# except ValueError as msg:
#     print(msg)

# except TypeError as msg:
#     print(msg)

# finally:
#  print("bye.....")


# # raise Keyword=this is used to raise an execution manually in a program whenevr we want
# dict1={'name':'Keerthna','address':'Hyd','qualification':'Mca'}
# print(list(dict1.keys()))
# print(list(dict1.values()))


# try:
#     def add(a,b):
#         return a+b
#     print(add(2,9))
#     raise TypeError("U Did a mistake")
# except TypeError as msg:
#     print(msg)
# except ValueError as msg:
#     print(msg)
# else:
#     print("Your code has no exceptions...")
# finally:
#     print("Thank you for visiting.")




# # assert keyword: it is used to evaluate a condition and for debugging purpose
# try:
#  username='hlo'
#  password='hii'
# except TypeError as msg:
#  print(msg)
# assert username=='llo' and password=='hii','An assertion error raised'


# try:
#     person_name=input("enter ur name:")
#     age=int(input("Enter ur age:"))
# except TypeError as msg:
#     print(msg)
# except ValueError as msg:
#     print(msg)
# assert age>=18 ,'he is below 18'



# try:
#     num1=int(input("enter a number:"))
#     num2=int(input("Enter another Number:"))
#     div=num1/num2
#     print(div)
# except ZeroDivisionError:
#     print("not possible by zero.")
# # except TypeError as msg:
# #     print(msg)
# except ValueError:
#     print('pass integers only')



# WAP to calculate profit per item when the total profit and number of items are given.
# try:
#   totalprofit=int(input("Enter the total profit:"))
#   no_of_items=int(input("enter the no.of items:"))
#   price_item=totalprofit/no_of_items
#   print(price_item)
# except:
#   print("something went wrong please check once!")

# try:
#  dict1={'name':'some','age':19,'adress':'hyd'}
#  print(dict1['nam'])
# except Exception as error:
#  print(error)
 
# try:
#  num1=int(input("Enter a num:"))
#  if num1<=1:
#    print("Prime")
#  for i in range(2,num1):
#     if num1%i==0:
#      print("It is a Prime Number")
# except Exception as error:
#  print(error)

# try:
#  list1=[2,3,4,5]
#  list2=1
#  for i in list1:
#     list2*=i
#  print(list2)
# except  Exception as error:
#   print(error)


# try:
#     list1 = [2, 3, 4, 5]
#     list2 = 1
#     for i in list1:
#         list2 *= i
#     print(list2)
# except Exception as error:
#     print(error)


























