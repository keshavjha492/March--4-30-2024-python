# difference()
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

result = s1.difference(s2)
print(result)  # {1, 2, 3}

print(s1 - s2)


# intersection()
result = s1.intersection(s2)
print(result)  # {4, 5}
print(s1 & s2)

# union()
result = s1.union(s2)
print(result)  # {1, 2, 3, 4, 5,6,7, 8}
print(s1 | s2)

# symmetric_difference()
result = s1.symmetric_difference(s2)
print(s1)  # {1, 2, 3, 4, 5}
print(s2)  # {4, 5, 6, 7, 8}
print(result)  # {1, 2, 3, 6, 7, 8}
print("Carrot Operator", s1 ^ s2)

result = s1.symmetric_difference_update(s2)
print(result)  # None
print(s1)  # {1, 2, 3, 6, 7, 8}
print(s2)  # {4, 5, 6,7, 8}

# isdisjoint()
result = s1.isdisjoint(s2)
print(result)  # False


# issubset()
s1 = {1, 2, 3, 4, 5}
s2 = {3, 2}

result = s2.issubset(s1)
print(result)  # True

result = s2.issuperset(s1)
print(result)  # False

result = s1.issuperset(s2)
print(result)  # True