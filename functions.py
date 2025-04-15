# To remove duplicate code multiple times, we write that logic in functions and call that function multiple times


# Without functions
units = 'seconds'
units_count= 24*60*60

print(f"20 days are {20*units_count} {units}")
print(f"30 days are {30*units_count} {units}")
print(f"50 days are {50*units_count} {units}")


print(" ---using functions -----")

def days_to_units(days):
    print(f"{days} days are {units_count} {units}")

days_to_units(20)
days_to_units(30)
days_to_units(50)


# Create a function ,
# use def keyword functionName parenthesis parameters
# > def functionName(parameters separated by coma)


#Function Call
#A function will not be executed until you call it
# > functionName(parameters)