"""
class is a blueprint of object or any real world entity
class contains methods and members both
__init__ - constructir
__ -> functions start with __ are special functions
self is a keyword which gives access to current instance
"""
class User:
    def __init__(self,name,password,email):  #init is constructor which create an object, initializes props
        self.name = name
        self.password = password
        self.email = email

    def change_email(self,new_email):
        self.email = new_email

    def get_info(self):
        print(f"name - {self.name}, password- {self.password} email-{self.email}")