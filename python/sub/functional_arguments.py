# functional arguments:
# function key word arguments
# def details(name,age,address,course,number):
#     print(f'''Hello {name} as of thid year you ae of agqe{age} ypu live at {address},studying{course},and your contact number is{number}''')
# details(name="abc",address="789",course="python",age=56,number=56789)


# def my_personal_info(name,study,village,college,age,number,mom_name):
#     print(f'''Hi My name is {name} i am  from {village} completed my {study} in {college},i am {age} years old my number is {number} my mother name is {mom_name}''')
# my_personal_info(age="21",name="vassu",village="Cheepurupalli",college="SSE college",number=1234545,mom_name="Laxmi",study="B.tech")

# def number(*num):                //variable length arguments
#     sum=0
#     for i in num:
#         sum+=i
#     return sum
# print(number(1,2,3,4,5))

# def number(*num):
#     mul=1
#     for i in num:
#         mul*=i
#     return mul
# print(number(1,2,3,4,5))

# def detailes(**info):     //variable length keyword arguments
#     for key,value in info.items():
#         print(f'{key}:{value}')
# print(detailes(name="vasu",study="B.tech",course="python"))

# def detailes(**urdtls):
#     for i,j in urdtls.items():
#         print(f'{i}:{j}')
# detailes(name="vasu",age=45,address="Kphb",study="B.tech-CSE",Number=1232456,college="SSS college",mom_name="Laxmi")


