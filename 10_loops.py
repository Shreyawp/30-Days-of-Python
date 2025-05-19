# Day 10: 30 Days of python programming

## Exercises: Level 1

# 1.Iterate 0 to 10 using for loop, do the same using while loop.
print("Using for loop:")
for x in range(11):
    print(x)

print("Using while loop: ")
x = 0
while x < 11 :
    print(x)
    x=x+1

''' 
####################### OUTPUT ##########################
Using for loop:
0
1
2
3
4
5
6
7
8
9
10

Using while loop:
0
1
2
3
4
5
6
7
8
9
10
##########################################################
'''

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
print("Using for loop:")
for y in range(10,-1,-1):
    print(y)

print("Using while loop:")
y = 10
while y >= 0:
    print(y)
    y = y-1
''' 
####################### OUTPUT ##########################
Using for loop:
10
9
8
7
6
5
4
3
2
1
0
Using while loop:
10
9
8
7
6
5
4
3
2
1
0
##########################################################
'''
# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
i = 0
while i < 7:
    print('#'*i)
    i=i+1

# Using for loop:
# for i in range(7):
#     print('#'*i)
''' 
####################### OUTPUT ##########################
#
##
###
####
#####
######
##########################################################
'''

# 3. Use nested loops to create the following:
for i in range(8):
    print('# '*8)
''' 
####################### OUTPUT ##########################
# # # # # # # # 
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
##########################################################
'''

# 4. Print the following pattern:
for i in range(11):
    print(f'{i} x {i} = {i*i}')
''' 
####################### OUTPUT ##########################
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
##########################################################
'''

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# using a for loop and print out the items.
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for s in skills:
    print(s)
''' 
####################### OUTPUT ##########################
Python
Numpy
Pandas
Django
Flask
##########################################################
'''

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2==0:
        print(i)
''' 
####################### OUTPUT ##########################
0
2
....
98
100
##########################################################
'''

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i%2!=0:
        print(i)

''' 
####################### OUTPUT ##########################
1
3
5
...
97
99
##########################################################
'''

## Exercises: Level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
s = 0
for i in range(101):
    s = s + i

print(f'The sum of all numbers is {s}')
''' 
####################### OUTPUT ##########################
The sum of all numbers is 5050
##########################################################
'''

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even = 0
odd = 0
for i in range(101):
    if i%2 == 0:
        even = even + i 
    else:
        odd = odd + i
print(f'The sum of all evens is {even}. And the sum of all odds is {odd}.')
''' 
####################### OUTPUT ##########################
The sum of all evens is 2550. And the sum of all odds is 2500.
##########################################################
'''

## Exercises: Level 3

# 1. Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries 
# containing the word land.
read_file = {}
with open("countries.py", 'r') as country_file:
    exec(country_file.read(), read_file)
country_list = read_file.get('countries')

for country in country_list:
    if 'land' in country:
        print(country)
''' 
####################### OUTPUT ##########################
Finland
Iceland
Ireland
Marshall Islands
Netherlands
New Zealand
Poland
Solomon Islands
Swaziland
Switzerland
Thailand
##########################################################
'''

# 2. This is a fruit list,  reverse the order using loop.
fruit = ['banana', 'orange', 'mango', 'lemon']
for i in range(3,-1,-1):
    print(fruit[i])
''' 
####################### OUTPUT ##########################
lemon
mango
orange
banana
##########################################################
'''

# 3. Go to the data folder and use the countries_data.py file.

with open("countries_data.py", "r", encoding="utf-8") as file:
    data = file.read()

countries_data = eval(data)
#print(countries_data[:5])

# What are the total number of languages in the data
lang = set()
for country in countries_data:
    for l in country['languages']:
        lang.add(l)
print("Total number of languages in list: ",len(lang))
# >> Total number of languages in list:  112

# Find the ten most spoken languages from the data
lang_dict = {}
for country in countries_data:
    for l in country['languages']:
        if l in lang_dict:
            lang_dict[l] += 1
        else:
            lang_dict[l] = 1

top10_lang = sorted(lang_dict.items(), key=lambda item:item[1] ,reverse=True)[:10]
print("Top 10 most Spoken languages: ")
for lang,count in top10_lang:
    print(f'{lang} : {count}')

''' 
####################### OUTPUT ##########################
Top 10 most Spoken languages:
English : 91
French : 45
Arabic : 25
Spanish : 24
Portuguese : 9
Russian : 9
Dutch : 8
German : 7
Chinese : 5
Serbian : 4
##########################################################
'''

# Find the 10 most populated countries in the world
country_pop = dict()

for country in countries_data:
    country_pop[country['name']] = country['population']

top10_populated_countries = sorted(country_pop.items(),key=lambda item:item[1], reverse=True)[:10]
print("List of top 10 populated countries in the world:")
for country,pop in top10_populated_countries:
    print(f'{country} : {pop}')
''' 
####################### OUTPUT ##########################
List of top 10 populated countries in the world:
China : 1377422166
India : 1295210000
United States of America : 323947000
Indonesia : 258705000
Brazil : 206135893
Pakistan : 194125062
Nigeria : 186988000
Bangladesh : 161006790
Russian Federation : 146599183
Japan : 126960000
##########################################################
'''