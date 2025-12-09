
1. Square of a Number

square = lambda x: x ** 2
print(square(5)) 


2. Check Even or Odd

is_even = lambda x: x % 2 == 0
print(is_even(4))  
print(is_even(7))  


3. Maximum of Two Numbers

max_num = lambda a, b: a if a > b else b
print(max_num(10, 20)) 


4. Add Two Numbers

add = lambda a, b: a + b
print(add(4, 6))  



1. 

pairs = [(1, 5), (2, 3), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  


2. Filter Even Numbers

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  


3. Map with Lambda (Cube each number)

numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x ** 3, numbers))
print(cubes)  


4. Reduce with Lambda (Product of numbers)

from functools import reduce
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  


1. Sort by Name Length
words = ["apple", "banana", "kiwi", "grapes"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words) 


4. 

check_num = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print(check_num(10))   
print(check_num(-5))   
print(check_num(0))    


5. 

data = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))
print(sorted_dict)  



6.
check_conditions = lambda x: "Even & >10" if x % 2 == 0 and x > 10 else ("Odd" if x % 2 != 0 else "Other")
print(check_conditions(12))  
print(check_conditions(7))   
print(check_conditions(8))   


