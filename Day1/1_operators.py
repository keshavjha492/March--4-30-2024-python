# Like in any other programming language python also has it's set of operators
# Operators are the mathematical and logical symbols to perform operations in a programming language

# Operators in python are:
# 1. Arithmetic Operators
# 2. Logical Operators
# 3. Relational Operators
# 4. Assignment Operators
# 5. Membership Operator
# 6. Identity Operator


# 1. Arithmetic Operators

# Addition(+)
a = 1  # a is a variable; = is an operator and 1 is a data of integer type
b = 2
print(a + b)  # print() is a python built-in function to view the results in a console  # 3

# Subtraction
a = 5
b = 3
print(a - b)  # 2


# Division (/)
b = 8
a = 2
print(b / a)  # 4  =>'/' operator gives quotient of the division


# Multiplication (*)
a = 2
b = 3
print(a * b)  # 6


# Exponent (**)
a = 4
print(a ** 2)  # 16

# Floor Division (//)
a = 10
b = 3
print(a // b)  # 3


# Modulus Operator (%)
a = 10
b = 3
print(a % b)  # % gives remainder of the division, 1


# 2. Logical Operators
# and, or, not are the logical operators
# Let's see the truth of each logical operators
# "and", "or" and "not" are the operators itself

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False


print(False or False)  # False
print(True or False)  # True
print(False or True)  # True
print(True or True)  # True

print(not False)  # True
print(not True)  # False


# Relational Operators
# >, <, >=, <=, !=, == are the relational operators
# Result of relational operations is boolean (True / False)

print(5 > 2)  # True
print(2 > 9)  # False
print(2 < 9)  # True

print(3 >= 3)  # True
print(4 != 2)  # True
print(4 != 4)  # False
print(5 == 5)  # True


# Assignment Operators
# =, +=, -=, *= are the assignment operators

a = 1
a = a + 1
print(a)  # 2

a += 1
print(a)  # 3

a -= 1
print(a)  # 2


# Membership Operator
# 'in' and "not in" are the membership operators
# result of membership operation is in boolean (True/False)
# Checks whether an element is a member of iterable
# Iterable means sequence of data. list, tuple etc. are the iterables in python

vowels = ["a", "e", "i", "o", "u"]
print("b" in vowels)  # False
print("b" not in vowels)  # True

print("e" in vowels)  # True
print("a" not in vowels)  # False


# Identity Operators
# 'is' and 'is not' are the identity operators
# They check whether two identities are the same object or not
a = 1
b = 1
print(a is b)  # True
print(a is not b)  # False

a = []
b = []
print(a is b)  # Both are not same object. False
print(a is not b)  # True