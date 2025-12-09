# class Evennumbers:
#     def __init__(self):
#         self.num=0

#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.num+=2
#         return self.num
# evens=Evennumbers()
# print(next(evens))
# print(next(evens))
# print(next(evens))
# print(next(evens))
# print(next(evens))



# Crearinf our own iterators:
# File objects already has __iter__() and __next__() method in it so it is an iterators.
# Hence anything that contains a __iter__() and 


# try:
#  class Stopwatch:
#     def __init__(self,num):
#         self.num=num
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=0:
#             raise StopIteration('stop')
#         self.num-=1
#         return self.num

#  s1=Stopwatch(4)
#  print(next(s1))
#  print(next(s1))
#  print(next(s1))
#  print(next(s1))
#  print(next(s1))
# except  StopIteration :
#  print("stop")



# list1=[1,2,3,4,5]
# for i in list1:
#     print(i)

# print('________ ___________________')
# it1=iter(list1)
# while True:
#     try:
#         i=next(it1)
#         print(i)
#     except StopIteration:
#         break




# filename=open("path")
# lines=filename.readlines()
# for line in lines:
#     print(line)
# print(next(filename))
# print(next(filename))


# Iterators are used to load chunks of huge data into memory and process them,so that a huge file won't crash or lag the system.




