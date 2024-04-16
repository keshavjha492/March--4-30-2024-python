# If a function calls itself inside it's definition then such a function is called
# recursive function


x = 0


def count():  # function definition
    global x
    print(x)
    x += 1
    if x == 10:
        return
    count()  # function call

count()  # function call


# Calculate the factorial of 5 using
# 1. Normal loop
# 2. reduce() function
# 3. Recursive function


fact = 1
num = int(input("Enter a number "))
for i in range(1, num+1):
    fact = fact * i
else:
    print(f"factorial of {num} is ", fact)


from functools import reduce

result = reduce(lambda x, y: x * y, range(1, num+1))
print(result)  # 120


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 5 * factorial(4) = 5 * 24 = 120
# 4 * factorial(3) = 4 * 6 = 24
# 3 * factorial(2) = 3 * 2 = 6
# 2 * factorial(1) = 2 * 1 = 2
# 1 * factorial(0)  = 1 * 1 = 1


result = factorial(5)
print(result)