# Strings are the immutable datatypes in Python
# They are the sequence of characters enclosed inside single, double or triple quotes

# Creating an empty string
a = str()
# str() is a built-in function to create string in Python
print(a) # ""

a = ""
print(a)  # empty string

a = ''
print(a)  # empty string

a = """"""
print(a)  # empty

a = ''''''
print(a)  # a

print(bool(a))  # False

# Creating Non-empty strings
a = "Hello World"
b = 'Hello World'
c = """"
Hello World.
I am learning Python
"""
d = '''
Hello World.
I am learning Python
'''

print(bool(d))  # True


# Accessing string elements
# Accessing string elements are similar to accessing list elements i.e. Indexing and Slicing

# Indexing
# Forward indexing starts from 0 and reverse from -1
data = "Hello World. I am learning Python"

print(data[7])  # o
print(data[0])  # H
print(data[100])  # Error

print(data[-1])  # n
print(data[-7])  # " "
print(data[-10])  # i
print(data[-100])  # Error


# Slicing
data = "Hello World. I am learning Python"

print(data[3: 10])  # "lo Worl"
print(data[8:2])  # ""
print(data[:9])  # "Hello Wor"
print(data[7:])  # "orld. I am learning Python"
print(data[1:10:2])  # "el ol"

print(data[-10: -2])  # "ing Pyth"
print(data[-1: -9])  # ""
print(data[2: -3])  # "llo World. I am learning Pyt"
print(data[-3:])  # hon
print(data[-4:])  # thon