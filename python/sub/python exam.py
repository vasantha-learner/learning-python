1. for i in range(1, 20):
    if i % 3 == 0 and i % 5 != 0:  
        print(i, end=" ")
    elif i % 5 == 0 and i % 3 != 0: 
        print(i, end=" ")

2. n = 7
for i in range(1, n+3,2):
    print("*" * i)

3.def second_largest(lst):
    if len(lst) < 2:
        return None  
    if lst[0] > lst[1]:
        first, second = lst[0], lst[1]
    else:
        first, second = lst[1], lst[0]
    for i in range(2, len(lst)):
        if lst[i] > first:
            second = first
            first = lst[i]
        elif lst[i] > second and lst[i] != first:
            second = lst[i]
    return second if first != second else None
print(second_largest([49, 44, 45, 99,43])) 


4.def is_palindrome(s):
    rev = ""                        
    for ch in s:
        rev = ch + rev              
    if s == rev:
        return True
    else:
        return False
print(is_palindrome("madam"))    
   


5.def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(45, 15))  



6.def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def filter_primes(lst):
    return [x for x in lst if is_prime(x)]
print(filter_primes([2, 4, 6, 7, 9, 11, 15, 17]))

7.def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
print(word_frequency("This is a test this is only a test"))


8.def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
print(generate_primes(10))


9.def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs
print(find_pairs([2, 4, 3, 7, 5], 7))



10.def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == num
print(is_armstrong(153))  