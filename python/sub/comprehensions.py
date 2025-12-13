squares = [x**2 for x in range(1, 21) if x % 2 != 0]
print(squares)

cubes = {x: x**3 for x in range(1, 11)}
print(cubes)

string = "programming in python"
vowels = {ch for ch in string if ch in 'aeiou'}
print(vowels)


d = {'a': 1, 'b': 2, 'c': 3}
rev_d = {v: k for k, v in d.items()}
print(rev_d)

table = [(n, n**2, n**3) for n in range(1, 6)]
print(table)


nums = [-3, -1, 0, 2, 4, -6]
positives = [x for x in nums if x > 0]
print(positives)


sentence = "Python programming"
word_lengths = {word: len(word) for word in sentence.split()}
print(word_lengths)


labels = ["Even" if n % 2 == 0 else "Odd" for n in range(1, 11)]
print(labels)



squares = tuple(n**2 for n in range(1, 8))
print(squares)


nums = [1,2,2,3,4,4,5,5,6]
unique_sorted = sorted(set(nums))
print(unique_sorted)

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

Right inverted triangle
rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * i)



Number square pattern
rows = 5
for i in range(1, rows + 1):
    print((str(i) + " ") * rows)


increaing number pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



decreaing Number pattern
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


Hollow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


rectangle

rows, cols = 3, 6
for i in range(rows):
    for j in range(1, cols + 1):
        print(j, end=" ")
    print()



pyramid pattern
i = 5
j= 5
for i in range(1, i+ 1):
    print(" " * (j - i), end="")
    print("* " * i)


inverted pattern
i = 5
j = 5
for i in range(i, 0,-1):
    print(" " * (j - i), end="")
    print("* " * i)



Diamond pattern
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
