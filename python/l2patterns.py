# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*"," ",end=" ")
#     print()

# n=5
# for i in range(n,-1,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*"," ",end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*"," ",end=" ")
#     print()
# for i in range(n,-1,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*"," ",end=" ")
#     print()

# n=5
# for i in range(n,-1,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*"," ",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*"," ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         if(j==0 or j==i-1 or i==n-1):
#             print("*"," ",end=" ")
#     print()
# for i in range(n,-1,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         if(j==0 or j==i-1 or i==n-1):
#             print("*"," ",end=" ")
#     print()




# merge two traingles
# n=5
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n,-1,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    for j in range(1,2*(n-i))