limit = int(input("Number: "))
total = 1
for i in range(2,limit+1):
    total *= i
print("{}! = {}\n".format(limit,total))

fib_1 = 1
fib_2 = 1

for i in range(1,limit+1):
    if(i > 2):
        """
        temp = fib_2
        fib_2 = fib_1 + fib_2
        fib_1 = temp
        """
        fib_1,fib_2 = fib_2,fib_1+fib_2
        print("{} ".format(fib_2),end="")
    else:
        print("{} ".format(fib_2),end="")