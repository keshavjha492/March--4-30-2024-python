# capitalize()
# title()
# upper()
# lower()
# split()
# join()


# title()
a = "hello world"
result = a.title()
print(result)  # Hello World

# capitalize()
a = "hello world"
result = a.capitalize()
print(result)  # Hello world


# upper()
result = a.upper()
print(result)  # HELLO WORLD

# lower()
a = "Hello World"
result = a.lower()
print(result)  # hello world


# split()
a = "hello world"
result = a.split()
print(result)  # ["hello", "world"]

result = a.split("o")
print(result)  # ["hell", " w", "rld"]


# join()
data = ["Python", "is", "high", "level", "language"]
result = " ".join(data)
# result = data.join(" ")  # This is wrong because list doesn't have join method
print(result)  # Python is high level language 

result = " + ".join(data)
print(result)

d = "hello world"
print(d[::-1])  # It reverses the string


data = [1, 2, 3, 4]

data[2] = 9
print(data)  # [1, 2, 9, 4]  # Here list is mutable so we can replace one of the elements

data = "hello"
# data[2] = "L" # We are not allowed tp replace a string element as strings are immutable