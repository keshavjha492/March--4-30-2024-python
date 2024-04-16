# We can use switch..case in python using a dictionary


a = 3

if a == 1:
    print("Ram")
elif a == 2:
    print("Hary")
elif a == 3:
    print("Gita")
else:
    print("Alex")


a = 5
name_number_map = {
    1: "Ram", 2: "Hary", 3: "Gita"
}

print(name_number_map.get(a, "Alex"))


# match case
"""
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")
    
    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
"""