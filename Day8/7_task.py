a = int(input("enter the number"))
if a % 3 == 0 and a % 5 == 0:
    print("fizzbuzz")
elif a % 3 == 0:
    print("fizz")
elif a % 5 == 0:
    print("buzz")
else:
    print(a)
