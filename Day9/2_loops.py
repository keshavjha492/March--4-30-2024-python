# Loops are used to perform repetitive task in Python
# Loops are also called iterations
# There are two types of loops in Python

# 1. for loop
# 2. while loop
# 3. do...while (This is not possible in python)


# For loops in python
# for loop is used with iterables (sequence data) in python
# Unlike in C/C#/Java condition is not checked in python for loop

# for(i=0;i<=10;i++){
#     printf(i)
# }

vowels = ["a", "e", "i", "o", "u"]
for each in vowels:  # traversing in vowels
    print(each)

# range()
# range is a python built-in function to generate n numbers

data = range(10)
print(list(data))  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

data = range(0, 10)
print(list(data))  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

data = range(2, 7)
print(list(data))  # 2, 3, 4, 5, 6

data = range(1, 10, 2)
print(list(data))  # 1, 3, 5, 7, 9


# WAP to print "Hello World" 50 times
for _ in range(51):
    print("Hello World")


# enumerate()
# enumerate() is a python built-in function to give the elements of iterable along with their count

vowels = ["a", "e", "i", "o", "u"]
data = enumerate(vowels)
print(list(data))  # [(0, a), (1, e), (2, i), (3, o), (4, u)]

data = enumerate(vowels, start=1)
print(list(data))  # [(1, a), (2, e), (3, i), (4, o), (5, u)]

for i in range(len(vowels)):
    print(vowels[i])


for each in enumerate(vowels):
    print(each)  # (0, a)

for index, vowel in enumerate(vowels):  # here "index, value" is unpacking tuple from each loop
    print(index, vowel)  # 0  1  2  3  4

for index, vowel in enumerate(vowels[::-1]):  # reverse / here "index, value" is unpacking tuple from each loop
    print(index, vowel)  # 0  1  2  3  4