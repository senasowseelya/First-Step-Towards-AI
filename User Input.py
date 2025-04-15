units = 'seconds'
units_count= 24*60*60

def days_to_units(days):
    print(f"{days} days are {units_count} {units}")

user_input=input("enter value:\n")
days=int(user_input)
days_to_units(days)

# \n works as next line

# we convert str into int as:-
# number=int(input())
# eg:- number=int(6) or we can convert into string as:- string=string(6)
