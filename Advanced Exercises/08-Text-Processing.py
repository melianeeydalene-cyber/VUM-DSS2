# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:39:07 2026

@author: melia
"""

#%% 1. Valid Usernames

import re
usernames = input().split(", ")
for username in usernames:
    if 3 <= len(username) <= 16 and re.match(r'^[a-zA-Z0-9_-]+$', username):
        print(username)


#%% 2. Character Multiplier

str1 = input()
str2 = input()
total = 0
for i in range(max(len(str1), len(str2))):
    if i < len(str1) and i < len(str2):
        total += ord(str1[i]) * ord(str2[i])
    elif i < len(str1):
        total += ord(str1[i])
    else:
        total += ord(str2[i])
print(total)


#%% 3. Extract File

path = input()
filename = path.split("\\")[-1]
name, ext = filename.rsplit(".", 1)
print(f"File name: {name}")
print(f"File extension: {ext}")


#%% 4. Caesar Cipher

text = input()
print("".join(chr(ord(ch) + 3) for ch in text))


#%% 5. Multiply Big Number

big = input()
digit = int(input())
if digit == 0 or big == "0":
    print(0)
else:
    result = []
    carry = 0
    for ch in reversed(big):
        product = int(ch) * digit + carry
        carry = product // 10
        result.append(str(product % 10))
    while carry:
        result.append(str(carry % 10))
        carry //= 10
    print("".join(reversed(result)))


#%% 6. Replace Repeating Chars

text = input()
result = [text[0]]
for ch in text[1:]:
    if ch != result[-1]:
        result.append(ch)
print("".join(result))


#%% 7. String Explosion

text = input()
result = []
strength = 0
i = 0
while i < len(text):
    ch = text[i]
    if ch == '>':
        result.append(ch)
        i += 1
        if i < len(text):
            strength += int(text[i])
            i += 1
    elif strength > 0:
        strength -= 1
        i += 1
    else:
        result.append(ch)
        i += 1
print("".join(result))


#%% 8. Letters Change Numbers

import re
tokens = input().split()
total = 0.0
for token in tokens:
    left = token[0]
    right = token[-1]
    number = float(re.search(r'\d+', token).group())
    left_pos = ord(left.lower()) - ord('a') + 1
    if left.isupper():
        number /= left_pos
    else:
        number *= left_pos
    right_pos = ord(right.lower()) - ord('a') + 1
    if right.isupper():
        number -= right_pos
    else:
        number += right_pos
    total += number
print(f"{total:.2f}")