
print("""**********

BMI Calculator

**********

BMI = Weight / (Height * Height)

BMI < 18.5 -> Zayıf

BMI >= 18.5  && BMI < 25 -> Normal

BMI >= 25 && BMI < 30 -> Overweight

BMI >= 30 -> Obesite

**********""")
weight = float(input("Weight(in kg): "))
height = float(input("Height(in m): "))
bmi = weight/(height ** 2)
if bmi < 18.5:
    print("Zayıf")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesite")
