# Day 11: 30 Days of python programming

## Exercises: Level 1

# 1. Declare a function add_two_numbers. 
# It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    return a+b

print(add_two_numbers(2,6))
# >> 8

# 2. Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.
def area_of_circle(r):
    area = 3.14 * r * r
    return area

print(area_of_circle(r = 6))
# >> 113.03999999999999

# 3. Write a function called add_all_nums which takes arbitrary number 
# of arguments and sums all the arguments. 
# Check if all the list items are number types. 
# If not do give a reasonable feedback. 
def add_all_nums(*nums):
    sum = 0
    for n in nums:
        sum = sum + n
    return sum

print(add_all_nums(6,8,5,9))
# >> 28

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(cel):
    frh = (cel * 9.5) + 32
    return frh

print(convert_celsius_to_fahrenheit(30))
# >> 317.0

# 5. Write a function called check-season, it takes a month parameter 
# and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ['September', 'October', 'November']:
        print("Season is Autumn.")
    elif month in ['December', 'January', 'February']:
        print("Season is Winter.")
    elif month in ['March', 'April', 'May']:
        print("Season is Spring.")
    elif month in ['June', 'July', 'August']:
        print("Season is Summer.")
    else:
        print("Invalid Month !")

month = input('Enter Month: ')
check_season(month)

''' 
####################### OUTPUT ##########################
Season is Spring.
##########################################################
'''

# 6. Write a function called calculate_slope which return 
# the slope of a linear equation
def calculate_slope(x1,x2,y1,y2):
    m = (y2 - y1)/(x2 - x1)
    return m

print("Slope of given equation: ", calculate_slope(5,8,3,6))
''' 
####################### OUTPUT ##########################
Slope of given equation:  1.0
##########################################################
'''

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math
def solve_quadratic_eqn(a,b,c):
    d = abs((b**2)-(4*a*c))
    x1 = (-b + abs(math.sqrt(d)))/(2*a)
    x2 = (-b - abs(math.sqrt(d)))/(2*a)
    print("solve_quadratic_eqn: " ,(x1,x2))

solve_quadratic_eqn(1,1,1)
''' 
####################### OUTPUT ##########################
solve_quadratic_eqn:  (0.3660254037844386, -1.3660254037844386)
##########################################################
'''

# 8. Declare a function named print_list. It takes a list as a parameter 
# and it prints out each element of the list.
def print_list(input_list):
    for l in input_list:
        print(l)
fruits = ['apple', 'banana', 'orange', 'melon', 'berries', 'grapes']
print_list(fruits)
''' 
####################### OUTPUT ##########################
apple
banana
orange
melon
berries
grapes
##########################################################
'''

# 9. Declare a function named reverse_list. It takes an array as a parameter 
# and it returns the reverse of the array (use loops).
def reverse_list(lst):
    rev_lst = []
    for l in lst[::-1]:
        rev_lst.append(l)
    return rev_lst

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))
print(reverse_list([1,'a',50,'am','100', 100]))
''' 
####################### OUTPUT ##########################
[5, 4, 3, 2, 1]
['C', 'B', 'A']
[100, '100', 'am', 50, 'a', 1]
##########################################################
'''

# 10. Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(str_lst):
    new_lst = []
    for s in str_lst:
        new_lst.append(s.upper())
    return new_lst
print("Capitalize string items in list: ", capitalize_list_items(["data", "network", "packets", "frame", "messages"]))
''' 
####################### OUTPUT ##########################
Capitalize string items in list:  ['DATA', 'NETWORK', 'PACKETS', 'FRAME', 'MESSAGES']
##########################################################
'''

# 11. Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
def add_item(lst, item):
    if item not in lst:
        lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print("Adding item to list: ",add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print("Adding number to given list: ",add_item(numbers, 5))  
''' 
####################### OUTPUT ##########################
Adding item to list:  ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']
Adding number to given list:  [2, 3, 7, 9, 5]
##########################################################
'''

# 13. Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    sum = 0
    for n in range(num+1):
        sum = sum + n
    return sum
print(sum_of_numbers(5))  
print(sum_of_numbers(10)) 
print(sum_of_numbers(100)) 
''' 
####################### OUTPUT ##########################
15
55
5050
##########################################################
'''

# 14. Declare a function named sum_of_odds. It takes a number parameter 
# and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum = 0
    for n in range(num+1):
        if n%2 != 0:
            print(n)
            sum = sum + n
    return sum
print(sum_of_odds(5))  
print(sum_of_odds(10)) 
print(sum_of_odds(100)) 
''' 
####################### OUTPUT ##########################
9
25
2500
##########################################################
'''

# 15. Declare a function named sum_of_even. It takes a number parameter 
# and it adds all the even numbers in that range.
def sum_of_even(num):
    sum = 0
    for n in range(num+1):
        if n%2 == 0:
            sum = sum+n
    return sum

print(sum_of_even(5))  
print(sum_of_even(10)) 
print(sum_of_even(100))
''' 
####################### OUTPUT ##########################
6
30
2550
##########################################################
'''

## Exercise level 2

# 1. Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and 
# it counts number of evens and odds in the number.
def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for n in range(num+1):
        if n%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"The number of odds are {odd_count}. \nThe number of evens are {even_count}.")

evens_and_odds(100)
''' 
####################### OUTPUT ##########################
The number of odds are 50. 
The number of evens are 51.
##########################################################
'''

# 2. Call your function factorial, it takes a whole number as a parameter 
# and it return a factorial of the number
def factorial(num):
    if num == 1:
        return 1
    else:
        fact = 1
        for n in range(1,num+1):
            fact = fact*n
    return fact
print(factorial(1))
# >> 1
print(factorial(5))
# >> 120

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(para):
    if len(para) == 0:
        print("Given parameter is empty.")
    else:
        print("Given parameter is not empty.")

is_empty((''))
is_empty([])
is_empty((1,'a',50,'am','100', 100))
is_empty([1,'a',50,'am','100', 100])
''' 
####################### OUTPUT ##########################
Given parameter is empty.
Given parameter is empty.
Given parameter is not empty.
Given parameter is not empty.
##########################################################
'''

# 4. Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, 
# calculate_range, calculate_variance, calculate_std (standard deviation).
lst = [1,2,3,4,3,6,5,7,8,2,1,6,9,0,4,7,8]
n = len(lst)
def calculate_mean(lst):
    sum = 0
    for n in lst:
        sum = sum + n
    mean = sum/(n)
    return mean

print("Mean: ", calculate_mean(lst))

def calculate_median(lst):
    mid_val = int(n/2)
    if n%2 != 0:
        return lst[mid_val]
    else:
        return lst[mid_val-1],lst[mid_val]
    
print("Median: ", calculate_median(lst))

def calculate_mode(lst):
    mode = set(lst)
    return mode

print("Mode: ", calculate_mode(lst))

def calculate_range(lst):
    range = max(lst) - min(lst)
    return range

print("Range: ", calculate_range(lst))

def calculate_variance(lst, mean=calculate_mean(lst)): 
    sum = 0
    for i in lst:
        sum = sum + ((i - mean)**2)
    var = sum/(n - 1)
    return var

print("Variance: ", calculate_variance(lst))

import math
def calculate_std(lst):
    std = math.sqrt(calculate_variance(lst))
    return std

print("Standard Deviation: ",calculate_std(lst))
''' 
####################### OUTPUT ##########################
Mean:  9.5
Median:  8
Mode:  {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
Range:  9
Variance:  34.640625
Standard Deviation:  5.885628683496777
##########################################################
'''

## Exercise Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    elif num%2 == 0:
        return False
    else: 
        for i in range(3,num,2):
            if num%i == 0:
                return False
        return True
            
print(is_prime(3))
print(is_prime(5))
print(is_prime(2))
print(is_prime(33))
print(is_prime(1))
''' 
####################### OUTPUT ##########################
True
True
True
False
False
##########################################################
'''

# 2. Write a functions which checks if all items are unique in the list.
def check_list(lst):
    if lst == list(set(lst)):
        print("List has unique items!")
    else:
        print("List has NO unique items!")

check_list([1,1,1,2,5,2,3,6,5,3])
check_list([1,2,3,4])
check_list(["A",'B','B','C','A'])
''' 
####################### OUTPUT ##########################
List has NO unique items!
List has unique items!
List has NO unique items!
##########################################################
'''

# 3. Write a function which checks if all the items of the list are of the same data type.
def check_datatype(lst):
    first_item_type = type(lst[0])
    if all(type(item) == first_item_type for item in lst):
        print("Same Datatype!")
    else:
        print("Not Same Datatype!")

check_datatype([1,1,1,2,5,2,3,6,5,3])
check_datatype([["A",'B','B','C','A']])
check_datatype([1,'a',50,'am','100', 100])
''' 
####################### OUTPUT ##########################
Same Datatype!
Same Datatype!
Not Same Datatype!
##########################################################
'''
# 4. Write a function which check if provided variable is a valid python variable
import keyword
def check_python_var(var):
    if var.isidentifier() and not keyword.iskeyword(var):
        print(f"{var} is valid python variable")
    else:
        print(f"{var} is NOT valid python variable")
    
check_python_var("abc_10")
check_python_var('453')
check_python_var("_")
check_python_var("for")
''' 
####################### OUTPUT ##########################
abc_10 is valid python variable
453 is NOT valid python variable
_ is valid python variable
for is NOT valid python variable
##########################################################
'''

# 5. Go to the data folder and access the countries-data.py file.
with open("countries_data.py", "r", encoding="utf-8") as file:
    data = file.read()

countries_data = eval(data)

# Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(countries_data):
    lang_dict={}
    for country in countries_data:
        for lang in country['languages']:
            if lang in lang_dict:
                lang_dict[lang] += 1
            else:
                lang_dict[lang] = 1

    top20_lang = sorted(lang_dict.items(), key=lambda item:item[1], reverse=True)[:20]
    print("Top 20 most spoken Languages in the world:")
    for k,v in top20_lang:
        print(k,":",v)

most_spoken_languages(countries_data)
''' 
####################### OUTPUT ##########################
Top 20 most spoken Languages in the world:
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
Swahili : 4
Italian : 4
Swedish : 3
Albanian : 3
Croatian : 3
Norwegian : 3
Uzbek : 2
Turkmen : 2
Samoan : 2
Guaraní : 2
##########################################################
'''
# Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(countries_data):
    country_pop = {}
    for country in countries_data:
        country_pop[country['name']] = country['population']
    
    top20_population = sorted(country_pop.items(), key=lambda item:item[1], reverse=True)[:20]
    print("Top 20 most poplated countries in world:")
    for k,v in top20_population:
        print(k,":",v)

most_populated_countries(countries_data)
''' 
####################### OUTPUT ##########################
Top 20 most poplated countries in world:
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
Mexico : 122273473
Philippines : 103279800
Viet Nam : 92700000
Ethiopia : 92206005
Egypt : 91290000
Congo (Democratic Republic of the) : 85026000
Germany : 81770900
Iran (Islamic Republic of) : 79369900
Turkey : 78741053
France : 66710000
##########################################################
'''
