import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
html_information = response.content
parsed_information = BeautifulSoup(html_information,"html.parser")

for i in parsed_information.find_all("tbody",{"class":"lister-list"}):
    for j in i.find_all("a"):
        print(j.text,end="")