units = 'seconds'
units_count= 24*60*60

def days_to_units(days):
    condition_check= days>0
    print(condition_check)
    print(type(condition_check))
    if days>=0:
        return f"{days} days are {units_count} {units}"
    else:
        return "you entered a negitive number"
    

user_input=input("enter value:\n")
days=int(user_input)
print(days_to_units(days))
