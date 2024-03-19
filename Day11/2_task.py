"""
Check whether a number is palindrome or not
a = 121
Output = “It is a palindrome number”
A = 321
output = “It is not a palindrome number”

"""

num = input("Enter a number ")

if num == num[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


num = int(input("Enter a number "))
temp = num
summ = 0

while num != 0:  # 321
    r = num % 10  # 1  2  3
    summ = summ * 10 + r  # 123
    num = num // 10  # 0
    
if temp == summ:
    print("It is palindrome")
else:
    print("It is not palindrome")
    


"""
WAP to delete all the occurrences of a specified character in a given string
S = “All the occurrences of a specified character in a given string”
Input = “a”
Output = “ll occurrences of  specified chrcter in  given string”

"""
S = "All the occurrences of a specified character in a given string"
char = input("Enter the character yo want to remove ")  # a
result = ""
for each in S:
    if each.lower() == char.lower():
        continue
    result += each  # "ll"
print(result)