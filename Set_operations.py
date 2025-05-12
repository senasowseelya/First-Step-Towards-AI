set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'cherry', 'date', 'fig'}

for element in set1:
    print(element)

# Union: all unique elements from both sets
print(set1.union(set2))          # or set1 | set2

# Intersection: common elements
print(set1.intersection(set2))   # or set1 & set2

# Difference: elements in set1 but not in set2
print(set1.difference(set2))     # or set1 - set2

# Symmetric Difference: elements in either set but not both
print(set1.symmetric_difference(set2))  # or set1 ^ set2

set1.add('grape')               # Add one element
print(set1)
set1.update(['kiwi', 'lemon'])  # Add multiple elements
print(set1)
set1.remove('banana')           # Removes element, raises KeyError if not found
print(set1)
set1.discard('orange')          # Removes element if present, no error if absent
print(set1)
set1.pop()                      # Removes a random element
print(set1)
set1.clear()                    # Empties the set
print(set1)
