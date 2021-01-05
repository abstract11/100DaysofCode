height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) / (float(height) * float(height))
rounded_bmi = round(bmi, 1)
integer_bmi = int(rounded_bmi)
if rounded_bmi >= 18.5:
    if rounded_bmi <= 25:
        print(f"Your BMI is {integer_bmi}, you have normal weight")
    elif rounded_bmi <= 30:
        print(f"Your BMI is {integer_bmi}, you are overweight")
    elif rounded_bmi <= 35:
        print(f"Your BMI is {integer_bmi}, you are obese")
    else:
        print(f"Your BMI is {integer_bmi}, you are integer_bmiliniinteger_bmially obese")
else:
    print(f"Your BMI is {integer_bmi}, you are underweight")