# students = ["Jon", "Jane", "Hary", "Alex"] Write the above list in a binary file "student.dat"
# Read the binary file and create a dictionary with information of student and their respective exam marks 
# Finally write the info again to the binary file "marks.dat"


import pickle

students = ["Jon", "Jane", "Hary", "Alex"]

filename = "Day24/student.dat"
with open(filename, "wb") as f:
    pickle.dump(students, f)
    
with open(filename, "rb") as f:
    students = pickle.load(f)
print(students)

marks = {student: 0 for student in students}

marks["Jon"] = 90
marks["Jane"] = 85
marks["Hary"] = 80
marks["Alex"] = 95

with open("Day24/marks.dat", "wb") as f:
    pickle.dump(marks, f)