print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the tresure.")
question1 = input("You're at a cross road. Where do you want to go? " + 'Type "left" or "right"\n')
lower_question1 = question1.lower()
if lower_question1 == "left":
    question2 = input("Do you want to swim across and save your life or you want to wait on the island? " + 'Type "swim" or "wait"\n')
    lower_question2 = question2.lower()
    if lower_question2 == "wait":
        question3 = input("Ohh!! There is are 3 colourful doors one of these will take you to your destiny. Choose one! " + 'Type "red" or "yellow" or "blue"\n')
        lower_question3 = question3.lower()
        if lower_question3 == "yellow":
            print("Oh what now! Did you just win the game!!!")
        else:
            print("Game Over! Wrong choice")
    else:
        print("Game Over! Wrong choice")
else:
    print("You fell into a hole. Game over")
