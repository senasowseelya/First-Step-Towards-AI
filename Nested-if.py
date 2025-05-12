# if we have if condtion inside the another if conditons is known as nested if
units = 'seconds'
units_count = 24 * 60 * 60

def days_to_units(days):
        return f"{days} days are {units_count} {units}"


user_input = input("enter value:\n")
if user_input.isdigit():
    days = int(user_input)
    if days>0:
        print(days_to_units(days))
    elif days==0:
        print("you have enter 0 so please check")
else:
    print("you have to enter a positive number")