"""
a,b,c = input("Enter three number: ").split()
a = float(a)
b = float(b) 
c = float(c)
if a > b:
    if a > c:
        max = a
    else:
        max = c
else:
    if b > c:
        max = b
    else:
        max = c
print("Biggest number: ",max)
"""

print("****************\n")
print("Grade Calculator\n")
print("****************\n")

print("""
    Total = Midterm 1*30/100 + Midterm 2*30/100 + Final*40/100

    Total >=  90 -----> AA

    Total >=  85 -----> BA

    Total >=  80 -----> BB

    Total >=  75 -----> CB

    Total >=  70 -----> CC

    Total >=  65 -----> DC

    Total >=  60 -----> DD

    Total >=  55 -----> FD

    Total <  55 -----> FF
""")

midterm1,midterm2,final = input("Midterm 1-Midterm 2-Final: ").split()
midterm1 = float(midterm1)
midterm2 = float(midterm2)
final = float(final)
total = midterm1*3/10+midterm2*3/10+final*4/10
if total >= 90:
    grade = 'AA'
elif total >= 85:
    grade = 'BA'
elif total >= 85:
    grade = 'BB'
elif total >= 85:
    grade = 'CB'
elif total >= 85:
    grade = 'CC'
elif total >= 85:
    grade = 'DC'
elif total >= 85:
    grade = 'DD'
else:
    grade = 'FF'
print("Grade: ",grade)
