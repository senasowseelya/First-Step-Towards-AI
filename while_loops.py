units = 'seconds'
units_count = 24 * 60 * 60

def days_to_units(days):
        return f"{days} days are {units_count} {units}"

def validate_execute():
    try:
        days = int(user_input)
        if days>0:
            print(days_to_units(days))
        elif days==0:
            print("you have enter 0 so please check")
        else:
            print("you entered a negitive number")
    except ValueError:
        print("you have to enter a positive number")
'''while True:
    user_input = input("enter value:\n")
    validate_execute()'''
#this loop will stop until we click on stop
#while is is used when we dint know the exact number of loop to run

user_input=''
while user_input != "exit":
    user_input = input("enter value:\n")
    validate_execute()
