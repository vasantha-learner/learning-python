Check if a number is divided by both 3 and 5
Number=int(input("Enter a number:"))
if(Number%3==0 and Number%5==0):
    print("Given Number is Divisible both 3 and 5")
else:
    print("Given Number is not divisible both 3 and 5")

A=int(input("Enter number A:"))
B=int(input("Enter number B:"))
if(A>B):
    print("A is Greater")
else:
    print("B is Greater")


Ask for a score and print Grade A/B/C/Fail
Score=int(input("Enter your score:"))
if(Score>90):
    print("A Grade obtained")
elif(Score>70 and Score<90):
    print("B Grade is obtained")
elif(Score>45 and Score<70):
    print("c Grade is Obtained")
else:
    print("Student failed")

Check if a number is positive and even
Number=int(input("Enter a number:"))
if(Number>0 and Number%2==0):
    print("Positive and Even")
else:
    print("odd")

Ask the users age and suggest:
Age=int(input("Enter your age:"))
if(Age>20):
    print("You are a adult")
elif(Age>13 and Age<19):
    print("You are teen")
else:
    print("you are a child")
