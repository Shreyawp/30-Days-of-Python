# Day 3: 30 Days of python programming

# Declaring Variables
my_age = 27
_my_height = 5.0
complex_var = 5+6j
print("my age: ", my_age ,
      "\nMy height:", _my_height, 
      "\ncomplex var: ", complex_var
      )
print("#" * 50)
''' 
####################### OUTPUT ##########################
my age:  27 
My height: 5.0
complex var:  (5+6j)
##################################################
'''
# 4. area of triangle
print("Calculate area of triangle")
base = int(input("ENter Base: "))
height = int(input("ENter Height: "))
print("Area of triangle: ", 0.5*base*height)
print("#" * 50)
''' 
####################### OUTPUT ##########################
Calculate area of triangle
ENter Base: 6
ENter Height: 4
Area of triangle:  12.0
##################################################
'''
# 5. perimeter of triangle
print("Calculate perimeter of triangle")
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
print("Perimeter of triangle = ", a+b+c)
print("#" * 50)
''' 
####################### OUTPUT ##########################
Calculate perimeter of triangle
Enter side a: 4  
Enter side b: 3
Enter side c: 9
Perimeter of triangle =  16
##################################################
'''
# 6. area and perimeter of rectangle
print("Calculate area and perimeter of rectangle")
length = int(input("Enter length: "))
width = int(input("ENter Width: "))
print("Area of rectangle: ", length*width,
      "\nPerimeter of rectangle: ", 2*(length+width))
print("#" * 50)
''' 
####################### OUTPUT ##########################
Calculate area and perimeter of rectangle
Enter length: 5
ENter Width: 9
Area of rectangle:  45 
Perimeter of rectangle:  28
##################################################
'''
# 7. Area and Circumference of Circle
print("Calculate Area and Circumference of Circle")
rad = int(input("ENter radius: "))
print("Area of circle: ", 3.14*rad*rad,
      "\nCircumfernece: ", 2*3.14*rad)
print("#" * 50)
''' 
####################### OUTPUT ##########################
Calculate Area and Circumference of Circle
ENter radius: 7
Area of circle:  153.86 
Circumfernece:  43.96
##################################################
'''
#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("Calculate the slope, x-intercept and y-intercept for: \ny = 2x - 2")
# Given equation: y = 2x - 2
m1 = 2
# y-intercept with x=0
x=0
y_intercept = m1*x-2
# x-intercept with y=0
y=0
x_intercept = (y+2)/m1
print("Slope: ", m1,
      "\ny_intercept: ", y_intercept,
      "\nx_intercept: ", x_intercept
      )
print("#" * 50)
''' 
####################### OUTPUT ##########################
Calculate the slope, x-intercept and y-intercept for:
y = 2x - 2
Slope:  2
y_intercept:  -2
x_intercept:  1.0
##################################################
'''
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and
#  Euclidean distance between point (2, 2) and point (6,10)
(x1,y1) = (2,2)
(x2,y2) = (6,10)
y_diff = y2-y1
x_diff = x2-x1
m2 = y_diff/x_diff
eud_dist = (y_diff**2)+(x_diff**2)
print("Slope: ", m2,
      "\nEuclidean Distance: ", eud_dist)
print("#" * 50)
''' 
####################### OUTPUT ##########################
Slope:  2.0
Euclidean Distance:  80
##################################################
'''
# 10. Compare the slopes in tasks 8 and 9.
print("Is Slope of task 8 equal to task 9: ", m1==m2)
print("#" * 50)
''' 
####################### OUTPUT ##########################
Is Slope of task 8 equal to task 9:  True
##################################################
'''
# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values 
# and figure out at what x value y is going to be 0.
for x in range(-10,10):
    y = (x**2) + (6*x) + 9
    if y == 0:
        print("For equation, y = x^2 + 6x + 9\ny = 0, at x = ", x )

print("#" * 50)
''' 
####################### OUTPUT ##########################
For equation, y = x^2 + 6x + 9
y = 0, at x =  -3
##################################################
'''
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
if len('python') != len('dragon'):
    print("length of string 'python' is not equal than 'dragon'")
else:
    print("length of string 'python' is equal than 'dragon'")
print("#" * 50)
''' 
####################### OUTPUT ##########################
length of string 'python' is equal than 'dragon'
##################################################
'''
# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
if ('on' in 'python') and ('on' in 'dragon'):
    print("'on' is present in strings 'python' and 'dragon'")
else:
    print("'on' is not present in strings 'python' and 'dragon'")
print("#" * 50)
''' 
####################### OUTPUT ##########################
'on' is present in strings 'python' and 'dragon'
##################################################
'''
# 14. Use in operator to check if jargon is in given sentence.
str1 = "I hope this course is not full of jargon."
if 'jargon' in str1:
    print("jargon is in given sentence")
else:
    print("jargon is not in given sentence")
print("#" * 50)
''' 
####################### OUTPUT ##########################
jargon is in given sentence
##################################################
'''
# 15. There is no 'on' in both dragon and python
if 'on' not in ('dragon','python'):
    print(False)
else:
    print(True)
print("#" * 50)
''' 
####################### OUTPUT ##########################
False
##################################################
'''
# 16. Find the length of the text python 
# and convert the value to float and convert it to string
s = 'python'
len_s = len(s)
print("length of string 'python'", len_s,
      "\nits float value: ", float(len_s),
      "\nString: ", str(len_s))
print("#" * 50)
''' 
####################### OUTPUT ##########################
length of string 'python' 6
its float value:  6.0
String:  6
##################################################
'''
# 17. Even numbers are divisible by 2 and the remainder is zero.
# How do you check if a number is even or not using python?
for num in range(1,5):
    if (num/2) and (num%2==0):
        print(num," is even number")
    else:
        print(num," is odd number")
print("#" * 50)
''' 
####################### OUTPUT ##########################
1  is odd number
2  is even number
3  is odd number
4  is even number
##################################################
'''
# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
if (7//3) == int(2.7):
    print(True)
print("#" * 50)
''' 
####################### OUTPUT ##########################
True
##################################################
'''
# 19. Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print(True)
else: 
    print(False)
print("#" * 50)
''' 
####################### OUTPUT ##########################
False
##################################################
'''
# 20. Check if int('9.8') is equal to 10
if int('9.8') == 10:
    print(True)
else:
    print(False)
print("#" * 50)
''' 
####################### OUTPUT ##########################
ValueError: invalid literal for int() with base 10: '9.8'
##################################################
'''
# 21. Write a script that prompts the user to enter hours and rate per hour. 
# Calculate pay of the person?
hour = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hour * rate_per_hour
print("Your weekly earning is ", weekly_earning)
print("#" * 50)
''' 
####################### OUTPUT ##########################
Enter hours: 40
Enter rate per hour: 30
Your weekly earning is  1200
##################################################
'''
# 22. Write a script that prompts the user to enter number of years. 
# Calculate the number of seconds a person can live. 
# Assume a person can live hundred years
num_of_years = int(input("Enter number of years you have lived: "))
year_in_secs = num_of_years*365*360*24
print(f"You have lived for {year_in_secs} seconds.")
print("#" * 50)
''' 
####################### OUTPUT ##########################
Enter number of years you have lived: 27
You have lived for 85147200 seconds.
##################################################
'''
# 23. Write a Python script that displays the following table
for i in range(1,6):
    c = i
    d = i**2
    e = i**3
    print(i, 1, c, d, e)
    
print("#" * 50)
''' 
####################### OUTPUT ##########################
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
##################################################
'''