"""
array = ["345","sadas","324a","14","kemal"]
for i in array:
    try:
        print(int(i))
    except ValueError:
        continue
"""

def odd_even(number):
    if number % 2 == 1:
        raise ValueError
    else:
        return number
array = [i for i in range(1,20)]
for i in array:
    try:
        num = odd_even(i)
        print(num,end=" ")
    except ValueError:
        continue