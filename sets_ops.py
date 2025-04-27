""""
set removes duplicate elements in the list
set() is the function used to create a set.
set is an unordered collection of list and we cannot index it
"""


values = [1,2,3,1,2]
values_set = set(values)
print(values_set)   #{1,2,3}
#print(values_set[0])  #TypeError: 'set' object is not subscriptable  -- we cannot perform indexing on set


values_set.add(6);
print(values_set)  #{1,2,3,6}

values_set.remove(3)
print(values_set)  #{1,2,6}


