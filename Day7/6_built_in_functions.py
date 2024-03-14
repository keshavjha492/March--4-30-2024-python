items = {"pen": 20, "pencil": 31, "erasers": 12}

total_items = sum(items.values())
print(total_items)  # 63

# all() and any()
# Both all() and any() takes iterable as an input


# all() takes iterable as an input and if all the items of the iterable are truthy then
# all() returns True. But if one or more elements are Falsy then it returns False

result = all(items.values())
print(result)  # True

result = all([1, 2, [3, 4], None])
print(result)  # False

result = all([1, 2, [3, 4], 0])
print(result)  # False


# any() takes iterable as an input and if one of the items of the iterable is truthy then it returns True
# any() returns False if all the elements of the iterable are Falsy

result = any([1, 2, True, 0])
print(result)  # True

result = any([0, None, False, [], {}])
print(result)  # False