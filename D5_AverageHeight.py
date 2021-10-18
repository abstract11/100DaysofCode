student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0
n = 0

for student in student_heights:
    n = n + 1

for number in student_heights:
    sum = sum + number
average = sum / n
avg = round(average)
print (avg)

