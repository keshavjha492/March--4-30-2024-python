# rb and wb are used for binary read and write respectively

import pickle


filename = "bin.txt"
name = "Sita"
age = 30
address = "KTM"

with open(filename, "wb") as fp:
    pickle.dump(name, fp)
    pickle.dump(age, fp)
    pickle.dump(address, fp)
print("Written to a binary file")


with open(filename, "rb") as fp:
    data = pickle.loads(fp.read())


print(data)
