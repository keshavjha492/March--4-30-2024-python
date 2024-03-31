# Operator overloading is also one of the features of Python OOP
# In python most of the operators invoke the magic methods
# Magic methods are the methods with double underscores in each side
# Magic methods are also called dunder methods


a = 1
b = 2
print(a + b)
result = a.__add__(b)
print(result)

print(b.__sub__(a))

a = [1, 2, 3]
iter_a = iter(a)
# print(next(iter_a))
print(iter_a.__next__())


class A:
    def __str__(self):
        return "Object of A"

    def __add__(self, other):
        return self.v + other.v


a = A()  # obj
print(a.__str__())
print(str(a))