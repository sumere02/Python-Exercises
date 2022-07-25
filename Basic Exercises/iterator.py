def prime_num_generator(max):
    for i in range(1,max):
        flag = 1
        for j in range(2,i):
            if i % j == 0:
                flag = 0
        if flag:
            yield i
for i in prime_num_generator(1000):
    print(i)