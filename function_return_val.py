""" 
Functions can return value and we use return keyword for that

def send_hours():
    return 24

def send_mins():
    return 60

"""

def calc_hours(days):
    return days*24


hours = calc_hours(10)    # here we are using the value returned by a function
print(f"10 days have {hours} hours")