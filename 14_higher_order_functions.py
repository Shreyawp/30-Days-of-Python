# Day 14: 30 Days of python programming

# Higher order functions
# decorators
# map, filter, reduce

# Functions as parameter
def sum_nums(nums):
    return sum(nums)

def higher_order_function(f, lst):
    summation = f(lst)
    return summation

result = higher_order_function(sum_nums, [1,2,3,4,5])
print(result)
# >> 15

# Function as return value
def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if x>= 0:
        return x
    else:
        return -(x)
    
def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3))
result = higher_order_function('absolute')
print(result(-3))
''' 
####################### OUTPUT ##########################
9
27
3
##########################################################
'''

# Python Closures - nested function to access outer scope of enclosing function
def add_ten():
    ten = 10
    def sum(num):
        return num+ten
    return sum

closure_result = add_ten()
print(closure_result(5))
# >> 15
print(closure_result(10))
# >> 20

# Python decorators - allows a user to add new functionality to 
# an existing object without modifying its structure

# creating decorators
def uppercase_decorator(function):
    def wrapper():
        func = function()       # greetings()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator    # calling decorator

def greetings():
    return "Welcome to Python"
print(greetings())

# Applying multiple decorators to single function
# first decorator -- uppercase_decorator

# second decorator
def split_str_decorator(function):
    def wrapper():
        func = function()
        splitted_str = func.split()
        return splitted_str
    return wrapper

# calling decorators
@split_str_decorator
@uppercase_decorator

def greet_world():
    return 'Hello World!'
print(greet_world())
# >> ['HELLO', 'WORLD!']

# decorator accepting parameters
def decor_with_params(function):
    def wrapper_accepting_params(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_params

@decor_with_params

def print_full_name(firstname, lastname, country):
    print("I am {} {}. I love to teach {}.".format(firstname, lastname, country))

print_full_name("Shreya", "Parse", "India")
''' 
####################### OUTPUT ##########################
I am Shreya Parse. I love to teach India.
I live in India
##########################################################
'''

# Python : Map function
# map(function, iterable)

## Example 1
nums = [1, 2, 3, 4, 5]
def square(x):
    return x**2
numbers_squared = map(square, nums)
print(list(numbers_squared))
# >> [1, 4, 9, 16, 25]

# map() using lambda
numbers_squared = map(lambda x:x**2, nums)
print(list(numbers_squared))
# >> [1, 4, 9, 16, 25]

## Example 2
num_str = ['1','2','3','4','5']
num_int = map(int, num_str)
print(list(num_int))
# >> [1, 2, 3, 4, 5]

## Example 3
names = ['Eric', 'Lucas', 'Jenny', 'Sophie']
def change_to_upper(name):
    return name.upper()

names_upper_case = map(change_to_upper, names)
print(list(names_upper_case))
# >> ['ERIC', 'LUCAS', 'JENNY', 'SOPHIE']

# using lambda
names_upper_case = map(lambda name: name.upper(), names)
print(list(names_upper_case))
# >> ['ERIC', 'LUCAS', 'JENNY', 'SOPHIE']

# Filter function
# filter(bool_function, iterable)

# Example 1
nums = [1, 2, 3, 4, 5]
def is_even(num):
    if num%2 == 0:
        return True
    return False

even_nums = filter(is_even, nums)
print(list(even_nums))
# >> [2, 4]

# Example 2
nums = list(range(1,10))
def is_odd(nums):
    if nums%2!=0:
        return True
    return False

odd_nums = filter(is_odd, nums)
print(list(odd_nums))
# >> [1, 3, 5, 7, 9]

# Example 3
names = ['Eric', 'Lucas', 'Jennifer', 'Sophie', 'Alexander', 'Christiana']
def is_name_long(name):
    if len(name)>7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))
# >> ['Jennifer', 'Alexander', 'Christiana']

## Reduce function 
# reduce(function, iterable) >> single_value
from functools import reduce
num_str = ['1','2','3','4','5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, num_str)
print(total)
# >> 15

# Exercise Level - 1 

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.Explain the difference between map, filter, and reduce.
# 2. Explain the difference between higher order function, closure and decorator
# 3. Define a call function before map, filter or reduce, see examples.
def upper_case(item):
    return item.upper()

def if_name_short(name):
    if len(name)<7:
        return True
    return False

def add_nums(x,y):
    return x+y

def print_list(list):
    for item in list:
        print(item)
# 4. Use for loop to print each country in the countries list.
upper_case_countries = map(upper_case, countries)
print_list(upper_case_countries)
''' 
####################### OUTPUT ##########################
ESTONIA
FINLAND
SWEDEN
DENMARK
NORWAY
ICELAND
##########################################################
'''
filter_countries = filter(if_name_short, countries)
print_list(filter_countries)
''' 
####################### OUTPUT ##########################
Sweden
Norway
##########################################################
'''

# 5. Use for to print each name in the names list.
upper_case_names = map(upper_case, names)
print_list(upper_case_names)
''' 
####################### OUTPUT ##########################
ASABENEH
LIDIYA
ERMIAS
ABRAHAM
##########################################################
'''
filter_short_names = filter(if_name_short, names)
print_list(filter_short_names)
''' 
####################### OUTPUT ##########################
Lidiya
Ermias
##########################################################
'''

# 6. Use for to print each number in the numbers list.
total_of_num_list = reduce(add_nums, numbers)
print(total_of_num_list)
# >> 55

# Exercise Level - 2

# 1. Use map to create a new list by changing each country 
# to uppercase in the countries list
upper_case_countries = map(upper_case, countries)
print(list(upper_case_countries))
# >> ['ESTONIA', 'FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']

# 2. Use map to create a new list by changing each number 
# to its square in the numbers list
def num_squares(n):
    return n**2

squared_num = map(num_squares,numbers)
print(list(squared_num))
# >> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 3. Use map to change each name to uppercase in the names list
upper_case_names = map(lambda name:name.upper(), names)
print(list(upper_case_names))
# >> ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# 4. Use filter to filter out countries containing 'land'.
def filter_land(country):
    if country.endswith('land'):
        return True
    return False

land_country = filter(filter_land, countries)
print(list(land_country))
# >> ['Finland', 'Iceland']

# 5. Use filter to filter out countries having exactly six characters.
def filter_6_char(chars):
    if len(chars) == 6:
        return True
    return False

six_char_countries = filter(filter_6_char, countries)
print(list(six_char_countries))
# >> ['Sweden', 'Norway']

# 6. Use filter to filter out countries containing six letters and 
# more in the country list.
def more_than_six(chars):
    if len(chars) >= 6:
        return True
    return False

long_char_countries = filter(more_than_six, countries)
print(list(long_char_countries))
# >> ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# 7. Use filter to filter out countries starting with an 'E'
def if_start_with_E(chars):
    if chars.startswith('E'):
        return True
    return False

country_start_with_E = filter(if_start_with_E, countries)
print(list(country_start_with_E))
# >> ['Estonia']

# 8. Chain two or more list iterators 
# (eg. arr.map(callback).filter(callback).reduce(callback))
result = reduce(lambda acc,x : acc + x,
                filter(lambda x:x%2==0,
                       map(lambda x:x**2,numbers)
                       )
                )

print("Sum of even squares: ", result)
# >> Sum of even squares:  220

result = reduce(lambda acc,x: acc+', '+x,
                filter(lambda x:x.endswith('LAND'),
                       map(lambda x:x.upper(),countries)
                       )
                )

print("Countries end with 'LAND': ", result)
# >> Countries end with 'LAND':  FINLAND, ICELAND

# 9. Declare a function called get_string_lists which takes a list 
# as a parameter and then returns a list containing only string items.
list1 = ['Asabeneh', 123, True, 'Python', 3.14, 'Hello']
def get_string_lists(list):
    if isinstance(list,str): 
        return True
    return False

is_list_str = filter(get_string_lists, list1)
print(list(is_list_str))
# >> ['Asabeneh', 'Python', 'Hello']

# 10. Use reduce to sum all the numbers in the numbers list.
sum_all_num = reduce(add_nums, numbers)
print(sum_all_num)
# >> 55

# 11. Use reduce to concatenate all the countries and to produce this sentence:
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def concat_countries(c1, c2):
    return c1+", "+c2

country_con = reduce(concat_countries, countries)
print(country_con + " are north European countries.")
# >> Estonia, Finland, Sweden, Denmark, Norway, Iceland are north European countries.

# 12. Declare a function called categorize_countries that returns 
# a list of countries with some common pattern 
# (eg 'land', 'ia', 'island', 'stan')).
read_file = {}
with open('countries.py','r') as country_file:
    exec(country_file.read(), read_file)

country_list = read_file.get('countries')

def categorize_countries(country):
    if country.endswith(('land', 'ia', 'island', 'stan')):
        return True
    return False

country_category = filter(categorize_countries, country_list)
print(list(country_category))
''' 
####################### OUTPUT ##########################
['Afghanistan', 'Albania', 'Algeria', 'Armenia', 'Australia', 'Austria', 
'Bolivia', 'Bulgaria', 'Cambodia', 'Croatia', 'Estonia', 'Ethiopia', 'Finland',
'Georgia', 'Iceland', 'India', 'Indonesia', 'Ireland', 'Kazakhstan', 
'Kyrgyzstan', 'Latvia', 'Liberia', 'Lithuania', 'Macedonia', 'Malaysia', 
'Mauritania', 'Micronesia', 'Mongolia', 'Namibia', 'New Zealand', 'Nigeria', 
'Pakistan', 'Poland', 'Romania', 'Russia', 'Saint Lucia', 'Saudi Arabia', 
'Slovakia', 'Slovenia', 'Somalia', 'Swaziland', 'Switzerland', 'Syria', 
'Tajikistan', 'Tanzania', 'Thailand', 'Tunisia', 'Turkmenistan', 'Uzbekistan',
'Zambia']
##########################################################
'''

# 13. Create a function returning a dictionary, where keys stand for starting
# letters of countries and values are the number of country names starting
# with that letter.
from functools import reduce
def country_letter_count(c_dict, country):
    first_letter = country[0]
    if first_letter in c_dict: 
        c_dict[first_letter] += 1
    else:
        c_dict[first_letter] = 1
    return c_dict

country_dict = reduce(country_letter_count, country_list, {})
print(country_dict)
''' 
####################### OUTPUT ##########################
{'A': 11, 'B': 17, 'C': 18, 'D': 4, 'E': 8, 'F': 3, 'G': 11, 'H': 3, 'I': 8, 'J': 3, 'K': 7, 
'L': 9, 'M': 18, 'N': 9, 'O': 1, 'P': 9, 'Q': 1, 'R': 3, 'S': 25, 'T': 11, 'U': 7, 'V': 4, 'Y': 1, 'Z': 2}
##########################################################
'''
#  *******************************************
# how reduce(function, iterable, initializer) works
# acc = initializer
# for item in iterable:
#     acc = function(acc, item)
# return acc

# while function defination:
# def function(acc, iterable)
#  *******************************************

# 14. Declare a get_first_ten_countries function - it returns a list of 
# first ten countries from the countries.js list in the data folder.

def get_first_ten_countries(country_list):
    print(list(map(str.title, country_list[:10])))

get_first_ten_countries(country_list)
# >> ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria']

# 15. Declare a get_last_ten_countries function that returns the 
# last ten countries in the countries list.
def get_last_ten_countries(country_list):
    print(list(map(str.title, country_list[-10:])))

get_last_ten_countries(country_list)
# >> ['United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']


## Exercise level - 3
# Use the countries_data.py file and follow the tasks below:
with open("countries_data.py", "r", encoding="utf-8") as file:
    data = file.read()

countries_data = eval(data)
#print(countries_data[:5])

# 1. Sort countries by name, by capital, by population
sort_by_country_name =  sorted(countries_data, key= lambda country:country['name'])
sorted_country_name = map(lambda c:c['name'], sort_by_country_name)
print(list(sorted_country_name))
# >> ['Afghanistan', 'Albania', 'Algeria', ... , 'Zambia', 'Zimbabwe', 'Åland Islands']

sort_by_country_capital =  sorted(countries_data, key= lambda country:country['capital'])
sorted_country_capital = map(lambda c:c['capital'], sort_by_country_capital)
print(list(sorted_country_capital))
# >> ['', '', '', '', '', 'Abu Dhabi', 'Abuja', 'Accra', ... , 'Yaren', 'Yerevan', 'Zagreb']

def population(pop_dict, country_data):
    pop_dict[country_data['name']] = country_data['population']
    return pop_dict

pop_dict = reduce(population, countries_data, {})
sort_by_country_population =  sorted(pop_dict.items(), key=lambda item:item[1])
print(sort_by_country_population)
# >> [('Bouvet Island', 0), ('Heard Island and McDonald Islands', 0), ('South Georgia and the South Sandwich Islands', 30), ... ,  ('United States of America', 323947000), ('India', 1295210000), ('China', 1377422166)]

# 2. Sort out the ten most spoken languages by location.
def language(lang_dict, country_data):
    for lang in country_data['languages']:
        if lang in lang_dict:
            lang_dict[lang] += 1
        else:
            lang_dict[lang] = 1
    return lang_dict

lang_count = reduce(language, countries_data, {})
top_10_lang = sorted(lang_count.items(), key=lambda item:item[1], reverse=True)[:10]
print(dict(top_10_lang))
''' 
####################### OUTPUT ##########################
{'English': 91, 'French': 45, 'Arabic': 25, 'Spanish': 24, 'Portuguese': 9, 'Russian': 9, 'Dutch': 8, 'German': 7, 'Chinese': 5, 'Serbian': 4}
##########################################################
'''

# 3. Sort out the ten most populated countries.
def population(pop_dict, country_data):
    pop_dict[country_data['name']] = country_data['population']
    return pop_dict

pop_dict = reduce(population, countries_data, {})
top_10_poplated_countries = sorted(pop_dict.items(), key=lambda items:items[1], reverse=True)[:10]
print(dict(top_10_poplated_countries))
''' 
####################### OUTPUT ##########################
{'China': 1377422166, 'India': 1295210000, 'United States of America': 323947000, 'Indonesia': 258705000, 'Brazil': 206135893, 'Pakistan': 194125062, 'Nigeria': 186988000, 'Bangladesh': 
161006790, 'Russian Federation': 146599183, 'Japan': 126960000}
##########################################################
'''





