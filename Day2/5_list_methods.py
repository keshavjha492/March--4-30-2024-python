# What are methods?
# Those functions which are defined inside a class are called methods

# Functions
# => Built-in functions
# => User-Defined functions
# => Built-in Methods (Those functions which are already defined in python classes)
# => User-defined methods (Those functions which are defined inside user-defined class)


# List Methods

# append()
a = [1, 2, 3]  # list object
a.append(4)
print(a)  # [1, 2, 3, 4]


# extend()
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]


# insert()
vowels = ["a", "e", "o", "u"]
vowels.insert(2, "i")
print(vowels)  # ["a", "e", "i", "o", "u"]


# index()
vowels = ["a", "e", "i", "o", "u"]
result = vowels.index("i")
print(result)  # 2


# remove()
vowels = ["a", "e", "i", "o", "u"]
vowels.remove("o")
print(vowels)  # ["a", "e", "i", "u"]

# vowels.remove("z")  # Error


# pop()
vowels = ["a", "e", "i", "o", "u"]
result = vowels.pop()
print(vowels)  # ["a", "e", "i", "o"]
print(result)  # "u"

vowels = ["a", "e", "i", "o", "u"]
result = vowels.pop(3)
print(result)  # "o"
print(vowels)  # ["a", "e", "i", "u"]

# vowels.pop(10)  # It raises error.


# count()
data = [3, 2, 1, 1, 1, 3, 3, 3, 3, 4, 5]
result = data.count(1)
print(result)  # 3

# print(data.count())  # It raises error


# clear()
vowels = ["a", "e", "i", "o", "u"]
vowels.clear()
print(vowels)  # []


# copy()
a = [1, 2, 3]
b = a

print(a == b)  # True
print(a is b)  # True

b = a.copy()
print(a == b)  # True
print(a is b)  # False


# Concept of shallow copy and deep copy
a = [1, 2, [3, 4]]
b = a.copy()

a[2][1] = 7
print(a)  # [1, 2, [3, 7]]
print(b)  # [1, 2, [3, 7]]


from copy import deepcopy
b = deepcopy(a)

a[2][1] = 9
print(a)  # [1, 2, [3, 9]]
print(b)  # [1, 2, [3, 7]]