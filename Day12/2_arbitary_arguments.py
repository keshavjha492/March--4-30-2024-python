# Arbitrary arguments are the arguments to a function which can take random number of elements as input
# *args and **kwargs are the arbitrary arguments in Python
# They are like an expandable bucket


# args
def addition(*args):
    print(sum(args))
    print(args)
    print(type(args))  # tuple


addition(1, 2)  # 3
addition(1, 2, 3)  # 6
addition(1, 2, 3, 4)  # 10
addition(1, 2, 3, 4, 5)  # 15


# **kwargs
def addition(**kwargs):
    print(sum(kwargs.values()))
    print(kwargs)
    print(type(kwargs))  # dictionary


addition(a=1, b=2)  # 3
addition(a=1, b=2, c=3)  # 6
addition(a=1, b=2, c=3, d=4)  # 10
addition(a=1, b=2, c=3, d=4, e=5)  # 15