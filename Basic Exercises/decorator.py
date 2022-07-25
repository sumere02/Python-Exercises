
"""
def extra(func):
    def wrapper(numbers):
        even_total = 0
        odd_total = 0
        even_num = 0
        odd_num = 0
        for i in numbers:
            if i % 2 == 0:
                even_num += 1
                even_total += i
            else:
                odd_num += 1
                odd_total += i
        print("Even Average: {}\nOdd Average: {}\n".format(even_total/even_num,odd_total/odd_num))
        func(numbers)
    return wrapper

@extra
def find_avg(numbers):
    total = 0
    for i in numbers:
        total += i
    print("Average: ",total/len(numbers))

find_avg([1,2,3,4,5,6,7,8])
"""
"""
@decorator
def func(arg):
   return "value"

def func(arg):
   return "value"
func = decorator(func)
"""
def extra(func):
    def wrapper(numbers):
        func(numbers)
        perfect_num = list()
        for i in numbers:
            total = 0
            for j in range(1,i):
                if i % j == 0:
                    total += j
            if total == i:
                perfect_num.append(i)
        print("Perfect Numbers\n*******************")
        for i in perfect_num:
            print(i)
    return wrapper
@extra
def prime_numbers(numbers):
    flag = 1
    prime_number = list()
    for i in numbers:
        flag = 1
        for j in range(2,i):
            if(i % j == 0):
                flag = 0
                break
        if flag and i != 1:
            prime_number.append(i)
    print("Prime Numbers\n*******************")
    for i in prime_number:
        print(i)
prime_numbers(range(1,1000))