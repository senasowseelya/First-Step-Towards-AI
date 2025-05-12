my_list = ['bob', 'cat', 'elephant']
print(my_list)

print(my_list[0])  # indexing starts at 0

# Add an element to the end
my_list.append('pig')
print("After append:", my_list)

# Insert at a specific index
my_list.insert(1, 'dog')  # insert 'dog' at index 1
print("After insert:", my_list)

# Remove a specific element
my_list.remove('cat')  # removes the first occurrence of 'cat'
print("After remove:", my_list)

# Pop an element (by default, last item)
popped = my_list.pop()
print("After pop:", my_list)
print("Popped element:", popped)

# Count how many times an element appears
print("Count of 'bob':", my_list.count('bob'))

# Reverse the list
my_list.reverse()
print("After reverse:", my_list)

# Sort the list
my_list.sort()
print("After sort:", my_list)

# Copy the list
new_list = my_list.copy()
print("Copied list:", new_list)

# Clear the list
my_list.clear()
print("After clear:", my_list)

#single comment
'''multiple comments'''