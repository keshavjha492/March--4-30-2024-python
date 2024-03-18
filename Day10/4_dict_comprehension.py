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


result ={i : i for i in range(1,5)}
print(result)