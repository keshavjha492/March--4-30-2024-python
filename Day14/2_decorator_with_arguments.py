def decorator_func(func):
    def inner_fxn(x, y):

        print("Extra Functionality")

        return func(x, y)
    return inner_fxn


@decorator_func
def addition(a, b):
    return a + b

result = addition(2, 3)
print(result)



def decorator_func(func):
    def inner_fxn(*args, **kwargs):

        print("Extra Functionality")

        return func(*args, **kwargs)
    return inner_fxn


@decorator_func
def addition(a, b, c):
    return a + b + c

result = addition(2, 3, 4)
print(result)


@decorator_func
def another_addition(a, b):
    return a + b

result = addition(2, 3)
print(result)