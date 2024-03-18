result = list()
for i in range(1, 11):
    result.append(i)
print(result)

# List Comprehension
# It is a one-liner efficient / elegant way of creating a list
result = [i for i in range(1, 11)]
print(result)


even = []
for i in range(1, 11):
    if i % 2 == 0:
        even.append(i)

print(even)   # [2, 4, 6, 8, 10]

result = [i for i in range(1, 11) if i % 2 == 0]  # comprehension with condition
print(result)