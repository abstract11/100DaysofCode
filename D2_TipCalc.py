print("Welcome to the tip calculator.")
amount = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? "))
per = (percent * amount) / 100
t_bill = amount + per
people = input("How many people to split the bill? ")
split = t_bill / int(people)
print(f"Each person should pay: {round(split,2)}")