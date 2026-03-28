# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:16:48 2026

@author: melia
"""

#%% 1. Person

class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age must be positive!")
        # name mangled with __ to simulate private fields like C#
        self.__name = name
        self.__age = age

    # properties = C# getters
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def __str__(self):
        # __str__ is Python's equivalent of ToString() (I looked for it on the internet)
        # type(self).__name__ gives the actual class name (Child or Person)
        return f"{type(self).__name__} -> Name: {self.name}, Age: {self.age}"


class Child(Person):
    def __init__(self, name, age):
        if age > 15:
            raise ValueError("Child's age must be <= 15!")
        # super().__init__() = calling base class constructor, same as : base(name, age) in C#
        super().__init__(name, age)


name = input()
age = int(input())

if age < 0:
    print("Age must be positive!")
elif age > 15:
    print(Person(name, age))
else:
    print(Child(name, age))


#%% 2. Zoo

# here inheriting is done with class Child(Parent): instead of : Parent

class Animal:
    def __init__(self, name):
        self.name = name

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

class Lizard(Reptile):
    def __init__(self, name):
        super().__init__(name)

class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)

class Gorilla(Mammal):
    def __init__(self, name):
        super().__init__(name)

class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)


#%% 3. Players and Monsters

class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __str__(self):
        # type(self).__name__ returns the subclass name
        # so a SoulMaster object prints "Type: SoulMaster" automatically
        return f"Type: {type(self).__name__} Username: {self.username} Level: {self.level}"

# All subclasses just call super().__init__() 
class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)

class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)

class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)

class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)

class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)


#%% 4. Need for Speed

class Vehicle:
    # class-level constant, equivalent to a static field in C#
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, horse_power, fuel):
        self.horse_power = horse_power
        self.fuel = fuel
        # instance gets its own fuel_consumption so subclasses can override it
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        # equivalent of the virtual void Drive() in C#
        self.fuel -= kilometers * self.fuel_consumption


class Motorcycle(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, horse_power, fuel):
        super().__init__(horse_power, fuel)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, horse_power, fuel):
        super().__init__(horse_power, fuel)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, horse_power, fuel):
        super().__init__(horse_power, fuel)
        # overrides the parent's fuel_consumption after calling super()
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION


class CrossMotorcycle(Motorcycle):
    def __init__(self, horse_power, fuel):
        super().__init__(horse_power, fuel)


class FamilyCar(Car):
    def __init__(self, horse_power, fuel):
        super().__init__(horse_power, fuel)


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, horse_power, fuel):
        super().__init__(horse_power, fuel)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION


#%% 5. Restaurant

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        # tips : always call super().__init__() to avoid rewriting shared fields
        super().__init__(name, price)
        self.milliliters = milliliters


class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.grams = grams


class HotBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)


class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)


class Coffee(HotBeverage):
    # class-level defaults, like C# const fields (internet)
    COFFEE_MILLILITERS = 50
    COFFEE_PRICE = 3.50

    def __init__(self, caffeine):
        super().__init__("Coffee", self.COFFEE_PRICE, self.COFFEE_MILLILITERS)
        self.caffeine = caffeine


class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)


class MainDish(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)


class Dessert(Food):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        # Dessert adds one extra field on top of Food
        self.calories = calories


class Starter(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)


class Fish(MainDish):
    DEFAULT_GRAMS = 22

    def __init__(self, name, price):
        # Fish always weighs 22g — caller doesn't pass grams
        super().__init__(name, price, self.DEFAULT_GRAMS)


class Soup(Starter):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)


class Cake(Dessert):
    DEFAULT_GRAMS = 250
    DEFAULT_CALORIES = 1000
    CAKE_PRICE = 5

    def __init__(self):
        # Cake takes zero arguments
        super().__init__("Cake", self.CAKE_PRICE, self.DEFAULT_GRAMS, self.DEFAULT_CALORIES)


#%% 6. Animals

class Animal:
    def __init__(self, name, age, gender):
        if not name or age <= 0:
            raise ValueError("Invalid input!")
        self.name = name
        self.age = age
        self.gender = gender

    def produce_sound(self):
        # equivalent of an abstract method in C#, forces subclasses to implement it
        raise NotImplementedError

    def __str__(self):
        # calling self.produce_sound() here uses the subclass version automatically (polymorphism)
        return (f"{type(self).__name__}\n"
                f"{self.name} {self.age} {self.gender}\n"
                f"{self.produce_sound()}")


class Dog(Animal):
    def produce_sound(self):
        return "Woof!"


class Cat(Animal):
    def produce_sound(self):
        return "Meow meow"


class Frog(Animal):
    def produce_sound(self):
        return "Ribbit"


class Kitten(Cat):
    def __init__(self, name, age, gender=None):
        # gender is ignored, Kittens are always Female
        super().__init__(name, age, "Female")

    def produce_sound(self):
        return "Meow"


class Tomcat(Cat):
    def __init__(self, name, age, gender=None):
        # same idea, Tomcats are always Male
        super().__init__(name, age, "Male")

    def produce_sound(self):
        return "MEOW"


# dict maps string input to class — cleaner than a big if/elif chain
ANIMAL_TYPES = {
    "Dog": Dog, "Cat": Cat, "Frog": Frog,
    "Kitten": Kitten, "Tomcat": Tomcat
}

animals = []
while True:
    animal_type = input()
    if animal_type == "Beast!":
        break
    try:
        parts = input().split()
        name, age = parts[0], int(parts[1])
        gender = parts[2] if len(parts) > 2 else "Male"
        if age <= 0:
            raise ValueError("Invalid input!")
        animal = ANIMAL_TYPES[animal_type](name, age, gender)
        animals.append(animal)
    except (ValueError, KeyError):
        # KeyError catches unknown animal types, ValueError catches bad age
        print("Invalid input!")

for animal in animals:
    print(animal)