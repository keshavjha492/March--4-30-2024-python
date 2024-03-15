a = 1
print(type(a))  # int

a = 1,
print(type(a))  # tuple

a = 1, 2, 3  # => This is tuple packing
print(a)  # (1, 2, 3)

a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3


# WAP to swap two values
a = 2
b = 3

temp = a
a = b
b = temp

print(a)  # 3
print(b)  # 2


# Do the same task using tuple packing-unpacking

a = 2
b = 3

a, b = b, a  # (3, 2)
print(a)  # 3
print(b)  # 2


# Possible errors in tuple packing-unpacking

# a, b = 1, 2, 3  # Error
# # Too many values to unpack

# a, b, c = 1, 2  # Error
# Not enough values to unpack

# Number of variables in LHS must be same to values at RHS