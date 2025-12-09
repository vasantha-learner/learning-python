
# String replication

# num1='sai'
# print((num1+' ')*3,' ')


# Take a product name as string it price as float and quantity as 

# Pro_name="Bananas"
# Price=float(input("Enter your product price:"))
# Quantity=int(input("Enter a quantity value:"))
# total_price=Price*Quantity
# print(str(total_price))

# 3.Input is='_*_' and output is='_*__*__*_'

# user_input='_*_'
# print(user_input*3)

# 4.Take two numbers as a strings and add them before and after ttype casting

# num1=int(input("enter a number:"))
# num2=float(input("Enter a number:"))
# sum1=num1+num2
# print(str(sum1))
# sum2=num1+int(num2)
# print(str(sum2))


# WAP to print if temperature is above 35c print its hot else print the temp moderate
# temperature=float(input("enter your area temperature:"))
# print("hot" if temperature>35 else "moderate" )


# Age=int(input("Enter your age:"))
# citizenship=input("Enter your citizenship:").upper()
# print("Eligible" if Age>18 and citizenship=='INDIAN' else " you are not eligible")


# WAP to give discount to a customer such that purchase of amount >10000 he is eligible for 10% discount.

# purchase_amount=float(input("Enter your total amount:"))
# if purchase_amount>10000:
#     perc=10
#     discount=(purchase_amount*perc)/100
#     print(f"your total bill-{purchase_amount-discount}")
# else:
#     print(f"your total bill-{purchase_amount}")



# check whether the sum of two digits is even or not
# num1=int(input("Enter number1:"))
# num2=int(input("Enter number2:"))
# sum=num1+num2
# if sum%2==0:
#     print("The sum of numbers is Even")
# else:
#     print("The sum of number is odd")





# Wap to remove duplicates elemnets from a list

# list1=[1,2,3,4,5,6,7,3,4,5,24,89,90,90,89]
# list2=[]
# for i in list1:
#     if i in list2:
#         continue
#     else:
#         list2+=[i]
# print(list2)


# list1=[1,2,3,4,5,6,7,3,4,5,24,89,90,90,89]
# list2=[]
# flag=False
# for i in range(len(list1)):
#     for j in range(len(list2)):
#      if list1[i]==list2[j]:
#         flag=True
#         break
#      else:
#         flag=False
# if flag==False:
#     list2+=[list1[i]]
# print(list2)
 


# list1=[0,1,0,2,0,3,0,4,0,5]
# list2=[]
# list3=[]
# for i in list1:
#     if i<=0:
#         list2+=[i]
#     else:
#         list3+=[i]
# for i in range(len(list2)):
#     list3+=[list2[i]]
# print(list3)



tuple1=(1,2,3,4,5,6,7,8,9,10)
tuple2=()
num=int(input("Enter a num:"))
for i in range(len(tuple1)):
    for j in range(i+1,len(tuple1)):
        if tuple1[i]+tuple1[j]==num:
           tuple2=(tuple1[i],tuple1[j])
print(tuple2)



