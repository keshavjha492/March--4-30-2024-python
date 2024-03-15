# Tuple being immutable there are only two methods
# index()
# count()

data = ("a", "b", "c", "b", "a", "a", "b")

result = data.count("a")
print(result)  # 3

result = data.index("a")
print(result)  # 0

result = data.index("a", 1, 6)
print(result)  # 4