# Task 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def add_radius(self, other):
        return self.radius + other.radius

    def __add__(self, other):
        return self.radius + other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    def __lt(self,other):
        return self.radius < other.radius


c1 = Circle(1)
c2 = Circle(2)

print(c1.add_radius(c2))  


print(c1 + c2)

if c1 > c2:
    print(f"{c1} is larger than {c2}")
elif c1 < c2:
    print(f"{c1} is smaller than {c2}")
else:
    print(f"{c1} and {c2} are the same size")


# Task 2
class Department:
    def __init__(self, name, number_of_students):
        self.name = name
        self.number_of_students = number_of_students

    def total_students(self, departments):
        total = 0
        for department in departments:
            total += department.number_of_students
        return total


dept1 = Department("CS", 100)
dept2 = Department("Math", 80)
dept3 = Department("Physics", 70)
dept4 = Department("chemistry", 50)

departments = [dept1, dept2, dept3,dept4]


total_students = dept1.total_students(departments)
print(f"Total number of students in all departments: {total_students}")