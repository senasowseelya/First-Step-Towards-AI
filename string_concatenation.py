print("There are 7 days in a week")

# print("There are "+ 7 +" days in a week")       ----- TypeError: can only concatenate str (not "int") to str

print("There are "+ str(7) +" days in a week")     # use + to concatenate strings

print(f"There are {7} days in a week")             # use f"" ,{} for string interpolation

print(f"There are {7*24} hours in a week")         # use any calculation between {}

