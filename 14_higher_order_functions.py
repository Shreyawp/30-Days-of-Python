# Day 14: Higher order functions

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




