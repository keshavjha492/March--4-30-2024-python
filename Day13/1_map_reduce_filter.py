# map(), reduce() and filter() are the built-in functions in python
# They are higher order functions which take function as an argument

# map()
# map takes two arguments. First argument is a function and second should be an iterable
# map function changes each item of the iterable into a new form.
# the change of the element is based on the function definition
# The final count of the mapped elements and the initial iterable is same in the case of map.

data = [1, 2, 3, 4, 5]


def add_ten_to_each_element(element):
    return element + 10


result = map(add_ten_to_each_element, data)

print(list(result))  # [11, 12, 13, 14, 15]


# filter()
# filter takes two arguments. First argument is a function and second should be an iterable
# filter function picks certain items of the iterable.
# the choosing of the element is based on the function definition
# The final count of the filtered elements and the initial iterable may or may not be same

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_odd_number(element):
    if element % 2 == 0:
        return False  # Falsy
    return True  # Truthy


result = filter(is_odd_number, data)

print(list(result))  # [1, 3, 5, 7, 9]



# reduce()
# reduce takes two arguments. First argument is a function and second should be an iterable
# reduce function process the input and gives a single result.
# the processing of the element is based on the function definition
# The final result is a single item

import functools

data = [1, 2, 3, 4, 5]

def sum_of_all(x, y):
    return x + y

result = functools.reduce(sum_of_all, data)
print(result)  # 15

