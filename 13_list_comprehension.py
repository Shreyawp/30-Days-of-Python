# Day 13: List comprehension
"""
language = 'Python For All'
# lst = list(language)
lst = [i for i in language]
print(lst)
print(type(lst))

# >> ['P', 'y', 't', 'h', 'o', 'n', ' ', 'F', 'o', 'r', ' ', 'A', 'l', 'l']
# >> <class 'list'>

# generate list of numbers 
nums = [i for i in range(11)]
print(nums)
# >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# math ops 
squares = [i*i for i in range(11)]
print(squares)
# >> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# make list of tuples
num_and_squares = [(i, i*i) for i in range(6)]
print(num_and_squares)
# >> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# list comp combined with if expressions
evens = [i for i in range(21) if i%2==0]
print(evens)
# >> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

odds = [i for i in range(21) if i%2 != 0]
print(odds)
# >> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_num = [i for i in numbers if i%2 == 0 and i>0]
print(positive_even_num)
# >> [4, 6, 8, 10]

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for row in list_of_lists for num in row]
print(flattened_list)
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# lambda function
add_2_nums = lambda a,b : a+b
print(add_2_nums(2,3))
# >> 5

# self-invoking
print((lambda a,b: a+b)(2,3))
# >> 5

square = lambda x : x**2
print(square(3))
# >> 9

cube = lambda x : x**3
print(cube(3))
# >> 27

mul_vars = lambda a,b,c : a**2 - 3*b + 4*c
print(mul_vars(2,8,6))
# >> 4

# lambda function inside another function
def power(x):
    return lambda n: x**n

cube = power(2)(3)
print(cube)
# >> 8
two_power_of_five = power(2)(5)
print(two_power_of_five)
# >> 32
"""
## Exercise

# 1.  Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero_nums = [i for i in numbers if i < 0 or i == 0]
print(negative_zero_nums)
# >> [-4, -3, -2, -1, 0]

# 2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [i for row in list_of_lists for i in row[0]]
print(flatten)
# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Using list comprehension create the following list of tuples:
list_of_tup = [(i, 1, i, i**2, i**3, i**4, i**5, i**6) for i in range(11)]
print(list_of_tup)
''' 
####################### OUTPUT ##########################
[(0, 1, 0, 0, 0, 0, 0, 0), 
(1, 1, 1, 1, 1, 1, 1, 1), 
(2, 1, 2, 4, 8, 16, 32, 64), 
(3, 1, 3, 9, 27, 81, 243, 729), 
(4, 1, 4, 16, 64, 256, 1024, 4096), 
(5, 1, 5, 25, 125, 625, 3125, 15625), 
(6, 1, 6, 36, 216, 1296, 7776, 46656), 
(7, 1, 7, 49, 343, 2401, 16807, 117649), 
(8, 1, 8, 64, 512, 4096, 32768, 262144), 
(9, 1, 9, 81, 729, 6561, 59049, 531441), 
(10, 1, 10, 100, 1000, 10000, 100000, 1000000)]
##########################################################
'''

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries = [[country.upper(), country.upper()[:3],city.upper()] for row in countries for country,city in row]
print(flatten_countries)
# >> [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']] 

# 5. Change the following list to a list of dictionaries:
dict_of_countries = [{'country': country.upper(), 'city': city.upper()}
                     for row in countries for country,city in row]
print(dict_of_countries)
''' 
####################### OUTPUT ##########################
[{'country': 'FINLAND', 'city': 'HELSINKI'}, 
{'country': 'SWEDEN', 'city': 'STOCKHOLM'}, 
{'country': 'NORWAY', 'city': 'OSLO'}]
##########################################################
'''

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name = [first+" "+last for row in names for first,last in row]
print(full_name)
# >> ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
# y = mx + c 
slope = lambda x,y: y/x
print(slope(2,6))
# >> 3.0


