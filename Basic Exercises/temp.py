"""
print("Multiplator\n")
try:
    a,b,c = input("A-B-C: ").split("-")
    a = int(a)
    b = int(b)
    c = int(c)
    print(a*b*c)
except ValueError:
    print("Please Enter seperator correctly")
"""
"""
print("BMI Calculator\n")

weight,height = input("Weight(in kg),Height(in m): ").split(",")
weight = float(weight)
height = float(height)
print("BMI: {}\n".format(weight/(height**2)))
"""
"""
print("Fuel Cost Calculator\n")
length = float(input("KM: "))
per_fuel = float(input("Fuel Per Km: "))
print("Cost: {}$\n".format(length*per_fuel))
"""
"""
print("Information Saver\n")
name,surname,tel = input("Name Surname Tel No: ").split()
print("Saving Data\n")
print("Name: {}\nSurname: {}\nTel No: {}\n".format(name,surname,tel))
print("Data saved successfully\n")
"""
print("Number Exchanger")
a = int(input("Number 1: "))
b = int(input("Number 2: "))
a,b = b,a
print("A: {}\nB: {}\n".format(a,b))
print("Hypothenus Calculator")
hypothenus = (a**2 + b**2)**0.5
print("Hypothenus: ",hypothenus)