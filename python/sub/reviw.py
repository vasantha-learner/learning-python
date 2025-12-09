# def even_odd(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("odd")
# even_odd(17)

# def greater(a,b,c):
#    if a>b and a>c:
#       print("a is greater")   
#    elif b>a and b>c:
#       print("b is greater")  
#    else:
#       print("C is greater")
# greater(323,90,89)

# def leap_year(n):
#     if n%400==0 or  (n%4==0 and n%100 !=0):
#         print("leap year")
#     else:
#         print("no")
# leap_year(2100)

# for i in range(1,51):
#     print(i)

# print("7 multiplication table:")
# for i in range(1,11):
#     print(f"7x{i}=",7*i)

# num=123
# sum=0
# while num>0:
#     digits=num%10
#     sum+=digits
#     num=num//10
# print("sum of digits:",sum)

# num=123
# rev=0
# while num>0:
#     digits=num%10
#     rev=rev*10+digits
#     num=num//10
# print(rev)

# string1="hari"
# rev=''
# for ch in string1:
#    rev=ch+rev
#    print(rev)

# def string_rev(s):
#      rev=''
#      for ch in s:
#         rev=ch+rev
#      print(rev)
# string_rev('vassu')

# s="harish"
# rev=''
# for ch in s:
#     rev=ch+rev
# print(rev)

# s="harisioih"
# vowels="aeiou"
# count=0
# for i in range(len(s)):
#     if s[i] in vowels:
#      print(s[i])
#      count+=1
# print("total",count)

# s="madam"
# rev=''
# for ch in s:
#     rev=ch+rev
# print(rev)
# if rev==s:
#     print("palindrome")
# else:
#     print("not a palindrome")

# list1=[23,56,78,12,70]
# n=len(list1)
# for j in range(n-1):
#    for i in range(n-1-j):
#     if list1[i]>list1[i+1]:
#       list1[i],list1[i+1]=list1[i+1],list1[i]
#       i=i+1
# print(list1)
# print(list1[4])
# print(list1[0])

# list1=["apple","ball","cat","fan","apple","cat"]
# list1=set(list1)
# print(list1)

# list1=[1,2,3,4,5]
# sq=[num*num for num in list1]
# print(sq)

# set1={"apple","ball","bag"}
# set2={"hlo","ball","bag"}
# set3=set1.union(set2)
# print(set3)

# list1=["apple","ball","cat","fan","apple","cat"]
# print(tuple(list1))

# string1="hariiishhhooo"
# vowels="aeiou"
# for i in range (len(string1)):
#     if string1[i] in vowels:
#      print(string1[i])
# s2=string1[i]
# print(set(s2))

# dict1={1:"apple",2:"ball"}
# dict2={3:"cat",4:"dog"}
# dict1.update(dict2)
# print(dict1)

# d={1:"a",2:"b",3:"c"}
# e={4:"f",5:"g"}
# d.update(e)
# print(d)

# s="python review tasks"
# freq={}
# for ch in s:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)

# d={1:"a",2:"b",3:"c"}
# print(max(d.items()))

# def fact(n):
#     factorial=1
#     for i in range(1,n+1):
#      factorial*=i
#     print(factorial)
# fact(4)

# def uuu(a):
#  x=lambda a:"true" if a%3==0 else "false"
#  print(x(a))
# uuu(9)

# def aaa(x,y):
#  z=lambda x,y:x+y
#  print(z(x,y))
# aaa(7,8)

# list1=[1,2,3,4,5]
# list1=list(map(lambda x:x*x ,list1))
# print(list1)

# list1=[1,2,3,4,5]
# list1=list(map(lambda x:x*x ,list1))
# print(list1)

# list1=[1,2,3,4,5]
# list1=list(filter(lambda x:x%2==0 ,list1))
# print(list1)

# list1=[1,2,3,4,5,6]
# list1=list(filter(lambda x:x%3==0,list1))
# print(list1)

