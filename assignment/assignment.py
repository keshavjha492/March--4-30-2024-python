
# 1
a = "Python + is + an + awesome + language"
b = a.split(' + ')  
result = ' '.join(b)  
print(result)


# 2
str = input("Enter a string")
dict = {} 
for i in str:
    if i in dict: 
        dict[i] += 1
else:
    dict[i] = 1 
    for key in dict:
        print(key,':',dict[key])
        
# 3
d1 = {'a': 100, 'b': 200, 'c':300} 
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d2:
    if i in d1:
        d2[i] = d2[i] + d1[i]
    else:
        pass
print(d2)

# 4
a= input("enter the string1 : ")
b= input("enter the string2 : ")
if sorted(a) == sorted(b):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# 5
num = int(input("Enter a number "))
temp = num
summ = 0

while num != 0:
    r = num % 10
    summ = summ * 10 + r 
    num = num // 10  
if temp == summ:
    print("It is palindrome")
else:
    print("It is not palindrome")