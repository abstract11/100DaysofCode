student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

x = 0
for highest in student_scores:
    if x <= highest:
        x = highest
print(f"The highest score in the class is: {x}")

