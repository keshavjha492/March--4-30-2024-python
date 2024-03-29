# Encapsulation is the process of data hiding in OOP concept
# Like in other languages, python also has the concept of private, public and protected attributes

# public are those attributes which are accessible both outside and inside the class
# protected are those attributes which are accessible inside the class and in child classes
# private are those attributes which are accessible only inside the main class
# (not in child classes or outside the class)


class Vehicle:
    def __init__(self, engine, doors, color):
        self.engine = engine  # public
        self._doors = doors  # protected
        self.__color = color  # private

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


vehicle = Vehicle("petrol", 4, "red")
print(vehicle.engine)  # petrol
print(vehicle._doors)  # 4 (not recommended)
# print(vehicle.__color)  # Private members can't be accessed

print(vehicle.get_color())  # red

vehicle.__color = "blue"
print(vehicle.get_color())

vehicle.set_color("blue")
print(vehicle.get_color())  # blue