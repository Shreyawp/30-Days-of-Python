# Day 12: 30 Days of python programming

# Modules -- Creating and importing package module 
# random 
# string

import random
import string

## Exercise Level 1

# declaring chars variable globally
chars = string.ascii_letters + string.digits

# 1. Write a function which generates a six digit/character random_user_id 
def random_user_id():
    print(''.join(random.choices(chars, k=6)))

random_user_id()
# >> Qu5VhN

# 2. Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is 
# the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_of_chars = int(input("Enter number of characters: "))
    num_of_ids = int(input("Enter number of IDs: "))
    
    for n in range(num_of_ids):
        print("#" + ''.join(random.choices(chars, k=num_of_chars)))

user_id_gen_by_user()
''' 
####################### OUTPUT ##########################
Enter number of characters: 5
Enter number of IDs: 5
#CDiQp
#fdNJe
#pakkt
#SxB0A
#unsK8
##########################################################
'''

# 3. Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).
from random import randint

def rgb_color_gen():
    r,g,b = randint(0,256), randint(0,256), randint(0,256)
    print(f'rgb({r},{g},{b})')

rgb_color_gen()
# >> rgb(135,20,161)

## Exercise Level 2

# 1. Write a function list_of_hexa_colors which returns any number of 
# hexadecimal colors in an array (six hexadecimal numbers written after #.
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and 
# first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

# print(string.hexdigits) -->> 0123456789abcdefABCDEF

def list_of_hexa_colors(num):
    hex_list = []
    for n in range(num):
        #hex_char = ['a','b','c','d','e','f'] + list(string.digits)
        #print("#" + ''.join(random.choices(hex_char, k=6)))
        hex_color = "#" + ''.join(random.choices(string.hexdigits, k=6))
        hex_list.append(hex_color)
    
    print(hex_list)

list_of_hexa_colors(5)
# >> ['#4f1C4B', '#59FcE8', '#68F1BE', '#8f5C43', '#A821c0']

# 2. Write a function list_of_rgb_colors which returns any number of 
# RGB colors in an array.
def list_of_rgb_colors(num):
    rgb_list = []
    for n in range(num):
        r,g,b = random.randrange(0,256), random.randrange(0,256), random.randrange(0,256)
        rgb_list.append(f'rgb({r},{g},{b})')
    print(rgb_list)

list_of_rgb_colors(3)
# >> ['rgb(40,111,144)', 'rgb(216,53,245)', 'rgb(242,206,15)']

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, num):
    if color_type == 'hexa':
        list_of_hexa_colors(num)
    elif color_type == 'rgb':
        list_of_rgb_colors(num)
    else:
        print("Invalid input! Choose color type from ['hexa', 'rgb']")

generate_colors('hexa', 3)
generate_colors('rgb', 2)
generate_colors('hjs', 1)
''' 
####################### OUTPUT ##########################
['#BFC914', '#c8D10a', '#eb45fF']
['rgb(237,103,90)', 'rgb(209,182,53)']
Invalid input! Choose color type from ['hexa', 'rgb']
##########################################################
'''

## Exercise Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter 
# and it returns a shuffled list
def shuffle_list(lst):
    random.shuffle(lst)
    print(lst)

shuffle_list([5,3,6,7,2,9])
shuffle_list(['a','o','e','u','i'])
''' 
####################### OUTPUT ##########################
[2, 7, 3, 5, 6, 9]
['e', 'u', 'o', 'i', 'a']
##########################################################
'''

# 2. Write a function which returns an array of seven random 
# numbers in a range of 0-9. All the numbers must be unique.
def array_of_7nums():
    return random.sample(range(10), k=7)

print(array_of_7nums())
# >> [9, 8, 1, 3, 7, 5, 6]

