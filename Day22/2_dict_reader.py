import csv

filename = "students.csv"

with open(filename, "r") as cr:
    rows = csv.DictReader(cr)
    print(list(rows))  # [{}, {}, {}]
    for each in rows:
        print(each['name'])
        print(each['age'])
        print(each['address'])