#functions are the blocks of code that are used to avoid same logic in the code
units = 'seconds'
units_count= 24*60*60
'''
print(f"25 days are {25*units_count} {units}")
print(f"50 days are {50*units_count} {units}")
print(f"100 days are {100*units_count} {units}")'''

#using function:-
def days_to_units(days): #we can use 2 functions at a time by using coma
    print(f"{days} days are {units_count} {units}")

#the ide is empty until we call the function so then only function can be executable
days_to_units(25) 
days_to_units(50)
days_to_units(100)

def days_to_units(days,months): #we can use 2 functions at a time by using coma
    print(f"{days} days are {units_count} {units} and {months} months")

#the ide is empty until we call the function so then only function can be executable
days_to_units(25,1) 
days_to_units(50,"3 months")
days_to_units(100,7)

