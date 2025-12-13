# sen=input(str("Enter a sentence:"))
# vowels="aeiou"
# v=[]
# c=[]
# for k in sen:
#   if k in vowels:
#     if k in v:
#       continue
#     else:
#      v.append(k)
#   else:
#     if k in c:
#       continue
#     c.append(k)
  
# print(v)
# print(c)


# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[]
# list3=[]
# for i in list1:
#     if i%2==0:
#         list2.append(i)
#     else:
#         list3.append(i)

# print(list2)
# print(list3)


# num=12321
# num1=str(num)
# num2=""
# for i in range(len(num1)-1,-1,-1):
#     num2+=num1[i]
# if num1==num2:
#     print("palin")
# else:
#     print("NO")


# n=int(input("Enter a numver"))
# a,b=0,1
# while a< n:
#     print(a,end=" ")
#     a,b=b,a+b


# pa,b=90,100
# print(pa+b)

# a,b=90,110
# if a>b:
#     print(a)
#     print("a is greater")
# else:
#     print(b)
#     print("B is gretaer")


# def facti(n):
#     if n<0:
#         print("Enter pos value")
#         return
#     fact=1
#     if n==0 or n==1:
#         fact=1
#     else:
#         for i in range(1,n+1):
#             fact*=i
#     print(fact)
# facti(4)

# def sim(p,t,r):
#     simple_intereset=0
#     if p==0 or r==0 or t==0:
#         simple_intereset=0
#     if p<=0 or r<=0 or t<0:
#       simple_intereset=0
#     else:
#        simple_intereset=(p*t*r)/100
#        print("simple intereset=",simple_intereset)
# sim(9,8,7)

# def fibanocci(n):
#     if n<=0:
#         print("enter a positive vall;ue:")
#         return
#     a,b=0,1
#     if n>0:
#         for i in range(1,n+1):
#             a,b=a,a+b
#             print()


# n=int(input("Enter a  number"))
# if n<=1:
#     print("False")
# else:
#     is_prime=True
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             print(False)
#     print(True)


# m,n=map(int,input("Enter two numbers:").split())
# if m<=1:
#     m=2
# for num in range(m,n+1):
#      is_primt=True
#      for i in range(2,int(num**0.5)+1):
#        if num%i==0:
#            is_primt=False
#            break
#      if is_primt:
#       print(num)


# def fib(n):
#     if n<=0:
#         print("Enter positive value")
#         return
#     else:
#         a,b=0,1
#         for i in range(n):
#             a,b=b,a+b
#         print(a)
# fib(9)

# c='f'
# print(ord(c))

# import math
# def is_per_sq(x):
#     s=int(math.sqrt(x))
#     return  s*s==x
# def is_fib(n):
#     if n<0:
#         return  False
#     return is_per_sq(5*n*n+4) or is_per_sq(5*n*n-1)

# num=int(input("Enter a number"))
# if is_fib(num):
#     print("Yes")
# else:
#     print("no")



# import math
# def is_sq(x):
#     s=int(math.sqrt(x))
#     return s*s==x
# def is_fib(n):
#     if n<0:
#         return False
#     return is_sq(5*n*n+4) or is_sq(5*n*n-4)
# num=int(input("Enter number"))
# if is_fib:
#     print("Yes")
# else:
#     print("No")


# def sum(n):
#     if n<0:
#         return False
#     else:
#      print("Sum of n natural numbers")
#      total=(n*(n+1))/2
#      return total
# print(sum(9))/

# list1=[1,2,3,4,5]
# list1[0],list1[-1]=list1[-1],list1[0]
# print(list1)

# list1=[1,2,3,4,5]
# n=int(input("enter a number"))
# if n in list1:
#      print(True)
# else:
#  print("no")

# list1=[1,2,3,4,5]
# list2=[]
# for i in range(len(list1)-1,-1,-1):
#     list2.append(list1[i])
# print(list2)

# list1=[1,2,3,4,5]
# total=1
# for i in list1:
#     total*=i
# print(total)

# list1=[8, 3, 5, 1, 9, 12]
# greatest=list1[0]
# for num in list1:
#     if num>greatest:
#         greatest=num
# print(num)

#
# list2=[] list1=[-10, 15, 0, 20, -5, 30, -2]
# list3=[]
# for num in list1:
#     if num<0:
#         list2.append(num)
#     else:
#         list3.append(num)
# print(list2)
# print(list3)

# list1=[-10, 15, 0, 20, -5, 30, -2,0,0,-5]
# list2=[]
# for i in list1:
#     if i in list2:
#         continue
#     else:
#         list2.append(i)
# print(list2)
