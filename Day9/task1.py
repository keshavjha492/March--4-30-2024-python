# WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 

A = float(input("enter the hour that you have worked"))
B= float(input("enter the pay rate"))
if A >40:
    total = 40 * B + (A-40)*B*1.5
    print("your pay will be", total)
else:
    total = A*B
    print("your pay will be", total)
