# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 15:24:42 2026

@author: melia
"""

# I adapted the exercises to Python while preserving the object-oriented 
# concepts from the original C# sheet, such as classes, abstraction, and 
# polymorphism. Since Python does not use interfaces in the same way as C#,
# I implemented the same logic using standard Python classes.

#%% 1. Define an Interface IPerson

class Citizen:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input()
age = int(input())

person = Citizen(name, age)

print(person.name)
print(person.age)

#%% 2. Multiple Implementation

class Citizen:
    def __init__(self, name, age, id, birthdate):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate

name = input()
age = int(input())
id = input()
birthdate = input()

citizen = Citizen(name, age, id, birthdate)

print(citizen.id)
print(citizen.birthdate)

#%% 3. Telephony

class Smartphone:
    def call(self, number):
        return f"Calling... {number}"

    def browse(self, site):
        return f"Browsing: {site}!"


class StationaryPhone:
    def call(self, number):
        return f"Dialing... {number}"


# I split the input into lists to process each element separately
numbers = input().split()
sites = input().split()

smartphone = Smartphone()
stationary = StationaryPhone()

for number in numbers:
    
    # Check if the number contains only digits
    if not number.isdigit():
        print("Invalid number!")
    
    # 10 digits → smartphone
    elif len(number) == 10:
        print(smartphone.call(number))
    
    # 7 digits → stationary phone
    elif len(number) == 7:
        print(stationary.call(number))


# Browsing
for site in sites:
    
    # If any character is a digit, the URL is invalid
    if any(char.isdigit() for char in site):
        print("Invalid URL!")
    else:
        print(smartphone.browse(site))
        
#%% 4. Border Control

class Citizen:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


class Robot:
    def __init__(self, model, id):
        self.model = model
        self.id = id


entities = []  # We store both Citizens and Robots in the same list

while True:
    line = input()
    if line == "End":
        break

    parts = line.split()

    # If there are 3 elements, it's a Citizen
    if len(parts) == 3:
        name, age, id = parts
        entities.append(Citizen(name, age, id))

    # If there are 2 elements, it's a Robot
    elif len(parts) == 2:
        model, id = parts
        entities.append(Robot(model, id))


fake_suffix = input()

# We loop through all entities without caring about their type
for entity in entities:
    if entity.id.endswith(fake_suffix):
        print(entity.id)
        
#%% 5. Birthday Celebrations

class Citizen:
    def __init__(self, name, age, id, birthdate):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate


class Pet:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate


entities = []

while True:
    line = input()
    if line == "End":
        break

    parts = line.split()

    if parts[0] == "Citizen":
        _, name, age, id, birthdate = parts
        entities.append(Citizen(name, age, id, birthdate))

    elif parts[0] == "Pet":
        _, name, birthdate = parts
        entities.append(Pet(name, birthdate))


year = input()

for entity in entities:
    if hasattr(entity, "birthdate") and entity.birthdate.endswith(year):
        print(entity.birthdate)
        
#%% 6. Food Shortage

class Citizen:
    def __init__(self, name, age, id, birthdate):
        self.name = name
        self.food = 0

    def buy_food(self):
        self.food += 10


class Rebel:
    def __init__(self, name, age, group):
        self.name = name
        self.food = 0

    def buy_food(self):
        self.food += 5


n = int(input())
people = {}

for _ in range(n):
    parts = input().split()

    if len(parts) == 4:
        name, age, id, birthdate = parts
        people[name] = Citizen(name, age, id, birthdate)

    elif len(parts) == 3:
        name, age, group = parts
        people[name] = Rebel(name, age, group)


while True:
    name = input()
    if name == "End":
        break

    if name in people:
        people[name].buy_food()


total_food = sum(person.food for person in people.values())
print(total_food)

#not yet finished