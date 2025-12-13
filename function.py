# functions:
# def add(a,b):         //declaring a function
#     print(a+b)
# add(10,29)


# def add(a,b):
#     return(a+b)
# print(add(10,20)+30)
    
# def sum(a,b,c):
#     return(a+b+c)
# print(sum(20,30,40))

# def mul(a,b,c):
#     return(a*b*c)
# print(mul(1,2,3)+90)

# def div(a,b):
#     return(a//b)
# var=div()

# print(div(12,3))


# def exp(a,b):
#     return(a**b)
# print(exp(2,3))

# def evenorodd(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")
# evenorodd(10)

# def evenodd():
#     sum=0
#     num=1
#     list1=[1,2,3,4,5,6,7,8,9,10]
#     for num in range(len(list1)):
#         if num%2==0:
#                 sum=sum+num
#     return sum   
# print("sum of even numbers",sum)
# print(evenodd())  

def greetings(name,institute,course='your cousre'):
    print(f'welcome {name} to {course} at {institute}')
greetings('vassu','python','10k coders')