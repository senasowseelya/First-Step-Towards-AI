def add():
    return num1 + num2


def sub():
    return num1 - num2


def perform_operation():
    if user == "add":
        print(add())
    else:
        print(sub())


num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2st number:"))
user = input("enter you need to add or sub:/n")

perform_operation()



