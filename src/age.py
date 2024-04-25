from datetime import datetime


birthday_year = input("In what year were you born? ")
current_year = datetime.today().year
age = current_year - int(birthday_year)

print(f"You're {age} years old")