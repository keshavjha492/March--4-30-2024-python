# iterable => sequence of data which can be used with for loop
# iterables are the objects from which we can obtain iterator object

vowels = ["a", "e", "i", "o", "u"]  # => iterable
iter_obj = iter(vowels)  # iterator object

# Iterator object follows next() protocol
print(next(iter_obj))  # a
print(next(iter_obj))  # e
print(next(iter_obj))  # i
print(next(iter_obj))  # o
print(next(iter_obj))  # u
# print(next(iter_obj))  # StopIteration


# for loop is also kind of while loop in python
iter_obj = iter(vowels)  # iterator object
while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        break

for i in vowels:
    print(i)


# a = 1  # Not an iterable
# iter(a)  # It raises error