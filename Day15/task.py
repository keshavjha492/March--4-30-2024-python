
# Create a class Person with instance attributes name and age. Create a method get_details in this class to print name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

person = Person("abc", 30)
person.get_details()



# Create another class Employee with attributes salary and designation and inherits the Person class. Create a method get_details in this class to print name, age, salary and designation of the Employee
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        super().get_details()
        print("Salary:", self.salary)
        print("Designation:", self.designation)

employee = Employee("abc", 35, 50000, "Software Engineer")
employee.get_details()