vowels = ("a", "e", "i", "o", "u")
for vowel in vowels:
    print(vowel)  # a e i o u

# For loop is similar for list, tuple and set
# But it might get quite tricky for looping in a dictionary

# Looping in Dictionary
student = {"name": "Jane", "age": 21, "address": "KTM"}

for data in student:
    print(data, student[data])  # name  age  address


# values = student.values()
for value in student.values():
    print(value)  # Jane  21  KTM


for key in student.keys():
    print(key)  # name  age  address


items = student.items()  # [("name", "Jane"), ("age", 21), ("address", "KTM")]
for item in items:
    print(item)
    print(type(item))  # tuple


for key, value in student.items():
    print(key)  # name   age   address
    print(value)  # Jane  21    KTM