# Dict comprehension is one-liner dict creating method
# It is similar to list comprehension

data = [("name", "Jon"), ("age", 21)]

result = {k: v for k, v in data}  # {"name": "John", "age": 21}
print(result)


result = {}
for i in range(1, 6):
    result[i] = i ** 2

print(result)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


result = {i: i ** 2 for i in range(1, 6)}  # dict comprehension
print(result)


# {1: 1, 2: 2, 3: 3, 4: 4}
result = {i: i for i in range(1, 6)}
print(result)

result = {i: i for i in range(1, 10) if i % 2 == 0}  # dict comprehension with condition
print(result)


# zip() built-in function
keys = ["name", "age", "address"]
values = ["Jon", 30, "KTM"]

data = zip(keys, values)
print(dict(data))