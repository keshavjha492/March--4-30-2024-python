# We can open a file in exclusive mode in python
# It means if a file already exists and we try to open in x mode it raises error


filename = "message.txt"

with open(filename, "x") as fp:
    fp.write("Hello World")
print("Written successfully !")