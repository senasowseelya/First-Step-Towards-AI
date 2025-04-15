units = 'seconds'
units_count= 24*60*60

def days_to_units(days):
        return f"{days} days are {units_count} {units}"

def validate_execute():
    if num_of_days.isdigit():               #if input is digit, convert the number into int and check
        num = int(num_of_days)
        if num > 0:
            return_val = days_to_units(int(num_of_days))
            print(return_val)
        elif num == 0:
            return "You entered 0, enter a valid number"
        else:
            return "You entered negative, enter a valid number"
    else:                                    #if input is not a valid digit, show error to user
        print("input is not an integer")


num_of_days = input("Enter days\n")
# before we call the actual function, we validate the input
# and if input is valid, then we execute the function
validate_execute()

