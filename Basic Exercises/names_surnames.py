
name = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surname = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
list_new = list(zip(name,surname))
list_new.sort()
for i,j in list_new:
    name_surname = i + " " + j
    print(name_surname)