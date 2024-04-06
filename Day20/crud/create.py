import json
import os
filename="students.json"



def create_students():
    id = input("enter students id")
    name = input("enter students name")
    age = input("enter the students age")
    address = input("enter the students address")

    student = dict(id=id, Name=name, age=age, address=address)
    if not os.path.exists(filename):
        with open(filename,"w") as fp:
            data = json.dumps([student], indent=2)
            fp.write(data)
    else: 
        with open(filename,"r+") as fp:
            students=json.loads(fp.read()) 
            students.append(student)
            fp.seek(0)
            data= json.dumps(students, indent=2)
            fp.write(data)
    print("students added successfully")
    count = input("do you want to continue? (y/n)")
    return True if count.lower=="y" else False