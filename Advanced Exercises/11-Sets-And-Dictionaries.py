# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:12:58 2026

@author: melia
"""

#%% 1. Unique Usernames

n = int(input())
seen = []
for _ in range(n):
    username = input()
    if username not in seen:
        seen.append(username)
for u in seen:
    print(u)


#%% 2. Sets of Elements

n, m = map(int, input().split())
set_n = []
for _ in range(n):
    set_n.append(input().strip())
set_m = set()
for _ in range(m):
    set_m.add(input().strip())
for el in set_n:
    if el in set_m:
        print(el, end=" ")


#%% 3. Periodic Table

n = int(input())
elements = set()
for _ in range(n):
    for el in input().split():
        elements.add(el)
print(*sorted(elements))


#%% 4. Even Times

n = int(input())
counts = {}
for _ in range(n):
    num = int(input())
    counts[num] = counts.get(num, 0) + 1
for num, count in counts.items():
    if count % 2 == 0:
        print(num)


#%% 5. Count Symbols

text = input()
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
for ch in sorted(counts):
    print(f"{ch}: {counts[ch]} time/s")


#%% 6. Wardrobe

n = int(input())
wardrobe = {}
order = []
for _ in range(n):
    line = input()
    color, items_str = line.split(" -> ")
    items = items_str.split(",")
    if color not in wardrobe:
        wardrobe[color] = {}
        order.append(color)
    for item in items:
        wardrobe[color][item] = wardrobe[color].get(item, 0) + 1

search_color, search_item = input().split()

for color in order:
    print(f"{color} clothes:")
    for item, count in wardrobe[color].items():
        if color == search_color and item == search_item:
            print(f"* {item} - {count} (found!)")
        else:
            print(f"* {item} - {count}")


#%% 7. The V-Logger

vloggers = {}   # name -> set of people they follow
followers = {}  # name -> set of followers

for line in iter(input, "Statistics"):
    parts = line.split()
    if parts[1] == "joined":
        name = parts[0]
        if name not in vloggers:
            vloggers[name] = set()
            followers[name] = set()
    elif parts[1] == "followed":
        follower, followee = parts[0], parts[2]
        if follower in vloggers and followee in vloggers:
            if follower != followee and followee not in vloggers[follower]:
                vloggers[follower].add(followee)
                followers[followee].add(follower)

print(f"The V-Logger has a total of {len(vloggers)} vloggers in its logs.")

sorted_vloggers = sorted(
    vloggers.keys(),
    key=lambda v: (-len(followers[v]), len(vloggers[v]))
)

for i, name in enumerate(sorted_vloggers, 1):
    following_count = len(vloggers[name])
    follower_count = len(followers[name])
    print(f"{i}. {name} : {follower_count} followers, {following_count} following")
    if i == 1:
        for f in sorted(followers[name]):
            print(f"* {f}")


#%% 8. Ranking

contests = {}
for line in iter(input, "end of contests"):
    contest, password = line.split(":")
    contests[contest] = password

users = {}  # username -> {contest: points}
for line in iter(input, "end of submissions"):
    parts = line.split("=>")
    contest, password, username, points = parts[0], parts[1], parts[2], int(parts[3])
    if contest not in contests or contests[contest] != password:
        continue
    if username not in users:
        users[username] = {}
    if contest not in users[username] or users[username][contest] < points:
        users[username][contest] = points

best_user = max(users, key=lambda u: sum(users[u].values()))
best_points = sum(users[best_user].values())
print(f"Best candidate is {best_user} with total {best_points} points.")
print("Ranking:")
for username in sorted(users):
    print(username)
    for contest, pts in sorted(users[username].items(), key=lambda x: -x[1]):
        print(f"# {contest} -> {pts}")