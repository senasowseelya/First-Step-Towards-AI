# import helper  # import whole module  --1
#from helper import *  --2
from helper import  validate_execute, input_message

num_of_days = ''
while num_of_days != "exit":
    num_of_days = input(input_message)
   #  print(helper.validate_execute(num_of_days))  # when importing whole module, user module name.  --1
    print(validate_execute(num_of_days))           # when using from module function name or *

