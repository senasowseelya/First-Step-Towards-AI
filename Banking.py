"""3 options:
1.deposit
2.withdraw
3.check balane

1. click>
how much deposit u want to add
and add it to total and show the balance


2.>
how much u want to withdraw
sub from total and show balance

3> just showiung balance"""

total=1000
print("Banking Options:\n 1.Deposit \n 2.Withdraw \n 3.Check Balance")
user_input=int(input("enter which option you want to experience: "))
if user_input==1:
    deposit=int(input("how much money you want to deposit:"))
    total=total+deposit
    print(f"Your current Balance after deposit: {total}")
elif user_input==2:
    withdraw = int(input("how much money you want to withdraw:"))
    total = total - withdraw
    print(f"Your current Balance after withdrawal: {total}")
elif user_input==3:
    print(f"Your current Balance: {total}")
else:
    print("you entered a invaliod number")

