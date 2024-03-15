# Tuples are immutable datatypes in Python
# They are sequence of heterogeneous data types enclosed within small brackets (iterable)

# int
# float
# list
# tuple
# dict
# set
# bool
# complex

# Creating empty tuples
a = ()
print(a)
b = tuple()


# Creating non-empty tuples
a = [1, 2, 3]
b = tuple(a)  # type casting
print(b)  # tuple datatype

c = ("a", "e", "i", "o", "u")

# Accessing tuple elements
# Tuple elements can also be accessed using indexing and slicing similar to list

# Indexing
# Forward indexing starts from 0 while reverse indexing from -1
vowels = ("a", "e", "i", "o", "u")
print(vowels[0])  # "a"
print(vowels[3])  # "o"
print(vowels[-1])  # u
# print(vowels[10])  # IndexError
# print(vowels[-10])  # IndexError

# Slicing
# Slicing is also similar to the list slicing

data = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
print(data[:5])  # ("a", "b", "c", "d", "e")
print(data[2:9])  # "c", "d", "e", "f", "g", "h", "i"
print(data[8:3])  # ()
print(data[7:])  # "h", "i", "j"
print(data[0:6])  # "a", "b", "c", "d", "e", "f"
print(data[-9:-2])  # "b", "c", "d", "e", "f", "g", "h"
print(data[-3:-8])  # ()
print(data[2:-2])  # "c", "d", "e", "f", "g", "h"
print(data[-3:])  # "h", "i", "j"
print(data[:-2])  # "a", "b", "c", "d", "e", "f", "g", "h"
print(data[2:9:2])  # "c", "e", "g", "i"