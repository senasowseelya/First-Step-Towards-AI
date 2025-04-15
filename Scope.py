#global scope -> variable avaliable from within any scope
#local scope -> variable created inside the function
#functions are the blocks of code that are used to avoid same logic in the code
units = 'seconds'
units_count= 24*60*60

def days_to_units(days):
    print(f"{days} days are {units_count} {units}")

def scope_check():
    print(units) # it is executable as the units are globally assigned
    print(days) # it shows error as the days are the locally asigned to the above function so we cant use them in present function

days_to_units(25) 
days_to_units(50)
days_to_units(100)

scope_check()