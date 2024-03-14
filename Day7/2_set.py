# Set is mutable datatype
# It is also an iterable enclosed within curly braces
# Set itself is mutable but every element of a set must be immutable

# Creating an empty set
data = set()  # empty set
d = {}  # This is empty dictionary

# Creating non-empty set
a = {1, 2, 3}
b = {"1", 2, "apple"}
# c = {1, 2, [4, 5]}  # Invalid


# Set is unordered. Order doesn't matter
print({1, 2} == {2, 1})  # True

a = {1, 1, 2, 3, 2, 3}
print(a)  # {1, 2, 3}

# Because of this, we cannot do indexing or slicing in set

# Adding and Removing elements in a set

# Add and Update
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}


s.update([5, 6, 7])
print(s)  # {1, 2, 3, 4, 5, 6, 7}


# Remove
# remove(), discard(), clear(), pop()

s = {1, 2, 3, 4}
s.remove(4)
print(s)  # {1, 2, 3}

# s.remove(10)  # Error


s.discard(3)
print(s)  # {1, 2}

s.discard(10)  # No Error
print(s)  # {1, 2}

s.clear()
print(s)  # {}


s = {1, 2, 3, 4, 5}
s.pop()  # Randomly removes element from arbitrary position
print(s)  # {1, 2, 3, 4}