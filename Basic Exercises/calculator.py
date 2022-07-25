print("""*******************
Calculator Program

Operations:

1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Exit

*******************""")

flag = 1
operation = int(input("Choose Operation: "))
if operation != 5:
    num_1 = float(input("Number 1: "))
while operation != 5:
    num_2 = float(input("Number 2: "))
    if operation == 1:
        num_1 = num_1+num_2
    elif operation == 2:
        num_1 = num_1 - num_2
    elif operation == 3:
        num_1 = num_1 * num_2
    elif operation == 4:
        num_1 = num_1 / num_2
    else:
        flag = 0
        print("Please enter correct operation\n")
    if flag:
        print("Result: {}".format(num_1))
    while(1):
        key = input("Do you want to continue(y or n): ")
        if key == 'y':
            flag = 1
            operation = int(input("Choose Operation: "))
            break
        elif key == 'n':
            operation = 5
            break
        else:
            print("Please enter correct key character\n")
