# recursive functions
# it is a phenomenon of calling a function within itself      each function call solves a smaller version of same problem
# def facti():
#     fact=1
#     for i in range(2,8):
#         fact*=i
#     print("factorials",fact)
# facti()

# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(3))                                                      
# def fibanocci(num):
#     if num==0:  
#      return 0
#     elif num==1:
#      return 1
#     else :
#        return fibanocci(num-1)+fibanocci(num-2)
# for i in range(11):
#  print(fibanocci(i),end=' ')

# Reverse of a string using recursion
def reverseii(name):
    if len(name)==0:
        return name
    else:
        return  reverseii (name[::-1])
print(reverseii("vassu"))
# String1="vassu"
# print(String1[::-1])