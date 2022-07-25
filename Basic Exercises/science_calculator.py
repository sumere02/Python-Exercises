from math import ceil,comb,copysign,fabs,factorial,floor,gcd,lcm,exp,log10,log
from sys import exit

print("""*******************
Calculator Program

Operations:

 1 - Addition
 2 - Subtraction
 3 - Multiplication
 4 - Division
 5 - GCD
 6 - LCM 
 7 - Combination
 8 - Sign
 9 - Absoulute Value
10 - Factorial
11 - Floor
12 - Ceil
13 - Exponential
14 - Log10
15 - Ln 
16 - Exit

*******************""")

num_1 = 0
while True:
    try:
        operate = int(input("Operation: "))
        if operate == 16:
            print("Goodbye")
            break
        elif operate < 8:
            if(num_1 == 0):
                while True:
                    try:
                        num_1 = float(input("Number 1: "))
                        break
                    except ValueError:
                        print("Unvalid Number")
            while True:
                try:
                    num_2 = float(input("Number 2: "))
                    break
                except ValueError:
                    print("Unvalid Number")        
            if operate == 1:
                num_1 = num_1 + num_2
                print("Result: ",num_1)
            elif operate == 2:
                num_1 = num_1 - num_2
                print("Result: ",num_1)            
            elif operate == 3:
                num_1 = num_1 * num_2
                print("Result: ",num_1)
            elif operate == 4:
                num_1 = num_1 / num_2
                print("Result: ",num_1)
            elif operate == 5:
                num_1 = int(num_1)
                num_2 = int(num_2)
                num_1 = gcd(num_1,num_2)
                print("Result: ",num_1)
            elif operate == 6:
                num_1 = int(num_1)
                num_2 = int(num_2)
                num_1 = lcm(num_1,num_2)
                print("Result: ",num_1)
            elif operate == 7:
                num_1 = int(num_1)
                num_2 = int(num_2)
                num_1 = comb(num_1,num_2)
                print("Result: ",num_1)
        elif operate < 16:
            if(num_1 == 0):
                while True:
                    try:
                        num_1 = float(input("Number 1: "))
                        break
                    except ValueError:
                        print("Unvalid Number")
            num = num_1
            if operate == 8:
                num = int(num)
                num = copysign(num)
                print("Result: ",num)
            elif operate == 9:
                num = fabs(num)
                print("Result: ",num)
            elif operate == 10:
                num = int(num_1)
                num = factorial(num)
                print("Result: ",num)
            elif operate == 11:
                num = floor(num)
                print("Result: ",num)
            elif operate == 12:
                num = ceil(num)
                print("Result: ",num)
            elif operate == 13:
                num = exp(num)
                print("Result: ",num)
            elif operate == 14:
                num = log10(num)
                print("Result: ",num)
            elif operate == 15:
                num = log(num)
                print("Result: ",num)
        else:
            pass
        while True:
            try:
                c = input("E - Exit: ")
                if c == 'E':
                    exit()
                else:
                    break
            except ValueError:
                print("Unvalid Entry")
    except ValueError:
        print("Please enter a valid operation")