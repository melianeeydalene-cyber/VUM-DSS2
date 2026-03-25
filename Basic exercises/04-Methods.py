# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 18:47:39 2026

@author: melia
"""

#%% 1. Smallest of Three Numbers

def smallest(a, b, c):
    return min(a, b, c)

a = int(input())
b = int(input())
c = int(input())

print(smallest(a, b, c))


#%% 2. Vowels Count

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

text = input()
print(count_vowels(text))


#%% 3. Characters in Range

def chars_between(a, b):
    start = min(ord(a), ord(b))
    end = max(ord(a), ord(b))
    return [chr(i) for i in range(start + 1, end)]

a = input()
b = input()

print(*chars_between(a, b))


#%% 4. Password Validator

def is_valid(password):
    valid = True

    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        valid = False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        valid = False

    digits = sum(1 for ch in password if ch.isdigit())
    if digits < 2:
        print("Password must have at least 2 digits")
        valid = False

    if valid:
        print("Password is valid")

password = input()
is_valid(password)


#%% 5. Add and Subtract

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a = int(input())
b = int(input())
c = int(input())

print(subtract(add(a, b), c))


#%% 6. Middle Characters

def middle(text):
    n = len(text)
    if n % 2 == 0:
        return text[n//2 - 1:n//2 + 1]
    else:
        return text[n//2]

text = input()
print(middle(text))


#%% 7. NxN Matrix

def matrix(n):
    for _ in range(n):
        print(" ".join([str(n)] * n))

n = int(input())
matrix(n)


#%% 8. Factorial Division

import math

def fact_div(a, b):
    return math.factorial(a) / math.factorial(b)

a = int(input())
b = int(input())

print(f"{fact_div(a, b):.2f}")


#%% 9. Palindrome Integers

def is_palindrome(n):
    return n == n[::-1]

while True:
    num = input()
    if num == "END":
        break

    print("true" if is_palindrome(num) else "false")


#%% 10. Top Number

def is_top(n):
    digits = [int(d) for d in str(n)]
    return sum(digits) % 8 == 0 and any(d % 2 != 0 for d in digits)

n = int(input())

for i in range(1, n + 1):
    if is_top(i):
        print(i)


#%% 11. Array Manipulator

arr = list(map(int, input().split()))

while True:
    cmd = input()
    if cmd == "end":
        break

    parts = cmd.split()

    if parts[0] == "exchange":
        idx = int(parts[1])
        if idx < 0 or idx >= len(arr):
            print("Invalid index")
        else:
            arr = arr[idx+1:] + arr[:idx+1]

    elif parts[0] in ["max", "min"]:
        parity = parts[1]
        nums = [x for x in arr if x % 2 == 0] if parity == "even" else [x for x in arr if x % 2 != 0]

        if not nums:
            print("No matches")
        else:
            value = max(nums) if parts[0] == "max" else min(nums)
            print(len(arr) - 1 - arr[::-1].index(value))

    elif parts[0] in ["first", "last"]:
        count = int(parts[1])
        parity = parts[2]

        if count > len(arr):
            print("Invalid count")
            continue

        nums = [x for x in arr if x % 2 == 0] if parity == "even" else [x for x in arr if x % 2 != 0]

        if parts[0] == "first":
            print(nums[:count])
        else:
            print(nums[-count:])

print(arr)