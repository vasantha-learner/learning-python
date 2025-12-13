1.def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5)) 


2.def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
print(sum_n(5))  


3.def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("navya"))  

1.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))  


2.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("madam"))  



3.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("madam"))  



4.
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)
print(power(2, 5)) 



1.is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(5)) 

2.
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20)) 

3.
square = lambda x: x * x
print(square(7))  


1.
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit) 



2.
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  



3.
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  



4.
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs) 
