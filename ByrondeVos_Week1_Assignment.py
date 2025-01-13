pet = "rock"
name = "Thurston"
print(f"I have a pet {pet} its name is {name}")

name = input("enter your name: ")
age = int(input("enter your age: "))
yearly_savings = int(input("enter your current annual savings: "))
print(f"Hello {name}! You are currently {age} years old.")
print(f"In 10 years, you will be {age + 10} years old")
print(f"if you save ${yearly_savings} each year, in 5 years you will have saved ${yearly_savings * 5}")
print(f"Your monthly savings rate is {yearly_savings / 12:.2f}.")

from datetime import datetime
import calendar
now = datetime.now()
last_day = calendar.monthrange(now.year, now.month)[1]
end_of_month = datetime(now.year, now.month, last_day, 23, 59, 59)
time_difference = end_of_month - now
seconds_left = time_difference.total_seconds()


print(f"Today is {now}")
print(f"That means you have about {seconds_left:.0f} seconds before the end of this month. Wow!")
abcs = int(input("How many seconds does it take you to say supercalifragilisticexpialidocious: "))
say = seconds_left // abcs
leftover = seconds_left % abcs
print(f"If it takes you {abcs} seconds to say the word supercalifragilisticexpialidocious and you began right now, you could say it {say} times and still have {leftover} seconds before the end of the month! Get going!")
