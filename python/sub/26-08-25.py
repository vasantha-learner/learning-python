# numbers=(1,2,3,4,5)
# squares=(i*i for i in numbers)
# print(squares)

# numbers=(1,2,3,4,5)
# squares=[i*i for i in numbers]
# print(tuple(squares))

# numbers=[1,2,3,4,5,6,7,8,9,10]
# squares=[i*i for i in numbers if i%3==0 and i%5==0]
# print(squares)
# print(tuple(squares))
# print(set(squares))

# numbers=(1,2,15,23,30,45,89)
# squares=[i*i for i in numbers if i%3==0 and i%5==0]
# d={i:i*i for i in numbers if i%3==0 and i%5==0}
# print(squares)
# print(tuple(squares))
# print(set(squares))
# print(d)

# numbers="comprehensions"
# cubes={ch:ch*2 for ch in numbers}
# print(cubes)

# ns="comprehensions"
# vowels="aeiou"
# s=[ch for ch in ns if ch in vowels]
# print(s)

# for i in range(5):
#     for j in range(3):
#         print('*',end=' ')
#     print(' ')


for i in range(4,-1,-1):
    for j in range(i+1):
        print("*",end=' ')
    print(' ')
