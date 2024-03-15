# sorted()
data = (2, 10, 20, 1, 5, 3)
result = sorted(data)
print(result)  # [1, 2, 3, 5, 10, 20]

result = sorted(data, reverse=True)
print(result)  # [20, 10, 5, 3, 2, 1]


a = [5, 4, 1, 2]
result = a.sort()  # List Method
result = a.sort(reverse=True)  # List Method
print(result)  # None


# reversed
data = (2, 10, 20, 1, 5, 3)
result = reversed(data)
print(list(result))  # [3, 5, 1, 20, 10, 2]