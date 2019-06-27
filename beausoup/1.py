from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')
# print(y.prettify())

data = y.find('table', class_='wikitable')

# for j in data.find_all('i'):
#     print(j.text)

# for k in data.find_all('span',class_='bday dtstart published updated'):
#     print(k.text)

# for l in data.find_all('span',class_='dtend'):
#     print(l.text)


