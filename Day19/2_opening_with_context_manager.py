# Advantage of using context manager in file is, we do not need to explicitly close the file
# the file closes itself while the context manager block ends


filename = "day19/tet1.txt"

with open(filename, "w") as fp:  # context manager
    fp.write("Writing in file using context manager")
    
with open(filename,"r+") as fp:
    data = fp.read()
    fp.write("\n this is a new line of the code")
print(data)

with open(filename,"w+") as fp:
    fp.write("this is the as write and read mode")
    fp.seek(0)
    data = fp.read()
print(data)

with open(filename,"a") as fp:
    fp.write("\nthis is a new line of the append")
    