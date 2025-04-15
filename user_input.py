# we sometimes require the user to enter input, for that python provides input() function

# input()                 # reads a value from user
# value = input()         # input function returns a string value and we are saving it in variable value. -- string
# int_value = int(input())# converted str to int


# input("enter a value")  # showing message to user


# ------------------------
units = 'seconds'
units_count= 24*60*60

def days_to_units(days):
    return f"{days} days are {units_count} {units}"

num_of_days = int(input("Enter days\n"))
return_val = days_to_units(num_of_days)
print(return_val)