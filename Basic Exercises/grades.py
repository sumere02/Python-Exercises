def grade_calculator(line):
    total = float(line[1])*3/10 + float(line[2])*3/10 + float(line[3])*4/10
    if total >= 80:
        grade = 'AA'
    elif total >= 70:
        grade = 'BA'
    elif total >= 60:
        grade = 'BB'
    elif total >= 50:
        grade = 'CB'
    elif total >= 40:
        grade = 'CC'
    elif total >= 30:
        grade = 'DC'
    elif total >= 20:
        grade = 'DD'
    else:
        grade = 'FF'
    return grade
with open("info.txt","r",encoding="utf-8") as file:
    j = 0
    inf = file.readlines()
    data = list()
    grades = list()
    for i in inf:
        i = i.strip("\n")
        data.append(i.split(","))   
        grades.append(grade_calculator(data[j]))
        j += 1
        


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

with open("grades.txt","w",encoding="utf-8") as file:
    j = 0
    for i in grades:
        #print("Name: {} Grade: {}\n".format(data[j][0],i))
        file.write("Name: {} Grade: {}\n".format(data[j][0],i))
        j +=1
with open("fails.txt","w",encoding="utf-8") as file:
    j = 0
    file.write("Students who failed the exams\n")
    for i in grades:
        if i == "FF":
            file.write("Name: {}\n".format(data[j][0]))
            j += 1
with open("pass.txt","w",encoding="utf-8") as file:
    j = 0
    for i in grades:
        if i != 'FF':
            file.write("Name: {}\n".format(data[j][0]))
            j += 1