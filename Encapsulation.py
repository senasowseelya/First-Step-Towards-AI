#Hiding the internal details of an object and shows only necessary data is known as encapsulation

units = 'seconds'
units_count = 24 * 60 * 60

def days_to_units(days):
    condition_check = days > 0
    print(condition_check)
    print(type(condition_check))
    return f"{days} days are {units_count} {units}"

def validate_user():
    if user_input.isdigit():
        days = int(user_input)
        print(days_to_units(days))
    else:
        print("you have to enter number")
#here the data is wrapped in the function this is known as encapsulation

# we add isdigit to check the user input is number or not
user_input = input("enter value:\n")
validate_user()
