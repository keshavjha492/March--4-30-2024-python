# update(), pop(), get(), keys(), values(), items(), clear()

# pop()
student = {"name": "Jon", "age": 30, "address": "KTM"}
name = student.pop("name")
print(student)  # {"age": 30, "address": "KTM"}
print(name)  # Jon

# roll = student.pop("roll")  # KeyError


# get()
student = {"name": "Jon", "age": 30, "address": "KTM"}

roll = student.get("roll", 30)
print(roll)  # 30

name = student.get("name", "Jane")
print(name)  # "Jon"


# keys()
student = {"name": "Jon", "age": 30, "address": "KTM"}

print(student.keys())  # dict_keys(["name", "age", "address"])
print(list(student.keys()))  # ["name", "age", "address"]

# values()
print(student.values())  # dict_values(["Jon", 30, "KTM"])
print(list(student.values()))


# items()
print(student.items())  # dict_items([("name", "Jon"), ("age", 30), ("address", "KTM")])


#clear()
student.clear()
print(student)  # {}