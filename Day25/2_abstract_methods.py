# If we can't make an object of a class then such a class is called abstract class

# abstract methods are those methods which must be implemented on the inherited class declaration

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Barks !!")

    def details(self):
        print("This is dog")

class Cat(Animal):
    def sound(self):
        print("Meow")


d = Dog()
d.sound()
c = Cat()
c.sound()