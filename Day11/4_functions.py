# functions are the reusable block of code
# It can be visualized as a machine which takes input and always returns the same 
# o/p for same input

# We use "def" keyword to define a function in Python

# There are two parts of a function. 
#     => Function Definition
#     => Function Call

def addition(a, b):  # Function Definition
    r = a + b
    return r


result = addition(2, 3)  # Function Call
print(result)  # 5


# Variations
# With arguments without return
def addition(a, b):  # Function Definition
    r = a + b
    print(r)  # if a function doesn't return anything then it returns None by default

result = addition(2, 3)
print(result)  # None


# Without arguments with return
def message():
    return "I am learning function"


msg = message()
print(msg)  # I am learning function

# Without arguments without return
def message():
    print("I am learning function")

msg = message()
print(msg)  # None