# pip3 install beautifulsoup4

from bs4 import BeautifulSoup

# from html text
# web = '<p>Hello guys!</p>'
# x= BeautifulSoup(web, 'html.parser')        #html.parser = default


#from html file
web = open('0.html','r')
x= BeautifulSoup(web, 'html.parser')

# print(x)
# print(x.prettify()) 
# print(x.p.text)                               #.p.text = print text inside <p></p>
# print(x.p)                                      #<p id="p1">Test 1 2 3</p>
# print(x.p.name)                                 #hasil = p
# print(x.p.text)                                 #test 1 2 3
# print(x.p.string)                               #test 1 2 3
# print(x.title)                                  #<title>Web Scraping</title>
# print(x.title.name)                             # hasilnya = title    
# print(x.title.text)                             #hasil = Web scraping
# print(x.title.string)                           #Web scraping


# print(x.find_all('p'))                          #find all <p> print horizontal           
# for i in x.find_all('li'):                      #find all text inside tag <li>
#     print(i.text)                                   

# for i in x.find(id='p1'):                       #find tag id = p1
#     print(i)

# for i in x.find(class_='p2'):                     #find class_ p2. WITH UNDERSCORE_  
#     print(i)

# for i in x.find_all(class_='p2'):                 #find all class p2
#     print(i)

# for i in x.find_all('p', class_='p2'):            #find all tag<p> with class p2
#     print(i)

data = x.ol
for i in data.find_all('li'):
    print(i.text)