units = 'seconds'
units_count = 24 * 60 * 60

def days_to_units(days):
        return f"{days} days are {units_count} {units}"

def validate_execute(list_elements):
    try:
        days = int(list_elements)
        if days>0:
            print(days_to_units(days))
        elif days==0:
            print("you have enter 0 so please check")
        else:
            print("you entered a negitive number")
    except ValueError:
        print("you have to enter a positive number")


