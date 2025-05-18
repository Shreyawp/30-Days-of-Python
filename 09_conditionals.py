# Day 4: 30 Days of python programming

## Exercises: Level 1

# 1.Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.
age = int(input("Enter your age: "))
if age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need {18-age} more years to learn to drive.')
''' 
####################### OUTPUT ##########################
Enter your age: 18
You are old enough to drive.
Enter your age: 5
You need 13 more years to learn to drive.
##########################################################
'''

# 2. Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the 
# age as input. You can use a nested condition to print 'year' 
# for 1 year difference in age, 'years' for bigger differences, and 
# a custom text if my_age = your_age.
my_age = 27
your_age = int(input("Enter your age: "))
year = abs(my_age - your_age)
if year == 1:
    print(f"You are {year} younger than me.")
elif year > 0:
    print(f'You are {year} older than me.')
else: 
    print("We are same age !")
''' 
####################### OUTPUT ##########################
Enter your age: 26
You are 1 younger than me.

Enter your age: 30
You are 3 older than me.

Enter your age: 27
We are same age !
##########################################################
'''

# 3. Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, 
# else a is equal to b.
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a>b:
    print(f'{a} is greater than {b}')
elif a<b:
    print(f'{a} is smaller than {b}')
else:
    print("a is equal to b")
''' 
####################### OUTPUT ##########################
Enter number one: 5
Enter number two: 4
5 is greater than 4

Enter number one: 3
Enter number two: 6
3 is smaller than 6

Enter number one: 3
Enter number two: 3
a is equal to b
##########################################################
'''

## Exercises: Level 2

# 1. Write a code which gives grade to students according to theirs scores:
score = int(input("Enter Score: "))
if score in range(80,101):
    print("Grade : A")
elif score in range(70,80):
    print("Grade : B")
elif score in range(60,70):
    print("Grade : C")
elif score in range(50,60):
    print("Grade : D")
elif score in range(0,50):
    print("Grade : F")
else: 
    print("Invalid Score")
''' 
####################### OUTPUT ##########################
Enter Score: 20
Grade : F

Enter Score: 101
Invalid Score

Enter Score: 89
Grade : A
##########################################################
'''

# 2. Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring 
# June, July or August, the season is Summer
month = input("Enter month: ")
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
''' 
####################### OUTPUT ##########################
Enter month: May
Season is Spring.

Enter month: October
Season is Autumn.

Enter month: June
Season is Summer.

Enter month: December
Season is Winter.

Enter month: ghdcjkj
Invalid Month !
##########################################################
'''

# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list 
# and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruit = input("Enter Fruit: ")
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print("That fruit already exist in the list")
''' 
####################### OUTPUT ##########################
Enter Fruit: mango
That fruit already exist in the list
Enter Fruit: apple
['banana', 'orange', 'mango', 'lemon', 'apple']
##########################################################
'''

## Exercises: Level 3

# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
    'street': 'Space street',
    'zipcode': '02210'
        }
}

# 1. Check if the person dictionary has skills key, 
# if so print out the middle skill in the skills list.
if person['skills']:
    mid = int(len(person['skills'])/2)
    print(person['skills'][mid])
## >> Node

# 2. Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result.
if person['skills']:
    if 'Python' in person['skills']:
        print("Python is given person's skill.")
## >> Python is given person's skill.

# 3. If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
skill_set = set(person['skills'])
print(skill_set)
if skill_set == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(skill_set):
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'}.issubset(skill_set):
    print('He is a fullstack developer')
else:
    print('unknown title')
''' 
####################### OUTPUT ##########################
He is a backend developer
##########################################################
'''
# 4. If the person is married and if he lives in Finland, 
# print the information in the following format:
if person['is_marred'] == True:
    if person['country'] == 'Finland':
        print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
''' 
####################### OUTPUT ##########################
Asabeneh Yetayeh lives in Finland.He is married.
##########################################################
'''