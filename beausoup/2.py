from bs4 import BeautifulSoup
import requests
import csv

url = 'https://wikimon.net/Visual_List_of_Digimon'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')

file = open('dataDigimon.csv','w')

# for i in y.find_all('table'):
#     j= i.find('a')
#     print(j.get('title'))

for i in y.find_all('img'):
    file.write(i.get('alt') + ',http://wikimon.net' + i.get('src'))
    file.write('\n')

