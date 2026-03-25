# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:04:28 2026

@author: melia
"""

#%% 1. Reverse Numbers with a Stack

nums = input().split()
stack = []
for n in nums:
    stack.append(n)
print(" ".join(stack[::-1]))


#%% 2. Basic Stack Operations

n, s, x = map(int, input().split())
nums = list(map(int, input().split()))
stack = nums[:n]
for _ in range(s):
    if stack:
        stack.pop()
if not stack:
    print(0)
elif x in stack:
    print("true")
else:
    print(min(stack))


#%% 3. Maximum Element

n = int(input())
stack = []
max_stack = []
for _ in range(n):
    line = input().split()
    if line[0] == '1':
        val = int(line[1])
        stack.append(val)
        max_stack.append(max(max_stack[-1], val) if max_stack else val)
    elif line[0] == '2':
        stack.pop()
        max_stack.pop()
    elif line[0] == '3':
        print(max_stack[-1])


#%% 4. Basic Queue Operations

from collections import deque
n, s, x = map(int, input().split())
nums = list(map(int, input().split()))
queue = deque(nums[:n])
for _ in range(s):
    if queue:
        queue.popleft()
if not queue:
    print(0)
elif x in queue:
    print("true")
else:
    print(min(queue))


#%% 5. Calculate Sequence with Queue

from collections import deque
n = int(input())
queue = deque()
queue.append(n)
result = []
while len(result) < 50:
    val = queue.popleft()
    result.append(val)
    queue.append(val + 1)
    queue.append(2 * val + 1)
    queue.append(val + 2)
print(*result[:50])


#%% 6. Truck Tour

n = int(input())
pumps = []
for _ in range(n):
    petrol, dist = map(int, input().split())
    pumps.append((petrol, dist))

start = 0
while start < n:
    tank = 0
    ok = True
    for i in range(n):
        idx = (start + i) % n
        tank += pumps[idx][0] - pumps[idx][1]
        if tank < 0:
            ok = False
            break
    if ok:
        print(start)
        break
    start += 1


#%% 7. Balanced Parentheses

s = input()
stack = []
pairs = {')': '(', ']': '[', '}': '{'}
balanced = True
for ch in s:
    if ch in '([{':
        stack.append(ch)
    elif ch in ')]}':
        if not stack or stack[-1] != pairs[ch]:
            balanced = False
            break
        stack.pop()
print("YES" if balanced and not stack else "NO")


#%% 8. Stack Fibonacci

n = int(input())
stack = [0, 1]
while len(stack) < n:
    stack.append(stack[-1] + stack[-2])
print(stack[n - 1])


#%% 9. Simple Text Editor

n = int(input())
text = ""
history = []
for _ in range(n):
    line = input().split(" ", 1)
    cmd = line[0]
    if cmd == "1":
        history.append(text)
        text += line[1]
    elif cmd == "2":
        history.append(text)
        text = text[:-int(line[1])]
    elif cmd == "3":
        print(text[int(line[1]) - 1])
    elif cmd == "4":
        text = history.pop()


#%% 10. Poisonous Plants

n = int(input())
plants = list(map(int, input().split()))
days = 0
while True:
    to_remove = set()
    for i in range(1, len(plants)):
        if plants[i] > plants[i - 1]:
            to_remove.add(i)
    if not to_remove:
        break
    plants = [p for i, p in enumerate(plants) if i not in to_remove]
    days += 1
print(days)