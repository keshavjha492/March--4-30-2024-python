# Create a decorator functions which converts a strings input to Uppercase


def to_upper(fun):
    def inner_fxn(*args, **kwargs):
        a= fun(*args, **kwargs)
        return a.upper()
    return inner_fxn

@to_upper
def message(msg):
    return msg


result = message("hello world")
print(result)


# Create a decorator function "login_required" which asks for a password. If the password matches
# "1234" then allow permission to access the main function else display the message "Not Allowed !!"

def login_required(func):
    def inner_fxn(*args, **kwargs):
        pw = input("Enter your password ")
        if pw == "1234":
            return func(*args, **kwargs)
        else:
            return "Not Allowed !!"
    return inner_fxn


@login_required
def addition(a, b):
    return a + b


result = addition(3, 4)
print(result)


# create a decorator function which calculate the execution time of a function

import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper

@execution_time
def my_fun():
    for i in range(100000000):
        pass

my_fun()


