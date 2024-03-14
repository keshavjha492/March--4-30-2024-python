# Dictionary is a mutable datatype in Python
# They are the key-value pairs enclosed withing curly braces


# Creating an empty dictionary
a = {}
b = dict()


# Creating non-empty dictionary
student = {"name": "Jon", "age": 30, "address": "KTM", "last name": "Brown"}
print(student)

student = dict(name="Jon", age=30, address="KTM")
print(student)


# Rule for dictionary keys and values
# 1. Values of a dictionary can be of any datatype.
# 2. Keys of a dictionary must be an immutable datatype

d = {"": 12}
print(d)  #

# d = {"messg": "Hello", [1, 2]: 12}  # Invalid dictionary
d = {"messg": "Hello", (1, 2): 12}  # Valid dictionary
# d = {"messg": "Hello", (1, [2, 3]): 12}  # InValid dictionary

e = {1: "Hello", 2: "World"}  # Valid


# Accessing dictionary Values
student = {"name": "Jon", "age": 30, "address": "KTM", "last name": "Brown"}
a1 = [1, 2, 3]
print(a1[1])  # 2
# print(a1[10])  # IndexError

print(student["address"])  # "KTM"
print(student["last name"])  # "Brown"

d = {"": 12}
print(d[""])  # 12

d = {"messg": "Hello", (1, 2): 12}
print(d[(1, 2)])  # 12
e = {1: "Hello", 2: "World"}
print(e[2])  # World


student = {"name": "Jon", "age": 30, "address": "KTM", "last name": "Brown"}
print(student["roll"])  # KeyError
print(student["last name"])


# .get() method
name = student.get("name")
print(name)  # Jon

roll = student.get("roll")
print(roll)  # None


# Updating dictionary elements
student = {"name": "Jon", "age": 30, "address": "KTM", "last name": "Brown"}
student["roll"] = 30

print(student)  # {"name": "Jon", "age": 30, "address": "KTM", "last name": "Brown", "roll": 30}

student["name"] = "Jane"
print(student)  # {"name": "Jane", "age": 30, "address": "KTM", "last name": "Brown", "roll": 30}


# update() method
student = {"name": "Jon", "age": 20}

student.update({"roll": 30, "address": "KTM"})
print(student)  # {"name": "Jon", "age": 20, "roll": 30, "address": "KTM"}

student.update(email="jon@email.com", classroom=2)
print(student)  # {"name": "Jon", "age": 20, "roll": 30, "address": "KTM", "email: "jon@email.com", "classroom": 2}