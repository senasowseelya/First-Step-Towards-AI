def display_options():
    print("Banking Options:\n 1.Deposit \n 2.Withdraw \n 3.Check Balance")
    global user_input
    user_input=input("enter which option you want to experience: ")


def deposit():
    deposit_val = int(input("how much money you want to deposit:"))
    global total
    total = total + deposit_val
    check_balance()


def withdraw():
    withdraw_val = int(input("how much money you want to withdraw:"))
    global total
    total = total - withdraw_val
    check_balance()


def check_balance():
    print(f"Your current Balance: {total}")


total=1000
user_input=0
display_options()
while user_input!="exit":
    if user_input=="1":
        deposit()
    elif user_input=="2":
        withdraw()
    elif user_input=="3":
        check_balance()
    else:
        print("you entered a invalid number")
    display_options()


