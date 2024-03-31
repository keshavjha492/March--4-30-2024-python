# Create a Person class and set the age of the Person using a constructor
# But if birth year of the Person is passed then solve the problem using a factory method

from datetime import datetime


class Person:
    def __init__(self, age):
        self.age = age

    @classmethod
    def from_birth_year(cls, year):  # Factory Method
        age = datetime.now().year - year
        return cls(age)


p = Person(32)
print(p.age)  # 32


p2 = Person.from_birth_year(1990)
print(p2.age)  # 34