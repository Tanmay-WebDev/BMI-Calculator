# BMI Calculator
height = float(input("Enter Your Height : "))
weight = float(input("Enter Your weight : "))

BMI = weight / (height/100)**2

print("Your BMI is : ", BMI)

if BMI <= 18.4:
    print("You are Underweight")
elif BMI <= 24.9:
    print("You are Healthy")
elif BMI <= 29.9:
    print("You are Over Weight")
elif BMI <= 34.9:
    print("You are Severely Over Weight")
elif BMI <= 39.9:
    print("You are Obese")
else:
    print("You are Severely Obese")