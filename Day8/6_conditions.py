# Condition statement is used to make decisions in a program during program execution
# We can write conditions or True or False or any other Truthy or falsy data with if statement

# Variations of if statements in Python

# 1. Simple if
a = 5
b = 10
if a:
    print("a is not zero")

if b > a:
    print("b is greater than a")

#2.  if...else statement
a = 0
if a:
    print("a is not zero")
else:
    print("a is 0")


# 3. if...elif...elif...  (if..elif ladder)
a = 2
b = 2
c = 5

if a > c:
    print("a is greater than c")
elif a == b:
    print("a is equal to b")
elif c > b:
    print("c is greater than b")


# 4. # 3. if...elif...elif...else
if a > c:
    print("a is greater than c")
elif a == b:
    print("a is equal to b")
elif c > b:
    print("c is greater than b")
else:
    print("None of the above statements are True")


a = 2
b = 2
c = 5

if c > a:
    print("c is greater than a")
elif a == b:
    print("a is equal to b")
elif c > b:
    print("c is greater than b")


if c > a:
    print("c is greater than a")
if a == b:
    print("a is equal to b")
elif c > b:
    print("c is greater than b")


# 5. ternary if
a = 10
b = 5
print("b is greater than a") if b > a else print("a is greater than b")

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")