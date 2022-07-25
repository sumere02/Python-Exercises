with open("players.txt","r",encoding="utf-8") as file:
    with open("gs.txt","w",encoding="utf-8") as file_gs:
        with open("fb.txt","w",encoding="utf-8") as file_fb:
            with open("bjk.txt","w",encoding="utf-8") as file_bjk:
                array = list()
                for i in file:
                    i = i[:-1]
                    array.append(i.split(","))
                for i in array:
                    if(i[1] == "Galatasaray"):
                        file_gs.write(i[0] + "\n")
                    elif i[1] == "Fenerbahçe":
                        file_fb.write(i[0]+ "\n")
                    else:
                        file_bjk.write(i[0]+"\n")
            
