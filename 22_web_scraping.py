# Day 22: 30 Days of python programming

## Web Scraping Using BeautifulSoup ##

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/datasets/'

response = requests.get(url)
print(response.status_code)
# >> 200
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
#print(soup.body)

url1 = 'https://archive.ics.uci.edu/dataset/53/iris'
resp = requests.get(url1)
print(resp.status_code)
# >> 200
#print(resp.text)
content = resp.content
soup = BeautifulSoup(content, 'html.parser')

titles = soup.find_all('title')
for t in titles:
    print(t.get_text())
''' 
####################### OUTPUT ##########################
UCI Machine Learning Repository
Iris - UCI Machine Learning Repository
##########################################################
'''

print(soup.body)
''' 
####################### OUTPUT ##########################
<body>
<div> <div class="drawer h-full"> <input aria-label="toggle drawer" class="drawer-toggle" id="daisy-ui-drawer-checkbox" type="checkbox"/> <div class="drawer-content"> <header class="navbar shadow-md"> ...
##########################################################
'''

url = 'https://en.wikipedia.org/wiki/J._K._Rowling#Bibliography'
resp = requests.get(url)
print(resp.status_code)

soup = BeautifulSoup(resp.content, 'html.parser')
#print(soup.title.get_text())

tables = soup.find_all('table')
tables.pop(0)

for table in tables:
    for td in table.find('tr').find_all('td'):
        print(td.text)
''' 
####################### OUTPUT ##########################
200

The Philosopher's Stone (1997)
The Chamber of Secrets (1998)
##########################################################
'''

## Exercise


# 3. Scrape the following website and store the data as json file
import json
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States#Presidents'
resp = requests.get(url)
#print(resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup.prettify())

table = soup.find('table', class_='wikitable sortable sticky-header')

president_data = []
for row in table.find_all('tr'):
    data = row.find_all('td')
    for d in data:
        president_data.append(d.text.strip())
    
with open('./data/us_president.json', 'w') as f:
    json.dump(president_data, f, indent=4)


