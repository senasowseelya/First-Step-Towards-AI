units_count= 24*60*60
units = 'seconds'


def days_to_units(days):
        return f"{days} days are {days * units_count} {units}"

def validate_execute(num_of_days):
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
        return "input is not an integer"


input_message ="Enter days\n"