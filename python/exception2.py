# try:
#     list1=[1,2,3,4,5]
#     sum=0
#     for i in range(len(list1)):
#         sum+=list1[i]
#     print(sum)
# except (TypeError,IndexError):
#     print("something went wrong!")
# finally:
#     print("Bye Bye")

# Finallly=this block executed whether an exception is raised or not






# try:
#     list1=[1,2,3,4,5]
#     sum=0
#     for i in range(len(list1)):
#         sum+=list1[i+1]
#     print(sum)
# except (TypeError,IndexError) as e:
#     print("something went wrong!")
#     print(e)
# finally:
#     print("Bye Bye")

# try:
#     list1=[1,2,3,'4',5]
#     sum=0
#     sum2=0
#     for i in range(len(list1)):
#         if i%2==0:
#          sum+=list1[i]
#     print(sum)
#          else:
#          sum2+=list1[i]
#          print(sum2)
# except (TypeError,IndexError) as e:
#     print("something went wrong!")
#     print(e)

# finally:
#     print("Bye Bye")


# try:
#     num=int(input("Enter a number:"))
#     if num%2==0:
#        print("Even")
#     else:
#      print("odd")
# except:
#     print("error")
# finally:
#  print(f"{num} exexuted successfully")














# difference between else and finally:
# else block executed when no exception where as finally block exceuted whether exception is raosed or not



# 