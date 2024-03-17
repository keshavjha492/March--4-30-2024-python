# "Nested if" is also possible in python


a = 1
b = 2
c = 3

if c > a:
    if c > b:
        print("c is the greatest")
    else:
        print("c is not the greatest")
else:
    print("a is greater than c")