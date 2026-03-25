# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:39:07 2026

@author: melia
"""

#%% 1. Count Chars in a String

text = input()
counts = {}
for ch in text:
    if ch != ' ':
        counts[ch] = counts.get(ch, 0) + 1
for ch, count in counts.items():
    print(f"{ch} -> {count}")


#%% 2. A Miner Task

resources = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    resources[resource] = resources.get(resource, 0) + quantity
for resource, qty in resources.items():
    print(f"{resource} -> {qty}")


#%% 3. Orders

products = {}
while True:
    line = input()
    if line == "buy":
        break
    name, price, qty = line.split()
    price, qty = float(price), int(qty)
    if name in products:
        products[name][0] = price
        products[name][1] += qty
    else:
        products[name] = [price, qty]
for name, (price, qty) in products.items():
    print(f"{name} -> {price * qty:.2f}")


#%% 4. SoftUni Parking

n = int(input())
parking = {}
for _ in range(n):
    parts = input().split()
    if parts[0] == "register":
        username, plate = parts[1], parts[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = plate
            print(f"{username} registered {plate} successfully")
    elif parts[0] == "unregister":
        username = parts[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")
for username, plate in parking.items():
    print(f"{username} => {plate}")


#%% 5. Courses

courses = {}
while True:
    line = input()
    if line == "end":
        break
    course, student = line.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(student)
for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")


#%% 6. Student Academy

n = int(input())
students = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    if avg >= 4.50:
        print(f"{name} -> {avg:.2f}")


#%% 7. Company Users

companies = {}
while True:
    line = input()
    if line == "End":
        break
    company, emp_id = line.split(" -> ")
    if company not in companies:
        companies[company] = []
    if emp_id not in companies[company]:
        companies[company].append(emp_id)
for company, employees in companies.items():
    print(company)
    for emp in employees:
        print(f"-- {emp}")