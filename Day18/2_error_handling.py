# try...except block is used to handle errors in python
# try block is always executed initially
# If error is raised from the try block then the except block is executed
# We write codes with error-prone in the try block

try:
    data = int(input("Enter a number "))
except:
    print("Please enter a valid number")


# Variations
# 1. try...except exception as e

try:
    data = int(input("Enter a number "))
except Exception as e:
    print(e)
    print("Please enter a valid number")


# 2. try...except Handle specific error
try:
    data = int(input("Enter a number "))
except ValueError:
    print("Please enter a valid number")

# 3. try...except handle multiple errors
try:
    data = int(input("Enter a number "))
except (ValueError, TypeError, IndexError):
    print("Please enter a valid number")

# 4. try...except...except and so on
try:
    data = int(input("Enter a number "))
except ValueError:
    print("Please enter a valid number")
except IndexError:
    print("IndexError is raised")
except TypeError:
    print("TypeError")


# 5. try..except...else
try:
    d1 = int(input("Enter a number "))
    d2 = int(input("Enter a number "))
except:
    print("Enter a valid number")
else:
    result = d1 + d2
    print(result)

# 6. try..except..else...finally
try:
    d1 = int(input("Enter a number "))
    d2 = int(input("Enter a number "))
except:
    print("Enter a valid number")
else:
    result = d1 + d2
    print(result)
finally:
    print("This block is always executed")


fp = open("file.tx", "w")
try:
    data = fp.read()
except:
    print("Some error is raised")
finally:
    fp.close()