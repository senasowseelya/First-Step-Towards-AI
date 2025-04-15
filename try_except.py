"""
To execute the program or block of code multiple times, we use while loop
This while loop executes if the condition is true
if condition is false, it comes out of loop

We use while loop  to execute until a condition becomes false
"""


units = 'seconds'
units_count= 24*60*60

def days_to_units(days):
        return f"{days} days are {units_count} {units}"

def validate_execute():
    try:                             # instead of if, we used try as try covers all kinds of exceptions or unknown issues
        num = int(num_of_days)
        if num > 0:
            return_val = days_to_units(int(num_of_days))
            return return_val
        elif num == 0:
            return "You entered 0, enter a valid number"
        else:
            return "You entered negative, enter a valid number"

    except ValueError:                 # if there is any error in try block, except/ catch block will be called
        print("input is not an integer")

    except:                           # catches all error, generic way
        print("An error occured")


num_of_days = input("Enter days\n")
print(validate_execute())

