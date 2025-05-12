# Day 4: 30 Days of python programming

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to 
# a single string, 'Thirty Days Of Python'.
print('Thirty ' + 'Days '+ 'of ' + 'Python')
''' 
####################### OUTPUT ##########################
Thirty Days of Python
'''

# 2. Concatenate the string 'Coding', 'For' , 'All' to
# a single string, 'Coding For All'.
print("Coding " + "For " + "All")
''' 
####################### OUTPUT ##########################
Coding For All
'''

# 3. Declare a variable named company and 
# assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)
''' 
####################### OUTPUT ##########################
Coding For All
'''

# 5. Print the length of the company string using len() method and print().
print("length: ", len(company))
''' 
####################### OUTPUT ##########################
length:  14
'''

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())
''' 
####################### OUTPUT ##########################
CODING FOR ALL
'''

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())
''' 
####################### OUTPUT ##########################
coding for all
'''

# 8. Use capitalize(), title(), swapcase() methods 
# to format the value of the string Coding For All.
print("Capitalize: ", "Coding For All".capitalize())
print("Title: ", 'Coding For All'.title())
print("Swapcase: ", 'Coding For All'.swapcase())
''' 
####################### OUTPUT ##########################
Capitalize:  Coding for all
Title:  Coding For All
Swapcase:  cODING fOR aLL
'''

# 9.Cut(slice) out the first word of "Coding For All" string.
print("Coding For All".strip("Coding"))
''' 
####################### OUTPUT ##########################
 For All
'''

# 10. Check if "Coding For All" string contains a word 
# "Coding" using the method index, find or other methods.
print("Using index() method: ", "Coding For All".index("Coding"))
print("Using rindex() method: ", "Coding For All".rindex("Coding"))
print("Using find() method: ", "Coding For All".find('Coding'))
print("Using rfind() method: ", "Coding For All".rfind('Coding'))
print("Using startswith() method: ", "Coding For All".startswith('Coding'))
print("Using endswith() method: ", "Coding For All".endswith('Coding'))
''' 
####################### OUTPUT ##########################
Using index() method:  0
Using rindex() method:  0
Using find() method:  0
Using rfind() method:  0
Using startswith() method:  True
Using endswith() method:  False
'''

# 11. Replace the word coding in the string 'Coding For All' to Python.
print("Coding For All".replace("Coding", "Python"))
''' 
####################### OUTPUT ##########################
Python For All
'''

# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print("Using replace() method: ", "Python for Everyone".replace("Everyone", "All"))
print("Using strip() method and concatenate 'All': ", "Python for Everyone".strip("Everyone") + "All")
''' 
####################### OUTPUT ##########################
Using replace() method:  Python for All
Using strip() method and concatenate 'All':  Python for All
'''

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print("Coding For All".split(" "))
''' 
####################### OUTPUT ##########################
['Coding', 'For', 'All']
'''

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
str1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str1.split(","))
''' 
####################### OUTPUT ##########################
['Facebook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon']
'''

# 15. What is the character at index 0 in the string 'Coding For All'.
str2 = 'Coding For All'
print(str2[0])
''' 
####################### OUTPUT ##########################
C
'''

# 16. What is the last index of the string 'Coding For All'.
print(len(str2)-1)
''' 
####################### OUTPUT ##########################
13
'''

# 17. What character is at index 11 in "Coding For All" string.
print(str2[11]) 
''' 
####################### OUTPUT ##########################
A
'''

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
str3 = 'Python For Everyone'
def acronym(string):
    a = []
    for s in string:
        if s.isupper():
            a.append(s)    
    print("".join(a))

acronym(str3)
''' 
####################### OUTPUT ##########################
PFE
'''

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
acronym(str2)
''' 
####################### OUTPUT ##########################
CFA
'''

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(str2.index('C'))
''' 
####################### OUTPUT ##########################
0
'''

# 21. Use index to determine the position of the first occurrence of F in Coding For All. 
print(str2.index('F'))
''' 
####################### OUTPUT ##########################
7
'''

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rfind('l'))
''' 
####################### OUTPUT ##########################
19
'''

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the 
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
a = 'You cannot end a sentence with because because because is a conjunction'
print("Using index() method: ", a.index('because'))
print("Using find() method: ", a.find('because'))
''' 
####################### OUTPUT ##########################
Using index() method:  31
Using find() method:  31
'''

# 24. Use rindex to find the position of the last occurrence of the word 'because' in the following 
# sentence: 'You cannot end a sentence with because because because is a conjunction'
print("Using rindex() method: ", a.rindex('because'))
print("Using rfind() method: ", a.rfind('because'))
''' 
####################### OUTPUT ##########################
Using rindex() method:  47
Using rfind() method:  47
'''

# 25. Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(a.replace('because', ""))
''' 
####################### OUTPUT ##########################
You cannot end a sentence with    is a conjunction
'''

# 26. and 27. is repeated at 23. and 25.

# 28. Does 'Coding For All' start with a substring 'Coding'?
str2 = 'Coding For All'
sub_str = 'Coding'
print(str2.startswith(sub_str))
''' 
####################### OUTPUT ##########################
True
'''

# 29. Does 'Coding For All' end with a substring 'Coding'?
print(str2.endswith(sub_str))
''' 
####################### OUTPUT ##########################
False
'''

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
b = '   Coding For All      '
print(b.strip(" "))
''' 
####################### OUTPUT ##########################
Coding For All
'''

# 31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
''' 
####################### OUTPUT ##########################
False
True
'''

# 32. The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash and with space string.
l_str = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(l_str))
print(" ".join(l_str))
''' 
####################### OUTPUT ##########################
Django#Flask#Bottle#Pyramid#Falcon
Django Flask Bottle Pyramid Falcon
'''

# 33. Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")
''' 
####################### OUTPUT ##########################
I am enjoying this challenge.
I just wonder what is next.
'''

# 34. Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity")
print("Shreya\t27\tIndia\tPune")
''' 
####################### OUTPUT ##########################
Name    Age     Country City
Shreya  27      India   Pune
'''
# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("using old method: \nThe area of a circle with radius %d is %.2f meters square."%(radius, area))
print('Using f-string method:',f'\nThe area of a circle with radius {radius} is {area} meters square.')
print("Using format method: ","\nThe area of a circle with radius {} is {} meters square.".format(radius,area))
''' 
####################### OUTPUT ##########################
using old method:
The area of a circle with radius 10 is 314.00 meters square.
Using f-string method:
The area of a circle with radius 10 is 314.0 meters square.
Using format method:
The area of a circle with radius 10 is 314.0 meters square.
'''

# 36. Make the following using string formatting methods:
a = 8
b = 6
print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {}".format(a, b, a/b))
print("{} % {} = {}".format(a, b, a%b))
print("{} // {} = {}".format(a, b, a//b))
print("{} ** {} = {}".format(a, b, a**b))
''' 
####################### OUTPUT ##########################
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.3333333333333333
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
