# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:33:20 2026

@author: melia
"""

#%% 1. Train

wagons = list(map(int, input().split()))
capacity = int(input())

while True:
    command = input()
    if command == "end":
        break

    parts = command.split()
    if parts[0] == "Add":
        wagons.append(int(parts[1]))
    else:
        passengers = int(parts[0])
        for i in range(len(wagons)):
            if wagons[i] + passengers <= capacity:
                wagons[i] += passengers
                break

print(*wagons)

#%% 2. Change List

numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    parts = command.split()
    action = parts[0]

    if action == "Delete":
        element = int(parts[1])
        numbers = [x for x in numbers if x != element]

    elif action == "Insert":
        element = int(parts[1])
        position = int(parts[2])
        numbers.insert(position, element)

print(*numbers)

#%% 3. House Party

n = int(input())
guests = []

for _ in range(n):
    command = input().split()
    name = command[0]

    if "going" in command:
        if name in guests:
            print(f"{name} is already in the list!")
        else:
            guests.append(name)
    else:
        if name in guests:
            guests.remove(name)
        else:
            print(f"{name} is not in the list!")

for g in guests:
    print(g)
    
#%% 4. List Operations

numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break

    parts = command.split()
    action = parts[0]

    if action == "Add":
        numbers.append(int(parts[1]))

    elif action == "Insert":
        num = int(parts[1])
        idx = int(parts[2])
        if 0 <= idx < len(numbers):
            numbers.insert(idx, num)
        else:
            print("Invalid index")

    elif action == "Remove":
        idx = int(parts[1])
        if 0 <= idx < len(numbers):
            numbers.pop(idx)
        else:
            print("Invalid index")

    elif action == "Shift":
        direction = parts[1]
        count = int(parts[2]) % len(numbers)

        if direction == "left":
            numbers = numbers[count:] + numbers[:count]
        else:
            numbers = numbers[-count:] + numbers[:-count]

print(*numbers)
    
#%% 5. Bomb Numbers

numbers = list(map(int, input().split()))
bomb, power = map(int, input().split())

while bomb in numbers:
    idx = numbers.index(bomb)
    left = max(0, idx - power)
    right = min(len(numbers) - 1, idx + power)
    del numbers[left:right + 1]

print(sum(numbers))

#%% 6. Cards Game

first = list(map(int, input().split()))
second = list(map(int, input().split()))

while first and second:
    a = first.pop(0)
    b = second.pop(0)

    if a > b:
        first.append(a)
        first.append(b)
    elif b > a:
        second.append(b)
        second.append(a)

if first:
    print(f"First player wins! Sum: {sum(first)}")
else:
    print(f"Second player wins! Sum: {sum(second)}")
    
#%% 7. Append Arrays

parts = input().split("|")
result = []

for arr in reversed(parts):
    nums = arr.split()
    result.extend(nums)

print(*result)
    
#%% 8. Anonymous Threat

data = input().split()

while True:
    command = input()
    if command == "3:1":
        break

    parts = command.split()
    action = parts[0]

    if action == "merge":
        start = max(0, int(parts[1]))
        end = min(len(data) - 1, int(parts[2]))
        merged = "".join(data[start:end + 1])
        data[start:end + 1] = [merged]

    elif action == "divide":
        idx = int(parts[1])
        partitions = int(parts[2])
        word = data[idx]
        length = len(word)
        part_len = length // partitions
        new_parts = []

        for i in range(partitions - 1):
            new_parts.append(word[i * part_len:(i + 1) * part_len])
        new_parts.append(word[(partitions - 1) * part_len:])

        data[idx:idx + 1] = new_parts

print(*data)
    
#%% 9. Pokemon Don't Go

numbers = list(map(int, input().split()))
removed_sum = 0

while numbers:
    idx = int(input())

    if idx < 0:
        removed = numbers.pop(0)
        numbers.insert(0, numbers[-1])
    elif idx >= len(numbers):
        removed = numbers.pop(-1)
        numbers.append(numbers[0])
    else:
        removed = numbers.pop(idx)

    removed_sum += removed

    for i in range(len(numbers)):
        if numbers[i] <= removed:
            numbers[i] += removed
        else:
            numbers[i] -= removed

print(removed_sum)

#%% 10. SoftUni Course Planning

schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    parts = command.split(":")
    action = parts[0]

    if action == "Add":
        lesson = parts[1].strip()
        if lesson not in schedule:
            schedule.append(lesson)

    elif action == "Insert":
        lesson = parts[1].strip()
        index = int(parts[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif action == "Remove":
        lesson = parts[1].strip()
        if lesson in schedule:
            schedule.remove(lesson)
        if f"{lesson}-Exercise" in schedule:
            schedule.remove(f"{lesson}-Exercise")

    elif action == "Swap":
        l1 = parts[1].strip()
        l2 = parts[2].strip()
        if l1 in schedule and l2 in schedule:
            i1, i2 = schedule.index(l1), schedule.index(l2)
            schedule[i1], schedule[i2] = schedule[i2], schedule[i1]

            # Move exercises if needed
            if f"{l1}-Exercise" in schedule:
                schedule.remove(f"{l1}-Exercise")
                schedule.insert(schedule.index(l1) + 1, f"{l1}-Exercise")

            if f"{l2}-Exercise" in schedule:
                schedule.remove(f"{l2}-Exercise")
                schedule.insert(schedule.index(l2) + 1, f"{l2}-Exercise")

    elif action == "Exercise":
        lesson = parts[1].strip()
        exercise = f"{lesson}-Exercise"

        if lesson in schedule:
            if exercise not in schedule:
                schedule.insert(schedule.index(lesson) + 1, exercise)
        else:
            schedule.append(lesson)
            schedule.append(exercise)

for i, lesson in enumerate(schedule, 1):
    print(f"{i}. {lesson}")