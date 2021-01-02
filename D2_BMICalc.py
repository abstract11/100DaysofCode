height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) / (float(height) * float(height))
a = str(bmi)
first = a[0]
second = a[1]
print("Your BMI is " + first + second)