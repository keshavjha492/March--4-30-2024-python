
students = [
    {"name": "Jon", "age": 21, "address": "KTM"},
    {"name": "Jane", "age": 25, "address": "BKT"},
    {"name": "Alex", "age": 27, "address": "LTP"},
    {"name": "Hary", "age": 30, "address": "PKR"},
    {"name": "Arya", "age": 28, "address": "KTM"},
]
# filter those students whose age is greater than 25 using filter() function
# 1. Normal Solution
# 2. using filter() function

def is_age_gt_25(student):
    return student["age"] >= 25

filtered_students = list(filter(is_age_gt_25, students))

print(filtered_students)



filtered_stu = []

for student in students:
    if student["age"] >= 25:
        filtered_stu.append(student)

print (list(filtered_stu))


students = [
    {"name": "Jon", "age": 21, "address": "KTM"},
    {"name": "Jane", "age": 25, "address": "BKT"},
    {"name": "Alex", "age": 27, "address": "LTP"},
    {"name": "Hary", "age": 30, "address": "PKR"},
    {"name": "Arya", "age": 28, "address": "KTM"},
]

def upper(student):
    student["name"] = student["name"].upper()
    return student


filtered_students = list(map(upper, students))

print(filtered_students)

import functools

def add(x, y):
    if type(x)== dict:
        return x["age"] + y["age"]
    return x + y["age"] 


filtered_students = (functools.reduce(add, students))

print(filtered_students)