from triangle import pisagor
triangle = list()
for i in range(1,101):
    for j in range(1,101):
        k = pisagor(i,j)
        if k == int(k):
            triangle.append((i,j,int(k)))
for i in triangle:
    print(i,end="\n")

