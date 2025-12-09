
# for num in n:
#     if num%3==0 or num%5==0 and num%7!=0:
#      print(num)


list1=[]
for num in range(101):
     if num%3==0 and num%5==0 and num%7!=0:
          list1+=[num]
print(list1)


# list1=[1,2,3,4,5]
# list2=[1,2,7,8,9]
# list3=" "
# for i in list1:
#      for j in list2:
#           if i==j:
#            list3=list2[i]
# print(list3)
