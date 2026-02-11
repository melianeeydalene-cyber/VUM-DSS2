# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 17:01:15 2026

@author: melia
"""

#%% Task 1

start = int(input("start = ? "))
end = int(input("end = ? "))

if start>end:
    stat, end = end, start
    
for i in range(start, end+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        
#%% Task 2 

N = int(input("How many numbers will be inserted ? "))

Num = [int(input("Number ?")) for i in range(N)]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None
        
    