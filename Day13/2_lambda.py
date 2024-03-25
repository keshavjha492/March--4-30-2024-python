# lambda is the anonymous function in python (function has no name)
# Lambda functions are used when it has to be passed directly to another function
# Lambda functions are the one-liner function

def addition(x, y):
    return x + y

lambda x, y: x + y


# map()
data = [1, 2, 3, 4, 5]
result = map(lambda x: x + 10, data)
print(list(result))  #  [11, 12, 13, 14, 15]


# filter()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x % 2 != 0, data)
print(list(result))  # [1, 3, 5, 7, 9]


# reduce()
import functools
data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)  # 15