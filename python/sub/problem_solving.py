# 1. Print reverse of a string (without built-in function)
string1="Python"
rev_str=""
for i in range(len(string1)-1,-1,-1):
    rev_str+=string1[i]
print("original string:",string1)
print("reversed string:",rev_str)

# 2. Average of marks of five students
student_marks=[100,200,300,400,500]
i=1
count=0
for i in range(len(student_marks)):
    count+=student_marks[i]
average=count/len(student_marks)
print("Average of marks of five students is:",average)

# 3. Check whether the given sides form a triangle or not
a, b, c = 5, 5, 5
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The given sides form a triangle")
else:
    print("The given sides do not form a triangle")