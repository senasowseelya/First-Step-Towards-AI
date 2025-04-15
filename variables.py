# instead of repeating the value multiple times, we can stire that value in a variable and use it.

print(f"20 days are {20*24*60*60} seconds")
print(f"30 days are {30*24*60*60} seconds")
print(f"50 days are {50*24*60*60} seconds")


# ----------using variables-------------
units = 'seconds'
units_count= 24*60*60

print(f"20 days are {20*units_count} {units}")
print(f"30 days are {30*units_count} {units}")
print(f"50 days are {50*units_count} {units}")


