from datetime import datetime

user_input = input("Enter goal: date in date.month.year format\n")
input_as_list=  user_input.split(":")
goal = input_as_list[0]
date_entered = input_as_list[1]

goal_date = datetime.strptime(date_entered,"%d.%m.%Y")
today = datetime.today()
remaining = goal_date - today

print(f"{remaining.days} remaining to hit the goal {goal}")
