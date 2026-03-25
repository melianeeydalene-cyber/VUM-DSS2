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

username = input("What is the username ? ")

password = username[::-1]

word = input("What is the password ? ")
while word!=password :
    print("Incorrect password. Try again. ")
    word = input("What is the password ? ")
    
print(f"User {username} logged in.")

#%% 6. Strong Number

def fact(n):
    if n ==0:
        return 1
    return n*fact(n-1)

N = int(input("What is the number ? "))

sum_fact = 0

for digit in str(N):
    sum_fact += fact(int(digit))
    
if sum_fact == N:
    print("Yes")
else:
    print("No")

#%% 7. Vending Machine 

"""coins = [0.1, 0.2, 0.5, 1, 2]

money = 0

command = input()
while command != "Start":
    coin = float(command)
    if coin not in coins:
        print(f"Cannot accept {coin}")
    else:
        money += coin
    command = input()

products = {"Nuts": 2.0, "Water": 0.7, "Crisps": 1.5, "Soda": 0.8, "Coke": 1.0}

command = input()
while command != "End":
    prod = command
    if prod not in products:
        print("Invalid product")
    else:
        price = products[prod]
        if price <= money:
            money -= price
            print(f"Purchased {prod}")
        else:
            print("Sorry, not enough money")
    command = input()

print(f"Change: {money:.2f}")"""
    
#this code didn't work, it was overlapping so i tried something else :
    
valid_coins = [0.1, 0.2, 0.5, 1, 2]

money = 0

while True:
    command = input()

    if command == "Start":
        break

    coin = float(command)

    if coin in valid_coins:
        money += coin
    else:
        print(f"Cannot accept {coin}")

products = {
    "Nuts": 2.0,
    "Water": 0.7,
    "Crisps": 1.5,
    "Soda": 0.8,
    "Coke": 1.0
}

while True:
    command = input()

    if command == "End":
        break

    if command not in products:
        print("Invalid product")
        continue

    price = products[command]

    if money >= price:
        money -= price
        print(f"Purchased {command.lower()}")
    else:
        print("Sorry, not enough money")


print(f"Change: {money:.2f}")

#%% 8. Triangle of Numbers

n = int(input())

for i in range(1, n + 1):
    print((" ".join([str(i)] * i)))

#%% 9. Padawan Equipment

money = float(input())
students = int(input())
price_saber = float(input())
price_robe = float(input())
price_belt = float(input())

sabers_needed = int(students * 1.1 + 0.999999)  # arrondi vers le haut
free_belts = students // 6

total = (
    sabers_needed * price_saber +
    students * price_robe +
    (students - free_belts) * price_belt
)

if total <= money:
    print(f"The money is enough - it would cost {total:.2f}lv.")
else:
    print(f"John will need {total - money:.2f}lv more.")

#%% 10. Rage Expenses

lost_games = int(input())
price_headset = float(input())
price_mouse = float(input())
price_keyboard = float(input())
price_display = float(input())

headset = mouse = keyboard = display = 0
keyboard_trash_count = 0

for game in range(1, lost_games + 1):
    if game % 2 == 0:
        headset += 1
    if game % 3 == 0:
        mouse += 1
    if game % 2 == 0 and game % 3 == 0:
        keyboard += 1
        keyboard_trash_count += 1
        if keyboard_trash_count % 2 == 0:
            display += 1

total = (
    headset * price_headset +
    mouse * price_mouse +
    keyboard * price_keyboard +
    display * price_display
)

print(f"Rage expenses: {total:.2f} lv.")

#%% 11. Orders

orders = int(input())
total_price = 0

for _ in range(orders):
    price = float(input())
    days = int(input())
    capsules = int(input())

    order_price = price * days * capsules
    total_price += order_price

    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total_price:.2f}")







