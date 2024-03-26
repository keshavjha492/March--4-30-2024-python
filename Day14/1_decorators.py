# Functions in Python can be stored in a variable, can be elements in an iterable and can be passed to another function

def addition(a, b):
    return a + b


add = addition

result = add(2, 3)
print(result)  # 5

a = [addition, 1, 2, add]
result = a[0](2, 3)
print(result)  # 5


# We can make closures in Python

def closure_fxn(msg):  # msg => Hello World
    def inner_fxn():
        print(msg)
    return inner_fxn


result = closure_fxn("Hello World")
print(result)  #
result()


# Criteria for a decorator
# 1. A function must take another function as an argument
# 2. There should be a nested function
# 3. The nested fxn should take reference of the passed function
# 4. Outer function must return the inner_fxn

# Decorator is a function which adds some extra functionality to the main function


def decorator_func(func):
    def inner_fxn():
        print("This is from decorator")

        func()
    return inner_fxn


@decorator_func
def message():
    print("I am learning decorator")


# result = decorator_func(message)
# message = decorator_func(message)  # This line is equivalent to @decorator_func
message()


@decorator_func
def display_messg():
    print("another message")
    
display_messg()