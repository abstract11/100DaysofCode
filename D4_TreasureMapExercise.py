# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
number = str(position)
number1 = int(number[0])
number2 = int(number[1])
map[number1 - 1][number2 - 1] = "A"
# print(map)
print(f"{row1}\n{row2}\n{row3}")