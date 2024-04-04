# We can use python to open, read, write and append in a file
# We can open files in various modes
# 1. Read Mode (r)
# 2. Write Mode (w)
# 3. Append Mode (a)
# 4. Read and Write (r+)
# 5. Write and read (w+)
# 6. Exclusive Mode (x)
# 7. Binary Read (rb)
# 8. Binary Write (rw)
# 9. Binary read and write (rb+)
# 10. Binary write and read (rw+)

filename = "Day19/test1.txt"


# If you open the file in write then it completely overrides the previous content
fp = open(filename, "w")
fp.write("Hello World.")
fp.close()

fp = open(filename, "r")
data = fp.read()
fp.close()
# print(data)

fp = open(filename, "a")
fp.write("\nI am learning file handling")
fp.close()


fp = open(filename, "r+")
data = fp.read()
# print(data)
fp.write("\nThis is a new line")
fp.close()


fp = open(filename, "w+")
fp.write("\nSecond line")
fp.seek(0)
data = fp.read()
fp.close
print(data)