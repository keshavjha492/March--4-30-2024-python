# Inheritance is the process of accessing the properties of the parent class by a child class
# Types of inheritance in python

# 1. Single Inheritance
# 2. Multiple
# 3. Multilevel
# 4. Hierarchical
# 5. Hybrid


class A:
    x = 1


class B(A):
    y = 2


obj = B()
print(obj.x)  # 1
print(obj.y)  # 2


# Multiple
class A:
    x = 1

class B:
    y = 2

class C(A, B):  # Multiple inheritance
    z = 3

obj = C()
print(obj.x)  # 1
print(obj.y)  # 2
print(obj.z)  # 3


# Multilevel Inheritance
class A:
    x = 1

class B(A):
    y = 2

class C(B):
    z = 3


# Hierarchical
class A:
    x = 1

class B(A):
    y = 2

class C(A):
    z = 3


# Hybrid Inheritance
class A:
    x = 1

class B(A):
    y = 2
    x = 10


class C(A):
    z = 3
    x = 20


class D(B, C):
    p = 10


class E(D):
    pass


obj = E()
print(obj.x)  # 12

# Order of accessing the attributes in inheritance is called MRO (Method resolution Order)
print(E.mro())

