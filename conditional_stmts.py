units = 'seconds'
units_count= 24*60*60

def days_to_units(days):
    if days>0:
        return f"{days} days are {units_count} {units}"
    elif days ==0:
        return "You entered 0, enter a valid number"
    else:
        return "You entered negative, enter a valid number"

num_of_days = int(input("Enter days\n"))
return_val = days_to_units(num_of_days)
print(return_val)