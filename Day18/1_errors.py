# There are broadly two types of errors in any language
# 1. Syntactic Error
# 2. Non-syntactic Error

# The error raised when we mess up with the grammar of the language are syntax error
# a =
# if a:
# print("kndf")
#
# @a = 2


# Non-syntactic Error => Logical errors during Runtime
# 1. ValueError
# 2. TypeError
# 3. IndexError
# 4. KeyError
# 5. ZeroDivisionError
# 6. NameError
# 7. ModuleNotFoundError
# 8. AttributeError


# ValueError
a = int(input("Enter a number "))

# TypeError
a = 1
b = "hello"
print(a + b)  #

# IndexError
data = [1, 2, 3]
print(data[10])  # IndexError

# KeyError
student = {"name": "Jon", "age": 30}
print(student["address"])

address = student.get("address")
print(address)  # None

address = student.get("address", "KTM")
print(address)  # KTM

name = student.get("name", "Jane")
print(name)  # Jon


# ZeroDivisionError
print(3 / 0)

# NameError
a = 1
print(a + x)  # Name x is not defined


import zyx  # ModuleNotFoundError


# Attribute
class A:
    x = 10
    
    
obj = A()
print(obj.y)  # obj of class A has no attribute y. AttributeError

a = [1, 2, 3]
a.appendd(4)