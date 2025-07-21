'''
> pip --version
pip 23.0.1 from C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\site-packages\pip (python 3.10)

>>> import numpy
>>> numpy.version
<module 'numpy.version' from 'C:\\Users\\Admin\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages\\numpy\\version.py'>
>>> numpy.version.version
'2.2.6'
>>> lst = [1, 2, 3,4,5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr) 
5
>>> np_arr*2    
array([ 2,  4,  6,  8, 10])
>>> np_arr+2    
array([3, 4, 5, 6, 7])
'''

import webbrowser
url_list = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

for url in url_list:
    webbrowser.open_new_tab(url)


## List of Packages installed:
'''
> pip list
Package         Version
--------------- -----------
numpy           2.2.6
pandas          2.3.1
python-dateutil 2.9.0.post0
pytz            2025.2
six             1.17.0
tzdata          2025.2
'''

## Show package info
'''
> pip show pandas
Name: pandas
Version: 2.3.1
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page:
Author:
Author-email: The Pandas Development Team <pandas-dev@python.org>
License: BSD 3-Clause License
.....
Requires: numpy, python-dateutil, pytz, tzdata
'''

# For additional info
'''
> pip show --verbose pandas    
Name: pandas
Version: 2.3.1
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page:
Author:
Author-email: The Pandas Development Team <pandas-dev@python.org>
License: BSD 3-Clause License
Requires: numpy, python-dateutil, pytz, tzdata
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
'''

# pip freeze -- Generate installed Python packages with their version and the output is suitable to use it in a requirements file.
'''
> pip freeze
numpy==2.2.6
pandas==2.3.1
python-dateutil==2.9.0.post0
pytz==2025.2
six==1.17.0
tzdata==2025.2
'''

import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)
print(response) 
# >> <Response [404]>
print(response.status_code)
# >> 404
print(response.headers)
# >> {'Date': 'Thu, 17 Jul 2025 18:21:22 GMT', 'Content-Type': 'text/html; charset=iso-8859-1', 'Transfer-Encoding': 'chunked',...}
print(response.text)
''' 
####################### OUTPUT ##########################
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
  <title>Error 404 - Not found</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
##########################################################
'''

url = 'https://restcountries.com/v3.1/all?fields=name,capital,region'
response = requests.get(url)
print(response)
print(response.status_code)

#print(response.text)
countries= response.json()
print(countries)
''' 
####################### OUTPUT ##########################
<Response [200]>
200
[{"name":{"common":"Moldova","official":"Republic of Moldova","nativeName":{"ron":{"official":"Republica Moldova","common":"Moldova"}}},"capital":["Chișinău"],"region":"Europe"},..
##########################################################
'''

## Creating and importing arithmetic and greet from mypackage

'''
>>> from mypackage import arithmetic
>>> arithmetic.add_num(1,2,3,4)
10
>>> arithmetic.subtract(5,3)
2
>>> arithmetic.multiply(5,3)
15
>>> arithmetic.dividion(5,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'mypackage.arithmetic' has no attribute 'dividion'. Did you mean: 'division'?
>>> arithmetic.division(5,3) 
1.6666666666666667
>>> arithmetic.remainder(5,3)
2
>>> arithmetic.power(2,5)
32
>>>
>>> from mypackage import greet
>>> greet.greet_person('Shreya', 'Parse')
'Shreya Parse, welcome to 30 days of Python challenge'
>>>
'''

## Exercise 

# 1. Read this url and find the 10 most frequent words. 
romeo_and_juliet_url = 'http://www.gutenberg.org/files/1112/1112-0.txt' 
resp = requests.get(romeo_and_juliet_url)
print(resp.status_code)

romeo_and_juliet = resp.text
words_dict = {}
for word in romeo_and_juliet.lower().split():
    words_dict[word] = words_dict.get(word, 0) + 1

top_10_most_frequent_words = sorted(words_dict.items(), key=lambda item:item[1], reverse=True)[:10]
print(top_10_most_frequent_words)
''' 
####################### OUTPUT ##########################
200
[('and', 690), ('the', 660), ('i', 567), ('to', 546), ('a', 471), ('of', 382), ('my', 374), 
('that', 329), ('is', 327), ('in', 305)]
##########################################################
'''



# 2. Read the cats API and find :
import requests
cats_api = 'https://api.thecatapi.com/v1/breeds'
resp = requests.get(cats_api)
#print(resp.status_code)
cats = resp.json()
# >> 200


# a) the min, max, mean, median, standard deviation of cats' weight in metric units.
import statistics
def cat_weight_stats(cats):
    weights = [(cat['weight']['metric']).split(' - ') for cat in cats]

    weights_list = []
    for lst in weights:
        for i in lst:
            weights_list.append(int(i))
    
    n = len(weights_list)
    median_index = int(n/2)
    mean = sum(weights_list)/n
    median = sorted(weights_list)[median_index]
    print("Minimum of cat's weight(in metric): ", min(weights_list))
    print("Maximum of cat's weight(in metric): ", max(weights_list))
    print("Mean of cat's weight(in metric): %.2f" %mean)
    print("Median of cat's weight(in metric): ", median)
    print("Standard Deviation of cat's weight(in metric): %.2f" %statistics.stdev(weights_list))

cat_weight_stats(cats)
''' 
####################### OUTPUT ##########################
Minimum of cat's weight(in metric):  2
Maximum of cat's weight(in metric):  11
Mean of cat's weight(in metric): 4.71
Median of cat's weight(in metric):  5
Standard Deviation of cat's weight(in metric): 1.90
##########################################################
'''

# b) the min, max, mean, median, standard deviation of cats' lifespan in years.

def cats_lifespan(cats):
    lifespan = [cat['life_span'].split(' - ') for cat in cats]
    
    lifespan_list = []
    for lst in lifespan:
        for i in lst:
            lifespan_list.append(int(i))

    lifespan_list = sorted(lifespan_list)
    print("Minimum of cat's weight(in metric): ", min(lifespan_list))
    print("Maximum of cat's weight(in metric): ", max(lifespan_list))
    print("Mean of cat's weight(in metric): %.2f" %statistics.mean(lifespan_list))
    print("Median of cat's weight(in metric): %d" %statistics.median(lifespan_list))
    print("Standard Deviation of cat's weight(in metric): %.2f" %statistics.stdev(lifespan_list))


cats_lifespan(cats)
''' 
####################### OUTPUT ##########################
Minimum of cat's weight(in metric):  8
Maximum of cat's weight(in metric):  20
Mean of cat's weight(in metric): 13.75
Median of cat's weight(in metric): 14
Standard Deviation of cat's weight(in metric): 2.41
##########################################################
'''

# c) Create a frequency table of country and breed of cats

def cats_frequency_table(cats):
    country = {}
    for cat in cats:
        country[cat['origin']] = country.get(cat['origin'], 0) + 1
        
    return sorted(country.items(), key=lambda item:item[0], reverse=True)

print((cats_frequency_table(cats))) 
''' 
####################### OUTPUT ##########################
[('United States', 28), ('United Kingdom', 8), ('United Arab Emirates', 1), 
('Turkey', 2), ('Thailand', 4), ('Somalia', 1), ('Singapore', 1), 
('Russia', 4), ('Norway', 1), ('Japan', 1), ('Isle of Man', 1), 
('Iran (Persia)', 1), ('Greece', 1), ('France', 2), ('Egypt', 3), 
('Cyprus', 1), ('China', 1), ('Canada', 3), ('Burma', 2), ('Australia', 1)]
##########################################################
'''

# 3. Read the countries API and find
country_api = 'https://restcountries.com/v3.1/all?fields=name,languages,population'
resp = requests.get(country_api)
#print(resp.status_code)
country_data = resp.json()

# 3.a) the 10 largest countries
def top_10_largest_country(data):
    country_population = {}
    for country in data:
        name = country['name']['common']
        population = country.get('population', 0)
        country_population[name] = population

    return sorted(country_population.items(), key=lambda items:items[1], reverse=True)[:10]
    
print(top_10_largest_country(country_data))
''' 
####################### OUTPUT ##########################
[('China', 1402112000), ('India', 1380004385), ('United States', 329484123), ('Indonesia', 273523621), ('Pakistan', 220892331), ('Brazil', 212559409), ('Nigeria', 206139587), ('Bangladesh', 164689383), ('Russia', 144104080), ('Mexico', 128932753)]
##########################################################
'''

# 3.b) the 10 most spoken languages
def languages(data):
    lang_dict = {}
    for country in data:
        for k,itm in country['languages'].items():
            lang_dict[itm] = lang_dict.get(itm,0) + 1 
    return sorted(lang_dict.items(), key=lambda items:items[1], reverse=True)

top_10_lang = languages(country_data)[:10]        
print(top_10_lang)
''' 
####################### OUTPUT ##########################
[('English', 91), ('French', 46), ('Arabic', 25), ('Spanish', 24), ('Portuguese', 10), ('Russian', 7), ('Dutch', 7), ('German', 6), ('Chinese', 5), ('Tswana', 4)]
##########################################################
'''

# 3.c) the total number of languages in the countries API
total_langs = len(languages(country_data))
print("Total number of languages in the countries API: ", total_langs)
# >> Total number of languages in the countries API:  155


