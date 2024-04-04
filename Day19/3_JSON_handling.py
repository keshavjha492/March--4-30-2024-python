# JSON stands for Javascript Object Notation
# JSON is a file format to share data among different entities. For example, it helps in the communication
# between FE and BE, BE and Mobile end, BE and BE

# There is also another format for data sharing i.e XML

# Example iof JSON is {"name": "Ram", "age": 20, "dob": "2004-02-12", "salary": 2440.12}
# JSON looks alike Python dictionary but there are differences.
# Keys and values of JSON object must be enclosed within double quotes (single not allowed) unless integer or
# float
# JSON objects don't support complex object. They only support string, integers and float
# Unlike python dictionary (which supports all immutable objects as a key), JSON only supports string

results = [
    {"name": "Ram", "age": 20},
    {"name": "Ram", "age": 20},
    {"name": "Ram", "age": 20},
]  # This is also a valid JSON
# Json can either be in array format or in object format
a = [1, 2, 3]  # This is also a valid JSON
b = [1, "Ram", 2]  # This is also a valid JSOn

# Python has a good support for JSON as it has a builtin json module
# Extension for json file is .json

filename = "student.json"
import json

# There is a concept of json dumps and loads
# dumps meas to write in a file
# loads means to read from a file

student = {'name': "Ram", 'age': 20, "address": "KTM"}
with open(filename, "w") as fp:
    data = json.dumps(student)
    fp.write(data)

with open(filename, "r") as fp:
    data = fp.read()
    print(data)
    print(type(data))
    x = json.loads(data)
    print(type(x))
    print(x["name"])

students = [
    {'name': "Ram", 'age': 20, "address": "KTM"},
    {'name': "Shyam", 'age': 21, "address": "PKR"},
    {'name': "Alex", 'age': 22, "address": "LTP"},
    {'name': "Jon", 'age': 23, "address": "BKT"},
]

filename = "students.json"
with open(filename, "w") as fp:
    data = json.dumps(students, indent=2)
    fp.write(data)

with open(filename, "r") as fp:
    data = fp.read()
    x = json.loads(data)
    print(x[2]["address"])