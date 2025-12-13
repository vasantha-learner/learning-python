# emnumerated function = it is used to  provide index values to a sequence of data
# syntax=enumerate(sequence,start=0)
# ruits=["apple","banana","grapes"]f
# count=0
# for count in range(len(fruits)):
#     print(fruits[count],count)
#     count+=1

# fruits=["apple","banana","grapes"]
# for index,fruit in enumerate(fruits,start=101):
#     print(index,' ',fruit)

# fruits={1:"Apple",2:"Banana",3:"Grapes",4:"Dragon"}
# for index,value in enumerate(fruits.values(),start=10):
#     print(index,' ',value)

# fruits={"Apple","Banana","Grapes","Dragon","Apple"}
# for index,fruits in enumerate(fruits,start=10):
#     print(index,' ',fruits)
    
# //zip() is uses to access two or more sequences at once ,by default it returns a sequences odf pairs of tuples
students=['saleem','rahul','venu','mahesh','kavya','navya']
scores=[36,79,23,56,89,90]
roll_numbers=[2,4,6,8,9,12]
combo=zip(roll_numbers,students,scores)
print(combo)
for i in combo:
    print(i)
# for roll_num,student,score in zip(roll_numbers,students,scores):
#     print(roll_num,student,score)

# for i in range(len(students)):
#      print(roll_numbers[i],students[i],'scored',scores[i])
