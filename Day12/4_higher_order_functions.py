# If a function takes another function as an argument then such a function is called higher order function

a = [(5, 4), (3, 2), (1, 7), (2, 9), (0, 10)]
# [(0, 10), (1, 7), (2, 9), (3, 2), (5, 4)]


def sort_by_first_element(item):  # item => (5, 4)
    return item[0]


a.sort(key=sort_by_first_element)
print(a)  # [(0, 10), (1, 7), (2, 9), (3, 2), (5, 4)]

# here sort() is a higher order function


a = [3, 4, 1, 2]
a.sort()  # ascending
print(a)  #

a.sort(reverse=True)  # descending


result = sorted(a)  # builtin function
print(result)