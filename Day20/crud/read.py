import json
filename = "students.json"


def read_students(student_id):
    with open(filename, 'r') as fp:
        students = json.loads(fp.read())
    student = list(filter(lambda x: x["id"] == student_id, students))
    if student:
        student = student[0]
        print(student)
    else:
        print("No matching student id")
    count = input("Do you want to continue?(y/n) ")
    return True if count.lower() == "y" else False