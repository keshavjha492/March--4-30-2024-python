import json
filename="students.json"

def read_student(student_id):
    id = input("enter the id you want to search")
    with open(filename, 'r') as fp:
        students = json.loads(fp.read())
        for students in students:
            if students["id"]==id:
                print(students)
    count =input("do you want to continue? (Y/N)")
    return True if count.lower() == "y" else False