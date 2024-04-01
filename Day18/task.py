try:
    data = int(input("enter the number"))
    data2 = int(input("enter the second number"))
    result = data/data2
    print (result)
except ValueError:
    print("please enter the valid number in program and re run")
except ZeroDivisionError:
    print("2nd value is 0")
else:
    result = data + data2
    print(result)
    

try:
    a = int(input("enter the number"))
    b= int(input("enter the second number"))
    result = a / b
    print(result)
except ZeroDivisionError:
    print("second value is 0")
finally:
    print("this program is completed")
    
    
student = {'id': 1, 'name': 'John', 'age': 22, 'department': 'Computer Science'}

key = input('Enter the key you want to access (id, name, age, or department): ')

try:
    key = input('Enter the key you want to access (id, name, age, or department): ')
    result = student[key]
    
except:
    print('the key is not present in dict')
else:
    print(f"the {key} of the student is {result}")