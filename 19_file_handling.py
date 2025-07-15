# Day 19: 30 Days of python programming

# File Handling
"""
f = open('./example_file.txt', 'w')
print(f)
# >> <_io.TextIOWrapper name='./example_file.txt' mode='w' encoding='cp1252'>

f.write('This is an example to show how to open a file and read.\nThis is the second line of the text.')

f = open('./example_file.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
''' 
####################### OUTPUT ##########################
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
##########################################################
'''
f = open('./example_file.txt')
first_10_letters = f.read(10)
print(first_10_letters)
f.close()
# >> This is an

f = open('./example_file.txt')
line = f.readline()
print(type(line))
print(line)
''' 
####################### OUTPUT ##########################
<class 'str'>
This is an example to show how to open a file and read.
##########################################################
'''
f = open('./example_file.txt')
lines = f.readlines()
print(type(lines))
# >> <class 'list'>
print(lines)
# >> ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']

f = open('./example_file.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines) 
f.close()
''' 
####################### OUTPUT ##########################
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
##########################################################
'''

# using 'with' keyword, closes file itself
with open('./example_file.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
''' 
####################### OUTPUT ##########################
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
##########################################################
'''

# Opening files to update/append
with open('./example_file.txt', 'a') as f:
    f.write('This text has to be appended at the end')
  
with open('./example_file.txt') as f:
    lines = f.read().splitlines()
    print(lines)
''' 
####################### OUTPUT ##########################
['This is an example to show how to open a file and read.', 'This is the second line of the text.This text has to be appended at the end']
##########################################################
'''

# Opening files to write, this will overwrite the lines
with open('./example_file.txt', 'w') as f:
    f.write('This text will be written in newly created file')

with open('./example_file.txt') as f:
    lines = f.read().splitlines()
    print(lines)
''' 
####################### OUTPUT ##########################
['This text will be written in newly created file']
##########################################################
'''

# Deleting files
import os
if os.path.exists('./example_file.txt'):
    os.remove('./example_file.txt')
else:
    print('File dont exist !!')

# File with .json(javascript object notation)
import json
person_json = '''{
                "name":"Jackson",
               "country":"China",
               "city":"Beijing",
               "skills":["Javascript", "React", "Python"]
               }'''

person_dict = json.loads(person_json)
print(type(person_dict))
print(person_dict)
print(person_dict['name'])
''' 
####################### OUTPUT ##########################
<class 'dict'>
{'name': 'Jackson', 'country': 'China', 'city': 'Beijing', 'skills': ['Javascript', 'React', 'Python']}
Jackson
##########################################################
'''

## dictionary to json
person = {
    "name":"Jackson",
    "country":"China",
    "city":"Beijing",
    "skills":["Javascript", "React", "Python"]
}

person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)
''' 
####################### OUTPUT ##########################
<class 'str'>
{
    "name": "Jackson",
    "country": "China",
    "city": "Beijing",
    "skills": [
        "Javascript",
        "React",
        "Python"
    ]
}
##########################################################
'''

with open('./json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

f = open('./json_example.json', 'r')   
lines = f.read()
print(lines)
f.close()
''' 
####################### OUTPUT ##########################
{
    "name": "Jackson",
    "country": "China",
    "city": "Beijing",
    "skills": [
        "Javascript",
        "React",
        "Python"
    ]
}
##########################################################
'''

# .csv file
import csv

with open('./csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are : {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}.')
            line_count += 1
        print(f'Number of lines: {line_count}')

''' 
####################### OUTPUT ##########################
Column names are : name, country, city, skills
Number of lines: 1
        Asabeneh is a teacher. He lives in Finland, Helsinki.
Number of lines: 2
##########################################################
'''

import xml.etree.ElementTree as ET
tree = ET.parse('./xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute: ', root.attrib)
for child in root:
    print('Field: ', child.tag)

''' 
####################### OUTPUT ##########################
Root tag: person
Attribute:  {'gender': 'female'}
Field:  name
Field:  country
Field:  city
Field:  skills
##########################################################
'''

# Exercise 

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
import os
def count_lines_and_words(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        words = " ".join(lines).split()
        print(f"Number of lines in {os.path.basename(file_path)}: ", len(lines))
        print(f"Number of words in {os.path.basename(file_path)}:", len(words))

count_lines_and_words('./data/obama_speech.txt')
count_lines_and_words('./data/michelle_obama_speech.txt')
count_lines_and_words('./data/donald_speech.txt')
count_lines_and_words('./data/melina_trump_speech.txt')
''' 
####################### OUTPUT ##########################
Number of lines in obama_speech.txt:  66
Number of words in obama_speech.txt: 2400
Number of lines in michelle_obama_speech.txt:  83
Number of words in michelle_obama_speech.txt: 2204
Number of lines in donald_speech.txt:  48
Number of words in donald_speech.txt: 1259
Number of lines in melina_trump_speech.txt:  33
Number of words in melina_trump_speech.txt: 1375
##########################################################
'''

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json

def most_spoken_lang(filename, n):
    with open(filename , 'r', encoding='utf-8') as f:
        countries_data = json.load(f)

    lang_dict = {}
    for country in countries_data:
        for lang in country['languages']:
            if lang in lang_dict:
                lang_dict[lang] += 1
            else:
                lang_dict[lang] = 1
    print(sorted(lang_dict.items(), key=lambda item:item[1], reverse=True)[:n])

most_spoken_lang('./data/countries_data.json', 3)
most_spoken_lang('./data/countries_data.json', 10)
''' 
####################### OUTPUT ##########################
[('English', 91), ('French', 45), ('Arabic', 25)]
[('English', 91), ('French', 45), ('Arabic', 25), ('Spanish', 24), ('Portuguese', 9), ('Russian', 9), ('Dutch', 8), ('German', 7), ('Chinese', 5), ('Serbian', 4)]
##########################################################
'''

# 3. create a function that creates a list of the ten most populated countries
def most_populated_countries(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        countries_data = json.load(f)

    country_pop = []
    for country in countries_data:
        country_pop_dict = {'country':country['name'], 'population':country['population']}
        country_pop.append(country_pop_dict)
    return sorted(country_pop, key=lambda x:x['population'], reverse=True)[:n]

print(most_populated_countries('./data/countries_data.json', 3))
print(most_populated_countries('./data/countries_data.json', 10))
''' 
####################### OUTPUT ##########################
[{'country': 'China', 'population': 1377422166}, {'country': 'India', 'population': 1295210000}, {'country': 'United States of America', 'population': 323947000}]
[{'country': 'China', 'population': 1377422166}, {'country': 'India', 'population': 1295210000}, {'country': 'United States of America', 'population': 323947000}, {'country': 'Indonesia', 'population': 258705000}, {'country': 'Brazil', 'population': 206135893}, {'country': 'Pakistan', 'population': 194125062}, {'country': 'Nigeria', 'population': 186988000}, {'country': 'Bangladesh', 'population': 161006790}, {'country': 'Russian Federation', 'population': 146599183}, {'country': 'Japan', 'population': 126960000}]
##########################################################
'''

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re

with open('./data/email_exchanges_big.txt') as f:
    text = f.read()
    #print(re.findall(r'From [A-Za-z0-9/s]*@[A-Za-z0-9]*.[A-Za-z0-9]*', text))

# 5. Find the most common words in the English language. Call the name of your function find_most_common_words
def find_most_common_words(file_name, n):
    word_dict = {}
    with open(file_name) as f:
        text = f.read()
    
    for words in text.split():
        if words in word_dict:
            word_dict[words] += 1
        else:
            word_dict[words] = 1
    return sorted(word_dict.items(), key=lambda x:x[1], reverse=True)[:n]

print(find_most_common_words('./data/romeo_and_juliet.txt', 10))
# >> [('the', 762), ('I', 549), ('and', 539), ('to', 522), ('of', 485), ('a', 453), ('in', 330), ('is', 322), ('my', 310), ('with', 274)]

# 6. Use the function, find_most_frequent_words to find: 

def find_most_frequent_words(filename, n):
    with open(filename) as f:
        text = f.read()
    
    word_dict ={}
    for words in text.split():
        if words in word_dict:
            word_dict[words] += 1
        else:
            word_dict[words] = 1
    return sorted(word_dict.items(), key=lambda x:x[1], reverse=True)[:n]

files = ['./data/obama_speech.txt', './data/michelle_obama_speech.txt', './data/donald_speech.txt', './data/melina_trump_speech.txt']
for f in files:
    print(f"The most frequent words in {os.path.basename(f)}: ", find_most_frequent_words(f,5))
''' 
####################### OUTPUT ##########################
The most frequent words in obama_speech.txt:  [('the', 120), ('and', 107), ('of', 81), ('to', 66), ('our', 58)]
The most frequent words in michelle_obama_speech.txt:  [('to', 83), ('and', 80), ('the', 78), ('of', 46), ('â€”', 41)]
The most frequent words in donald_speech.txt:  [('the', 61), ('and', 53), ('will', 40), ('of', 38), ('to', 32)]
The most frequent words in melina_trump_speech.txt:  [('and', 73), ('to', 54), ('the', 48), ('I', 28), ('is', 28)]
##########################################################
'''


# 7. 

# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
print(find_most_common_words('./data/romeo_and_juliet.txt', 5))
# >> [('the', 762), ('I', 549), ('and', 539), ('to', 522), ('of', 485)]

"""
# 9. Read the hacker news csv file and find out: 
import csv
import re

def count_number_of_rows_pattern_match(pattern):
    with open('./data/hacker_news.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        count = 0
        for row in csv_reader:
            text = " ".join(row)
            if re.search(rf'\b{pattern}\b', text, re.I):
                count += 1
        return count

print(f"Rows containing 'python': ", count_number_of_rows_pattern_match('python'))
print(f"Rows containing 'javascript': ", count_number_of_rows_pattern_match('javascript'))
print(f"Rows containing 'java': ", count_number_of_rows_pattern_match('java'))
''' 
####################### OUTPUT ##########################
Rows containing 'python':  162
Rows containing 'javascript':  183
Rows containing 'java':  59
##########################################################
'''




