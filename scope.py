
units = 'seconds'
units_count= 24*60*60

def days_to_units(days, message):
    print(f"{days} days are {units_count} {units}")
    print(message)

def check_scope():
    print(units)  # this is global variable which is defined outside function and can be accessed anywhere
    #print(days)   # this is passed as parameter to another function so it is available only inside that function
                  # > NameError: name 'days' is not defined

    animal = "dog"
    print(animal)  # this variable is created inside function and is available only inside function


#print(animal)       # > NameError: name 'animal' is not defined
check_scope()
