# break, continue and pass
# break, continue and pass are the keywords on itself

# "break" is used to terminate a loop
a = [1, 2, 3, 4, 5]
for each in a:
    print(each)
    if each == 3:
        break

a = 0
while a <= 5:
    print(a)
    a += 1
    if a == 3:
        break


# continue
# continue is used to skip a step in a loop

a = [1, 2, 3, 4, 5]
for each in a:
    if each == 3:
        continue
    print(each)

a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)


a = 1
while a <= 5:
    if a == 3:
        a += 1
        continue
    print(a)
    a += 1
    
# if the loop is traversed completely then the else block is executed
a = [1, 2, 3, 4, 5]
for each in a:
    print(each)
    if each == 3:
        break
else:
    print("The loop is complete")
    
    
# pass
# pass does nothing. It is just to maintain correct code syntax
# Sometimes it is also used as a placeholder for future code


a = 5
if a:
    pass  # placeholder for future code


def addition():
    pass