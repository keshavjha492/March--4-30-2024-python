# OOP stands for Object Oriented Programming
# It is a programming paradigm in which problems are solved with the concept of objects
# Class is the blueprint of objects
# Objects are the instantiation of a class

# "class" keyword is used to make a class in Python

# The four major pillars of OOP are:
# 1. Inheritance
# 2. Encapsulation
# 3. Polymorphism
# 4. Abstraction


# We can either define properties or methods inside a class. Both of them can be called as attributes.

class Vehicle:
    engine_type = "petrol"  # property / attribute (Class Attribute)

    def __init__(self, doors, color):  # constructor
        self.doors = doors  # instance attribute
        self.color = color  # instance attribute

    # method / instance attribute method
    def get_info(self):
        return f"The vehicle has {self.doors} doors. It has {self.color} color and engine type {self.engine_type}"


v1 = Vehicle(4, "red")  # vehicle object
# We can access attributes of the class using dot operator with object
print(v1.engine_type)  # petrol
print(v1.color)  # red
print(v1.doors)  # 4
print(v1.get_info())

v1.engine_type = "diesel"
print(Vehicle.engine_type)  # petrol
print(v1.engine_type)  # diesel

v1.color = "Yellow"
print(v1.color)  # Yellow

v2 = Vehicle(2, "green")
print(v2.engine_type)  # petrol
print(v2.color)  # green
print(v2.doors)  # 2
print(v2.get_info())