import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))
computer = random.randint(0,2)



if(player == 0):
    if(computer == 2):
        print("You entered\n" + rock)
        print("Computer entered\n" + scissors)
        print("You Won!")
    elif(computer == 1):
        print("You entered\n" + rock)
        print("Computer entered\n" + paper)
        print("You Lose")
    else:
        print("You entered\n" + rock)
        print("Computer entered\n" + rock)
        print("It is a Tie")
elif(player == 1):
    if(computer == 0):
        print("You entered\n" + paper)
        print("Computer entered\n" + rock)
        print("You Won!")
    elif(computer == 2):
        print("You entered\n" + paper)
        print("Computer entered\n" + scissors)
        print("You Lose")
    else:
        print("You entered\n" + paper)
        print("Computer entered\n" + paper)
        print("It is a Tie")
elif(player == 2):
    if(computer == 1):
        print("You entered\n" + scissors)
        print("Computer entered\n" + paper)
        print("You Won!")
    elif(computer == 0):
        print("You entered\n" + scissors)
        print("Computer entered\n" + rock)
        print("You Lose")
    else:
        print("You entered\n" + scissors)
        print("Computer entered\n" + scissors)
        print("It is a Tie")

