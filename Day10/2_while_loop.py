"""
Create a new list of repeated items from a provided list:
nums = [3, 4, 2, 2, 1, 3, 3, 3]
Output = [3, 2]

"""
nums = [3, 4, 2, 2, 1, 3, 3, 3]
result = []
for each in nums:
    if nums.count(each) > 1 and each not in result:
        result.append(each)  # [3, 2, 2, 3, 3, 3]

print(result)

result=[]
for i in range(1,11):
    result.append(i)
print(result)

result=[i for i in range(1,11)]
print(result)

# While loop is used with conditions or Truthy or Falsy values
# We should always update the condition variable from inside the while block.
# If the condition variable is not updated then the loop goes to infinite

a = 0
while a <= 10:
    print(a)
    a += 1

while 3:  # This is an infinite loop
    print("Hello World")

# if we need infinite loop then:
while True:
    print("Hello World")