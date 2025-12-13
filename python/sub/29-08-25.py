# //Number functions and math module

# float1=7.63
# print(complex(float1))

# num=float(input("enter a number:"))
# print(abs(num))

# num=complex(input("enter a number:"))
# print(abs(num))

# //power()

# print(pow(2,3,5))             # 2**3 % 5

# print(round(9.6))
# print(round(3.1415676,3))        #here 3 means telling how many digits displaying aftera decimal point

# divmod()
# print(divmod(10,2))              # we get quotient and remainer as a tuple


# list1=[1,2,3,4,5]                #list
# print(max(list1))
# print(min(list1))
# print(sum(list1))

# tuple1=(1,2,3,4,5)
# print(max(tuple1))        #tuple()
# print(min(tuple1))
# print(sum(tuple1))

# set1={1,2,3,4,5,3,2}
# print(max(set1))
# print(min(set1))        #set{}
# print(sum(set1))

# num=3+4j
# print(abs(num))

# import math
# //mathematical constant
# print(math.pi)
# print(math.e)
# print(math.inf)
# print(math.nan)

# //rounding and ceiling
# print(math.ceil(4.1))
# print(math.floor(4.9))
# print(math.pow(5,2))
# print(math.sqrt(36))
# print(math.factorial(8))

# //lambda functions


# //used to write short simple functions which are not meant for reusability.
# // it consists of lambda,argumentrs and an expression.
# /note: it can have any number of arguments but has only one expresssion.
# // lambda functions are anonymous and returns the value automatically.

# //syntax>lambda arguments:expression
# def square(num):
#     sq=num*num
#     print(sq)
# square(4)

# u=lambda x:x*x
# print(u(9))

# u=lambda x,y:x+y
# print(u(9,8))

# greater=lambda a,b:a if a>b else b
# print(greater(9,76))

# greater=lambda a,b:a if a>b else b
# print(greater(10,20))

# //map function()
# list1=[1,2,3,4,5]
# m=list(map(lambda x:x*x,list1))
# print(m)

# list1=[1.6,2.6,3.7,4.0,5.0]
# m=list(map(lambda x:int(x),list1))
# print(m)

# list1=[1,2,3,4,5]
# m=list(map(lambda x:"even" if x%2==0 else "is odd",list1))
# print(m)

# list1=[1,2,3,4,5]
# m=list(filter(lambda x:x%2==0,list1 ))
# print(m)

# num=[36,81,65]
# if num**(1/2)==int:
#     print("perfect square",num)
# else:
#     print("no")