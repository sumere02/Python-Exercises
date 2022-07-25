"""
array = [(3,4),(10,3),(5,6),(1,9)]

array = map(lambda x : x[0]*x[1],array)
    
print(list(array))
def triangle_check(triangle):
    if triangle[2] - triangle[1] < triangle[0] and triangle[2] + triangle[1] > triangle[0]:
        if triangle[2] - triangle[0] < triangle[1] and triangle[2] + triangle[0] > triangle[1]:
            if triangle[0] - triangle[1] < triangle[2] and triangle[0] + triangle[1] > triangle[2]:
                return True
    else:
        return False

array = [(3,4,5),(6,8,10),(3,10,7)]
array = filter(triangle_check,array)
print(list(array))
from functools import reduce
def odd_even(number):
    if number % 2 == 0:
        return True
    return False
array = range(1,11)
array = list(filter(odd_even,array))
array = reduce(lambda x,y : x + y,array)
print(array)
"""
"""
names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames = ["Yılmaz","Öztürk","Dğdeviren","Atatürk","Dikmen","Kaya","Polat"]
for name,surname in zip(names,surnames):
    print(name,surname)
"""