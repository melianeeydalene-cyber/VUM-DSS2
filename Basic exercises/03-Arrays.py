# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:29:12 2026

@author: melia
"""

#%% 1. Train

n = int(input())
wagons = []

for _ in range(n):
    wagons.append(int(input()))

print(*wagons)
print(sum(wagons))


#%% 2. Common Elements

arr1 = input().split()
arr2 = input().split()

for el in arr2:
    if el in arr1:
        print(el, end=" ")


#%% 3. Zig-Zag Arrays

n = int(input())

arr1 = []
arr2 = []

for i in range(n):
    a, b = input().split()
    if i % 2 == 0:
        arr1.append(a)
        arr2.append(b)
    else:
        arr1.append(b)
        arr2.append(a)

print(*arr1)
print(*arr2)


#%% 4. Array Rotation

arr = input().split()
rotations = int(input())

for _ in range(rotations):
    first = arr.pop(0)
    arr.append(first)

print(*arr)


#%% 5. Top Integers

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if all(arr[i] > x for x in arr[i+1:]):
        print(arr[i], end=" ")


#%% 6. Equal Sums

arr = list(map(int, input().split()))

for i in range(len(arr)):
    left = sum(arr[:i])
    right = sum(arr[i+1:])

    if left == right:
        print(i)
        break
else:
    print("no")


#%% 7. Max Sequence of Equal Elements

arr = input().split()

best_seq = []
current_seq = [arr[0]]

for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        current_seq.append(arr[i])
    else:
        if len(current_seq) > len(best_seq):
            best_seq = current_seq
        current_seq = [arr[i]]

if len(current_seq) > len(best_seq):
    best_seq = current_seq

print(*best_seq)


#%% 8. Magic Sum

arr = list(map(int, input().split()))
target = int(input())

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])


#%% 9. Kamino Factory

n = int(input())

best_seq = []
best_sum = 0
best_index = 0
sample = 0

while True:
    line = input()
    if line == "Clone them!":
        break

    sample += 1
    seq = list(map(int, line.replace('!', ' ').split()))

    max_len = 0
    current_len = 0
    start_index = 0
    best_local_index = 0

    for i in range(len(seq)):
        if seq[i] == 1:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
                best_local_index = i - current_len + 1
        else:
            current_len = 0

    total = sum(seq)

    if (max_len > len(best_seq) or
       (max_len == len(best_seq) and best_local_index < best_index) or
       (max_len == len(best_seq) and best_local_index == best_index and total > best_sum)):

        best_seq = seq
        best_sum = total
        best_index = best_local_index
        best_sample = sample

print(f"Best DNA sample {best_sample} with sum: {best_sum}.")
print(*best_seq)


#%% 10. LadyBugs

size = int(input())
field = [0] * size

indexes = list(map(int, input().split()))

for i in indexes:
    if 0 <= i < size:
        field[i] = 1

while True:
    command = input()
    if command == "end":
        break

    i, direction, fly = command.split()
    i = int(i)
    fly = int(fly)

    if i < 0 or i >= size or field[i] == 0:
        continue

    field[i] = 0

    while True:
        if direction == "right":
            i += fly
        else:
            i -= fly

        if i < 0 or i >= size:
            break

        if field[i] == 0:
            field[i] = 1
            break

print(*field)