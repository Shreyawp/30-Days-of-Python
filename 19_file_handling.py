# Day 19: 30 Days of python programming

# File Handling

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





# 1.

''' 
####################### OUTPUT ##########################

##########################################################
'''
