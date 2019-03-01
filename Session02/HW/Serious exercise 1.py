weight = input("Enter your weight (kg):\n")
height = input("Enter your height (cm):\n")
heightNumber = float(height) / 100
weightNumber = float(weight)
BMI =  float(weightNumber / (heightNumber * heightNumber))
print("BMI: " + str(BMI))
if BMI < 16:
    print("You are severely underweight")
elif 16 <= BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI <25:
    print("You are normal")
elif 25 <= BMI < 30:
    print("You are overweight")
else:
    print("You are obese")