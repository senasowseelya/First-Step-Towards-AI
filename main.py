import helper


user_input=''
while user_input != "exit":
    user_input = input("enter list comma separated:\n")
    print(user_input.split(", "))
    print(set(user_input.split(", ")))
    for list_elements in set(user_input.split(", ")):
        helper.validate_execute(list_elements)

'''
#importing single function instead of whole file
from helper import validate_execute

user_input=''
while user_input != "exit":
    user_input = input("enter list comma separated:\n")
    print(user_input.split(", "))
    print(set(user_input.split(", ")))
    for list_elements in set(user_input.split(", ")):
        validate_execute(list_elements)
'''