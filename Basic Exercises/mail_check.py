class mails():
    def __init__(self):
        with open ("mails.txt","r",encoding="UTF-8") as file:
            mails = list()
            info = list()
            for i in file:
                i = i.lstrip(" ")
                i = i.strip("\n")
                info.append(i)
            for i in info:
                index = i.find("@")
                if index != -1:
                    if i.endswith(".com"):
                        mails.append(i)
            for i in mails:
                print(i)
mail = mails()