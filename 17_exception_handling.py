# Day 17: 30 Days of python programming

# Exception Handling
# packing and unpacking
# Spreading
# Enumerate
# Zip

## Exception Handling
try:
    print(10 + '5')
except:
    print('Something went wrong!')
# >> Something went wrong!

try:
    name = input('Enter your name: ') 
    year_born = input('Year you were born: ')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong!')
''' 
####################### OUTPUT ##########################
Enter your name: Jacques
Year you were born: 1983
Something went wrong!
##########################################################
'''

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
''' 
####################### OUTPUT ##########################
Enter your name:Jacques
Year you were born:1983    
Type error occured
##########################################################
'''

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('I usually run with try block')
finally:
    print('I always run!')
''' 
####################### OUTPUT ##########################
Enter your name:Jacques
Year you were born:1983    
You are Jacques. And your age is 36.
I usually run with try block
I always run!
##########################################################
'''

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
''' 
####################### OUTPUT ##########################
Enter your name:Jacques
Year you were born:1983    
unsupported operand type(s) for -: 'int' and 'str'
##########################################################
'''

## Unpacking

def sum_of_five_nums(a,b,c,d,e):
    return a+b+c+d+e

lst = [1,2,3,4,5]
# print(sum_of_five_nums(lst))    
# TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

# hence, unpacking list using (*)
print(sum_of_five_nums(*lst))
# >> 15

numbers = range(2,7)
print(list(numbers)) # [2, 3, 4, 5, 6]

args = [2,7]
# nums = range(args)  
# TypeError: 'list' object cannot be interpreted as an integer
nums = range(*args)
print(nums)         # range(2, 7)
print(list(nums))   # [2, 3, 4, 5, 6]

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)
# >> Finland Sweden Norway ['Denmark', 'Iceland']

number_tup = (1,2,3,4,5,6,7)
one, *middle, last = number_tup
print(one, middle, last)
# >> 1 [2, 3, 4, 5, 6] 7

## unpacking dictionary
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name':'Jacques', 'country':'France', 'city':'Paris', 'age':36}
print(unpacking_person_info(**dct))
# >> Jacques lives in France, Paris. He is 36 year old.

## Packing Lists
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1,2,3))               # >> 6
print(sum_all(4,8,3,7,6,9,2,4,1))   # >> 44

## Packing Dictionaries
def packing_person_info(**kwargs):
    print(type(kwargs))  
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

print(packing_person_info(name='Jacques', country='France', city='Paris', age=36))
''' 
####################### OUTPUT ##########################
<class 'dict'>
name = Jacques
country = France
city = Paris
age = 36
{'name': 'Jacques', 'country': 'France', 'city': 'Paris', 'age': 36}
##########################################################
'''

## Spreading in Python
lst_one = [1,2,3]
lst_two = [4,5,6]
lst = [0, *lst_one, *lst_two]
print(lst)
# >> [0, 1, 2, 3, 4, 5, 6]

country_one = ['Finland', 'Sweden', 'Norway']
country_two = ['Denmark', 'Iceland']
nordic_countries = [*country_one, *country_two]
print(nordic_countries)
# >> ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

## Enumerate
for index, item in enumerate([20,30,40]):
    print(index, item)
''' 
####################### OUTPUT ##########################
0 20
1 30
2 40
##########################################################
'''
for index,i in enumerate(countries):
    print(index,i)
''' 
####################### OUTPUT ##########################
0 Finland
1 Sweden
2 Norway
3 Denmark
4 Iceland
##########################################################
'''

for index,i in enumerate(countries):
    if i == 'Norway':
        print(f'The country {i} found at index {index}')
# >> The country Norway found at index 2

## Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veggies = []
for f,v in zip(fruits,vegetables):
    fruits_and_veggies.append({'fruit':f, 'veg':v})
    
print(fruits_and_veggies)
''' 
####################### OUTPUT ##########################
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, 
{'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, 
{'fruit': 'lime', 'veg': 'Carrot'}]
##########################################################
'''

## Exercise

# 1. Unpack the first five countries and store them in a variable nordic_countries, 
# store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries, es, ru)
''' 
####################### OUTPUT ##########################
['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland'] Estonia Russia
##########################################################
'''
