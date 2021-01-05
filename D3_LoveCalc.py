print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
true_count = 0
love_count = 0
count1 = lower_name1.count('t')
true_count = true_count + count1
count1 = lower_name1.count('r')
true_count = true_count + count1
count1 = lower_name1.count('u')
true_count = true_count + count1
count1 = lower_name1.count('e')
true_count = true_count + count1

count1 = lower_name2.count('t')
true_count = true_count + count1
count1 = lower_name2.count('r')
true_count = true_count + count1
count1 = lower_name2.count('u')
true_count = true_count + count1
count1 = lower_name2.count('e')
true_count = true_count + count1

count2 = lower_name1.count('l')
love_count = love_count + count2
count2 = lower_name1.count('o')
love_count = love_count + count2
count2 = lower_name1.count('v')
love_count = love_count + count2
count2 = lower_name1.count('e')
love_count = love_count + count2

count2 = lower_name2.count('l')
love_count = love_count + count2
count2 = lower_name2.count('o')
love_count = love_count + count2
count2 = lower_name2.count('v')
love_count = love_count + count2
count2 = lower_name2.count('e')
love_count = love_count + count2

love_percentage = str(true_count) + str(love_count)
integer_love_percentage = int(love_percentage)

if integer_love_percentage <= 10 or integer_love_percentage >= 90:
    print("Your sccore is " + love_percentage + ", you go together like coke and mentos.")
elif integer_love_percentage >= 40 and integer_love_percentage <= 50:
    print("Your score is " + love_percentage + ", you are alright together.")
else:
    print("Your score is " + love_percentage)