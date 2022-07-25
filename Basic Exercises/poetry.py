class poem():
    def __init__(self):
        information = list()
        with open ("poem.txt","r",encoding="UTF-8") as file:
            for i in file:
                i = i.lstrip(" ")
                information.append(i)
            for i in information:
                print(i[0],end="")
poem_1 = poem()