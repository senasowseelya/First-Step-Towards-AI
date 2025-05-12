"""
key- value pairs where  we access the element using key
dictionay = {"keyname": value,"key2": value}
dictionary["keyname1"]
if key is not found it gives key error
"""

def days_to_units(days,units):
        if units == "hours":
            return  f"{days} days are {24*days} {units}"
        elif units == "minutes":
            return f"{days} days are {24*60*days} {units}"
        else:
            return f"{days} days are {24 * 60 * 60 * days} seconds"

def validate_execute(num_unit_dict):
    try:
        num = int(num_unit_dict["days"])
        if num > 0:
            return_val = days_to_units(int(num_unit_dict["days"]),num_unit_dict["units"])  # here we are accessing the dictionary just dict["key"]
            return return_val
        elif num == 0:
            return "You entered 0, enter a valid number"
        else:
            return "You entered negative, enter a valid number"

    except ValueError:                 # if there is any error in try block, except/ catch block will be called
        return "input is not an integer"


num_of_days = input("Enter days: units\n")
num_units = num_of_days.split(":")
num_unit_dictionary = {"days":num_units[0], "units": num_units[1]}
print("this is a dictionary",num_unit_dictionary)
print(num_unit_dictionary["days"])
print(num_unit_dictionary["units"])
#print(num_unit_dictionary["daysssss"])  #KeyError: 'daysssss'

print(validate_execute(num_unit_dictionary))


