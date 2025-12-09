# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()


# for i in range(3):
#     for j in range(5):
#         print("*",end=" ")
#     print()


# for i in range(5):
#     for j in range(3):
#         print("*",end=" ")
#     print()

# for row in range(6,-1,-1):
#     for j in range(row):
#         print("*",end=" ")
#     print()

# n=6
# for i in range(1,n+1):
#     print(" " * (n-i) + "*" * i)

# n=6
# for i in range(1,n+1):
#     print((n-i)*"*"+" "*i)
n=5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 and j == 0 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


