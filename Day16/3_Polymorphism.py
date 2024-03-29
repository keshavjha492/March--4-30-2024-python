# Method Overloading
# In python method overloding is not possible

# def addition(a, b):
#     return a + b


def addition(a, b, c=0):
    return a + b + c


r1 = addition(2, 3)
r2 = addition(2, 3, 4)

print(r1)
print(r2)


def addition(*args, **kwargs):
    if kwargs:
        return sum(args) + sum(kwargs.values())
    return sum(args)


print(addition(2, 3))
print(addition(2, 3, 5))
print(addition(2, 3, 5, a=6, b=7))

# Method overloading behaves in the same way of function overloading


class Vehicle:
    def get_details(self):
        return "This is vehicle"

    def get_details(self):
        return "This is a Vehicle"

v = Vehicle()
print(v.get_details())