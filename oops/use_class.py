from user import User

user1 = User("sena","test123","sena@mail.com")
user1.get_info()
user1.change_email("sena_dev@mail.com")
user1.get_info()


user2 = User("sowseelya","sow123","sowseelya@mail.com")
user2.get_info()
user2.change_email("sowseelya_dev@mail.com")
user2.get_info()