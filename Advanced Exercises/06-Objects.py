# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:48:07 2026

@author: melia
"""

#%% 1. Advertisement Message

import random

phrases = ["Excellent product.", "Such a great product.", "I always use that product.",
           "Best product of its category.", "Exceptional product.", "I can't live without this product."]
events = ["Now I feel good.", "I have succeeded with this product.",
          "Makes miracles. I am happy of the results!", "I cannot believe but now I feel awesome.",
          "Try it yourself, I am very satisfied.", "I feel great!"]
authors = ["Diana", "Petya", "Stella", "Elena", "Katya", "Iva", "Annie", "Eva"]
cities = ["Burgas", "Sofia", "Plovdiv", "Varna", "Ruse"]

n = int(input())
for _ in range(n):
    print(f"{random.choice(phrases)} {random.choice(events)} {random.choice(authors)} – {random.choice(cities)}.")


#%% 2. Articles

class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content):
        self.content = new_content

    def change_author(self, new_author):
        self.author = new_author

    def rename(self, new_title):
        self.title = new_title

    def __str__(self):
        return f"{self.title} - {self.content}: {self.author}"

title, content, author = input().split(", ")
article = Article(title, content, author)

n = int(input())
for _ in range(n):
    command, value = input().split(": ", 1)
    if command == "Edit":
        article.edit(value)
    elif command == "ChangeAuthor":
        article.change_author(value)
    elif command == "Rename":
        article.rename(value)

print(article)

#%% 3. Articles 2.0

class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} - {self.content}: {self.author}"

n = int(input())
articles = []
for _ in range(n):
    title, content, author = input().split(", ")
    articles.append(Article(title, content, author))

for article in articles:
    print(article)


#%% 4. Students

class Student:
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = float(grade)

n = int(input())
students = []
for _ in range(n):
    parts = input().split()
    students.append(Student(parts[0], parts[1], parts[2]))

students.sort(key=lambda s: s.grade, reverse=True)
for s in students:
    print(f"{s.first_name} {s.last_name}: {s.grade:.2f}")

#%% 5. Teamwork Projects

n = int(input())
teams = {}       # teamName -> creator
members = {}     # teamName -> [members]
user_teams = {}  # user -> teamName (tracks which team a user belongs to)

for _ in range(n):
    line = input()
    user, team_name = line.split("-")
    if team_name in teams:
        print(f"Team {team_name} was already created!")
    elif user in user_teams:
        print(f"{user} cannot create another team!")
    else:
        teams[team_name] = user
        members[team_name] = []
        user_teams[user] = team_name
        print(f"Team {team_name} has been created by {user}!")

line = input()
while line != "end of assignment":
    user, team_name = line.split("->")
    if team_name not in teams:
        print(f"Team {team_name} does not exist!")
    elif user in user_teams:
        print(f"Member {user} cannot join team {team_name}!")
    else:
        members[team_name].append(user)
        user_teams[user] = team_name
    line = input()

# Print valid teams (with members), sorted by member count desc then name asc
valid = {t: m for t, m in members.items() if len(m) > 0}
for team_name in sorted(valid, key=lambda t: (-len(members[t]), t)):
    print(team_name)
    print(f"- {teams[team_name]}")
    print("--")
    for member in sorted(members[team_name]):
        print(member)

# Print disbanded teams
disbanded = [t for t, m in members.items() if len(m) == 0]
if disbanded:
    print("Teams to disband:")
    for t in sorted(disbanded):
        print(t)

#%% 6. Vehicle Catalogue

class Vehicle:
    def __init__(self, v_type, model, color, horsepower):
        self.v_type = v_type.lower()
        self.model = model
        self.color = color
        self.horsepower = int(horsepower)

    def __str__(self):
        return (f"Type: {self.v_type.capitalize()}\n"
                f"Model: {self.model}\n"
                f"Color: {self.color}\n"
                f"Horsepower: {self.horsepower}")

catalogue = {}
line = input()
while line != "End":
    v_type, model, color, hp = line.split()
    catalogue[model] = Vehicle(v_type, model, color, hp)
    line = input()

line = input()
while line != "Close the Catalogue":
    print(catalogue[line])
    line = input()

cars = [v for v in catalogue.values() if v.v_type == "car"]
trucks = [v for v in catalogue.values() if v.v_type == "truck"]

car_avg = sum(v.horsepower for v in cars) / len(cars) if cars else 0
truck_avg = sum(v.horsepower for v in trucks) / len(trucks) if trucks else 0

print(f"Cars have average horsepower of: {car_avg:.2f}.")
print(f"Trucks have average horsepower of: {truck_avg:.2f}.")


#%% 7. Order by Age

class Person:
    def __init__(self, name, person_id, age):
        self.name = name
        self.person_id = person_id
        self.age = int(age)

people = {}
line = input()
while line != "End":
    name, person_id, age = line.split()
    people[person_id] = Person(name, person_id, age)
    line = input()

for p in sorted(people.values(), key=lambda x: x.age):
    print(f"{p.name} with ID: {p.person_id} is {p.age} years old.")