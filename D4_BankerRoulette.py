import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

string_length = len(names)
random_name = random.randint(0, string_length - 1)
print(f"{names[random_name]} is going to buy the Meal today!")