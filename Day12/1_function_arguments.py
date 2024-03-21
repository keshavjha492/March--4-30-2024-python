# Arguments are the input to a function

# There are three types of function arguments
# 1. Positional Arguments
# 2. Keyword/ default Arguments
# 3. Arbitrary Arguments


# Positional
# Positional arguments are the required arguments to a function

def addition(a, b):
    return a + b


result = addition(3, 5)  # They are must to be sent arguments
print(result)

# result = addition(2)  # It raises error


# Keyword / Default Argument
def addition(a, b, c=0):  # here c is a default argument
    return a + b + c

# Default arguments are for the fallback. If actual value is passed during a function call then it is prioritized
result = addition(1, 2, 3)
print(result)  # 6

result = addition(1, 2)
print(result)  # 3


# Variations in Keyword / Default arguments

def addition(a, b, c=0):
    return a + b + c


result = addition(a=1, b=2, c=3)
print(result)

result = addition(b=1, c=2, a=4)
print(result)

result = addition(1, c=2, b=4)
print(result)

result = addition(1, 2, c=5)
print(result)  # 8


# Possible Errors
# result = addition(1, 2, b=3)  # It raises error
# result = addition(a=1, 2, 3)  # It raises error

# result = addition(a=1, b=2, 4)  # It also raises error


# def addition(a, b=0, c):  # It raises error
#     return a + b + c