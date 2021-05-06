# BMI Calculator 
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = (float(weight) / (float(height)**2))

wholeNum_BMI = int(BMI)
print("Your BMI is: " + str(wholeNum_BMI))

if BMI <18.5:
  print("Your BMI is underweight")
elif BMI >= 18.5 and BMI <=24.9:
  print("Your BMI is normal")
elif BMI >= 25 and BMI <= 29.9:
  print("Your BMI is overweight")
else:
  print("Your BMI is obese")

