import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com"

response = requests.get(url)

html_information = response.content

parsed = BeautifulSoup(html_information,"html.parser")

list_currency = list()
list_currency_name = list()

currency = parsed.find_all("span",{"class":"value"})
currency_name = parsed.find_all("span",{"class":"name"})

for i in currency:
    list_currency.append(i.text.replace("$","").replace(",","."))
for i in currency_name:
    list_currency_name.append(i.text)
 
print("""*********************************
Operations:
1)Stock Market:
2)EUR ---> TL
3)TL ---> EUR
4)USD ---> TL
5)TL ---> USD
6)EUR ---> USD
7)USD ---> EUR
8)EXIT 
*********************************""")
while True:
    c = int(input("Operation: "))
    if c == 8:
        print("Goodbye")
        break
    else:
        if c == 1:
            for i,j in zip(list_currency_name,list_currency):
                print(i," : ",j)
        elif c == 2:
            amount = float(input("Amount: "))
            print("{} EUR = {} TL\n".format(amount,amount*float(list_currency[2])))
        elif c == 3:
            amount = float(input("Amount: "))
            print("{} TL = {} EUR\n".format(amount,amount/float(list_currency[2])))
        elif c == 4:
            amount = float(input("Amount: "))
            print("{} USD = {} TL\n".format(amount,amount*float(list_currency[1])))
        elif c == 5:
            amount = float(input("Amount: "))
            print("{} EUR = {} TL\n".format(amount,amount/float(list_currency[2])))
        elif c == 6:
            amount = float(input("Amount: "))
            print("{} EUR = {} USD\n".format(amount,amount*(float(list_currency[2])/float(list_currency[1]))))
        elif c == 7:
            amount = float(input("Amount: "))
            print("{} USD = {} EUR\n".format(amount,amount*(float(list_currency[1])/float(list_currency[2]))))
        else:
            print("Invalid Operation")   