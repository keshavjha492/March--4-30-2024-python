# What are Keywords?
# Keywords are the reserved words in python (or in any other language) which have their special meaning
# There are 35 keywords in Python => help("keywords")

# What are identifiers?
# Identifiers are the user-defined names while writing codes.
# variable name, function name, class name, file name etc. are the identifiers

# Rules for naming identifiers

#1. Identifiers can't start with a number. They should always start with A-Z or a-z
# 1a = 12  # This is an error.
a = 12
    # But it may occur somewhere in between
    
a12 = 15  # This is valid


# 2. Identifiers are case-sensitive
a = 12
A = 13
print(a)  # 12
print(A)  # 13

# 3. Identifiers can't contain special symbols, !, @, # etc.
# a@ = 12   this is an error

# 4. Identifiers can't be keywords

# def = 12  not allowed because def is a keyword to create a function in python


# 5. Identifiers can contain "_" anywhere
_a = 1
__a__ = 12
a_ = 12
a_b = 13
_ = 12