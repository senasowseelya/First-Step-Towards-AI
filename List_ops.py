


units = 'seconds'
units_count= 24*60*60

def days_to_units(days):
        return f"{days} days are {units_count*days} {units}"

def validate_execute(days):
    try:                             # instead of if, we used try as try covers all kinds of exceptions or unknown issues
        num = int(days)
        if num > 0:
            return_val = days_to_units(num)
            return return_val
        elif num == 0:
            return "You entered 0, enter a valid number"
        else:
            return "You entered negative, enter a valid number"

    except ValueError:                 # if there is any error in try block, except/ catch block will be called
        return "input is not an integer"


num_of_days = ''
while num_of_days != "exit":
    num_of_days = input("Enter coma seperated values for days\n")  #Here we are asking user for input as coma seperated values
    days = num_of_days.split(",")  #spliting the input based on coma and split returns a list
    for i in days:                 #iterating through list
        print(validate_execute(i))

