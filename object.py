from user import User

user1 = User("Bob","bob@123","Bob@mail.com")
user1.get_info()
user1.change_email("Bob@1127")
user1.get_info()


user2 = User("geetha","gee@123","geetha@mail.com")
user2.get_info()
user2.change_email("geetha1127@mail.com")
user2.get_info()