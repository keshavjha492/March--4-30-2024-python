# CSV stands for Comma Separated Values
# It is also a file format similar to json
# Python has a built-in module to support csv

import csv

filename = "students.csv"

with open(filename, "r") as cr:
    rows = csv.reader(cr)
    all_rows = list(rows)  # [['id','name',"age", "address"], [1,Jon,21,KTM]]
    columns = all_rows.pop(0)
    result = []
    for each in all_rows:
        result.append({
            "id": each[0], "name": each[1], "age": each[2], "address": each[3]
        })


data = ["a", "e", "i", "o", "u"]

for index, value in enumerate(data):
    print(index)
    print(value)
    
    
print(result)
"""
[{}, {}, {}]
"""