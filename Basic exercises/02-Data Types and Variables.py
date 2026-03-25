# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 18:28:24 2026

@author: melia
"""

#%% 1.Integer Operations

a = int(input("First integer ? "))
b = int(input("Second integer ? "))
c = int(input("Third integer ? "))
d = int(input("Fourth integer ? "))

op = a+b
if c!=0:
    op =op/c
    op=op*d
print(op)

#%% 2. Sum Digits

a = input("What is the number ? ")
s = 0

for car in a:
    s += int(car)
    
print(s)

#%% 3. Elevator

n = int(input())
p = int(input())

courses = n // p
if n % p != 0:
    courses += 1

print(courses)


#%% 4. Sum of Chars

n = int(input())
total = 0

for _ in range(n):
    ch = input()
    total += ord(ch)

print(f"The sum equals: {total}")


#%% 5. Print Part of ASCII Table

start = int(input())
end = int(input())

for i in range(start, end + 1):
    print(chr(i), end=" ")


#%% 6. Triples of Latin Letters

n = int(input())

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(chr(97+i) + chr(97+j) + chr(97+k))


#%% 7. Water Overflow

n = int(input())
capacity = 255
water = 0

for _ in range(n):
    liters = int(input())
    if water + liters > capacity:
        print("Insufficient capacity!")
    else:
        water += liters

print(water)


#%% 8. Beer Kegs

import math

n = int(input())
max_volume = 0
best_model = ""

for _ in range(n):
    model = input()
    r = float(input())
    h = int(input())

    volume = math.pi * r**2 * h

    if volume > max_volume:
        max_volume = volume
        best_model = model

print(best_model)


#%% 9. Spice Must Flow

yield_spice = int(input())
total = 0
days = 0

while yield_spice >= 100:
    total += yield_spice
    total -= 26
    yield_spice -= 10
    days += 1

if total >= 26:
    total -= 26

print(days)
print(total)


#%% 10. Pokemon

N = int(input())
M = int(input())
Y = int(input())

original = N
count = 0

while N >= M:
    N -= M
    count += 1

    if N == original * 0.5 and Y != 0:
        N //= Y

print(N)
print(count)


#%% 11. Snowballs

n = int(input())

best_value = 0
best_data = ()

for _ in range(n):
    snow = int(input())
    time = int(input())
    quality = int(input())

    value = (snow // time) ** quality

    if value > best_value:
        best_value = value
        best_data = (snow, time, quality)

print(f"{best_data[0]} : {best_data[1]} = {best_value} ({best_data[2]})")