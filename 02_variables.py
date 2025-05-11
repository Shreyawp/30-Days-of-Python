# Day 2: 30 Days of python programming

first_name = "Shreya"
last_name = "Parse"
full_name = "Shreya Vasudev Parse"
country = "India"
city = 'Pune'
age = 27
year = 2025
is_married = 'No'
is_true = False
is_light_on = True

pet, flower, DOB, color = "Shih Tzu", "Lily of Valley", 22-5-1998, 'Purple' 

print(first_name, type(first_name))
print(len(first_name))
print(last_name, type(last_name))
print(len(last_name))

print(age, type(age))
print(is_true, type(is_true))

print("len of first greater last name: ", len(first_name)  > len(last_name))
print('*' * 50)
''' 
####################### OUTPUT ##########################
Shreya <class 'str'>
6
Parse <class 'str'>
5
27 <class 'int'>
False <class 'bool'>
len of first greater last name:  True
**************************************************
'''
num_one = 5 
num_two = 4
print("num_one : ", num_one, 'num_two : ', num_two)

total = num_one + num_two
print("total : ", total)
diff = num_two - num_one
print("differnece : ", diff)
product = num_one * num_two
print("product : ", product)
division = num_one/num_two
print("Division: ", division)
remainder = num_two%num_one
print("Remainder : ", remainder)
exp = num_one * num_two
print("Exponent: ", exp)
floor_div = num_one//num_two
print("Floor division : ", floor_div)
print('*' * 50)
''' 
####################### OUTPUT ##########################
num_one :  5 num_two :  4
total :  9
differnece :  -1
product :  20
Division:  1.25
Remainder :  4
Exponent:  20
Floor division :  1
**************************************************
'''
radius = 30
print("Radius = ", radius)
area_of_circle = 3.14*(radius**2)
print("Area of Circle = ", area_of_circle)

circum_of_circle = 2*3.14*radius
print("Circumference of circle : ", circum_of_circle)

r = int(input("radius = "))
print("Area = ", 3.14*(r**2))
print('*' * 50)
''' 
####################### OUTPUT ##########################
Radius =  30
Area of Circle =  2826.0
Circumference of circle :  188.4
radius = 10
Area =  314.0
**************************************************
'''
f_name = input("Enter First name: ")
l_name = input("Enter Last name: ")
country = input("Enter Country: ")
age =  input("Enter age: ")

print(f_name, l_name, country, age)

help('keywords')
''' 
####################### OUTPUT ##########################
Enter First name: SHreya
Enter Last name: Parse
Enter Country: India
Enter age: 27
SHreya Parse India 27

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
'''