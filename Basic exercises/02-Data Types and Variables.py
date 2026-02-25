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

