# num1=int(input("Enter a number:"))
# i=1
# count=1
# for i in range(1,num1+1):
#    count*=(i)  
# print("Factorial of a given number is:",count)

# num1=int(input("Enter a number"))
# num2=0
# num3=1
# num4=num2+num3
# print("Fibanocci Series")
# for i in range(1,num1+1):
#    num5=num1(i-2)+num1(i-1)
#    print(num5)
#    print("Fibanocci series:",num1(i-1))

# Check whether a number is perfect square or not
# num1=int(input("Enter a number:"))
# num2=int(num1**(1/2))
# if num2*num2==num1:
#     print("Perfect Square")
# else:
#     print("given number is not a perfect square")

# print sum of digits of a number
# str1="123434"
# i=1
# count=0
# for i in range(len(str1)):
#     # str2=int(str1[i])
#     count+=i
#     i=i+1
# print("count",i)

num1=123
rev=0
digit=num1%10
rev=rev*10+digit  
    # sum+=digit 
    num1=num1//10
    if num1==rev:
        print("Given number is palindrome") 
    else:
        print("Given number is not a palindrome")                                              

# print reverse of a number
# num1=int(input("Enter a number"))
# rev_num=""
# for i in range(num1,-1,-1):
#     rev_num=num1[i]
#     print(i)