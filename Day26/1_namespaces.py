# Namespaces define the scope of variables / identifier in a python module / package
# It is explained by LGB rule
# L => Local, B => Built in scope, G => Global scope

import json  # built in scope
import csv


a = 1  # Global scope


def addition(x, y):
    global a
    a = 3   # Local scope
    print(a)


print(a) # 1
addition(2, 3)

print(a)  # 3