# Given a list of students ["Jon", "Jane", "Hary", "Alex"] create a list of dictionaries with
# random address and random exam marks. Dump the list to a JSON file students.json. Again read the json file
# and print the address of "Hary"

import random
import json
students = ["Jon", "Jane", "Hary", "Alex"]
addresses = ["KTM", "Pokhara", "Bhaktapur", "Lalitpur"]
filename = "students.json"

data = []
for name in students:
    student = {"name": name, "address": random.choice(addresses), "marks": random.randint(0, 100)}
    data.append(student)
print(data)


with open(filename, "w") as fp:
    fp.write(json.dumps(data, indent=2))
    print("Added to file successfully !")

with open(filename, "r") as fp:
    students = json.loads(fp.read())  # [{}, {}, {}]

for student in students:
    if student["name"] == "Hary":
        print(f"The address of {student['name']} is {student['address']}")