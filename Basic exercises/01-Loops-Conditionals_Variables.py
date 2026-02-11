# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 19:01:45 2026

@author: melia
"""

#%% 1. Ages

n = int(input("How old is the person ? "))

if n>=0 and n <=2:
    print("Baby")
elif n>=3 and n<= 13:
    print("Child")
elif n>=14 and n <= 19:
    print("Teenager")
elif n>=20 and n<=65:
    print("Adut")
elif n>=66:
    print("Elder")
else:
    print("Age not valid")
    
#%% 2. Division

n = int(input("What is the number ? "))

divisible_by = 0

if n % 10 == 0:
    divisible_by = 10
elif n % 7 == 0:
    divisible_by = 7
elif n % 6 == 0:
    divisible_by = 6
elif n % 3 == 0:
    divisible_by = 3
elif n % 2 == 0:
    divisible_by = 2

if divisible_by == 0:
    print("Not divisible")
else:
    print(f"The number is divisible by {divisible_by}")

#%% 3. Vacation

people = int(input("How many people ? "))
group_type = input("Type of the group ? (Students/Business/Regular) ")
day = input("Day of the week ? (Friday/Saturday/Sunday) ")

prices = {
    "Friday":    {"Students": 8.45, "Business": 10.90, "Regular": 15},
    "Saturday":  {"Students": 9.80, "Business": 15.60, "Regular": 20},
    "Sunday":    {"Students": 10.46, "Business": 16,   "Regular": 22.50}
}

price_per_person = prices[day][group_type]
total_price = people * price_per_person

# Students discount
if group_type == "Students" and people >= 30:
    total_price *= 0.85   # -15%

# Business discount
if group_type == "Business" and people >= 100:
    total_price -= 10 * price_per_person   # 10 stay for free

# Regular discount
if group_type == "Regular" and 10 <= people <= 20:
    total_price *= 0.95   # -5%

print(f"Total price: {total_price:.2f}")

#%% 4. Print and Sum

start = int(input("Start ? "))
end = int(input("End ? "))

for i in range(start, end+1):
    print(f"{i}", end = " ")

print("", end = "\n")
s = 0    
for i in range(start, end+1):
    s+=i

print(f"Sum: {s}")

#%% 5. Login












