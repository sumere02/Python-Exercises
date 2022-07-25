import requests
from bs4 import BeautifulSoup
import sys

url = "http://data.fixer.io/api/latest?access_key=b824f9280e65cb54543613435fc8770e"
response = requests.get(url)
html_information = response.json()
try:
    first_currency = input("First Currency: ")
    first_eur = html_information["rates"][first_currency]
    second_currency = input("Second Currency: ")
    second_eur = html_information["rates"][second_currency]
except KeyError:
    sys.stderr.write("Invalid Currency")
    sys.stderr.flush()
    sys.exit()
amount = float(input("Amount: "))
result = amount * second_eur/first_eur
print(amount,first_currency,"=",result,second_currency)