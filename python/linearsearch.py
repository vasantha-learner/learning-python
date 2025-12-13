# list1=[1,2,3,4,5,6,7,8,9,10]
# target=9
# def linearsearch(seq,target):
#     index=0
#     while(index<len(list1)):
#         if seq[index]==target:
#             return index
#         index+=1
#     return -1
# result=linearsearch(list1,target)
# if result!=-1:
#     print("Element found",result)
# else:
#     print("element not found")





# list1=[1,2,3,4,5,6,7,8,9,10]
# target=7
# def Binarysearch(seq,target):
#  initial=0
#  final=len(seq)-1
#  while initial<=final:
#     mid=(initial+final)//2
#     if target==seq[mid]:
#      return mid
#     elif target>seq[mid]:
#      initial=mid+1
#     else:
#      final=mid-1
#  return -1
# result=Binarysearch(list1,target)
# if result!=-1:
#  print("Element found",result)
# else:
#  print("Element not found")




# list1=[1,2,9,4,5,6,5,8,3,10]
# def bubblesort(seq):
#     num=len(seq)
#     for i in range(num):
#         swap=False
#         for j in range(0,num-i-1):
#             if seq[j]>seq[j+1]:
#                 seq[j],seq[j+1]=seq[j+1],seq[j]
#                 swap=True
#         if not swap:
#             break
# bubblesort(list1)
# print(list1)




