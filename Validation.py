units = 'seconds'
units_count = 24 * 60 * 60

def days_to_units(days):
    condition_check = days > 0
    print(condition_check)
    print(type(condition_check))
    return f"{days} days are {units_count} {units}"


# we add isdigit to check the user input is number or not
user_input = input("enter value:\n")
if user_input.isdigit():
    days = int(user_input)
    print(days_to_units(days))
else:
    print("you have to enter number")