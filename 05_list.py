# Day 5: 30 Days of python programming

# List

## Exercises: Level 1

# 1.Declare an empty list
#lst = []
lst = list()
print(lst)
''' 
####################### OUTPUT ##########################
[]
##########################################################
'''
# 2. Declare a list with more than 5 items
lst = ['Hey', 'Hi', 'Hello', 'Dear', 'Respected', 'Sincerely', 'Thanking']
print(lst)
''' 
####################### OUTPUT ##########################
['Hey', 'Hi', 'Hello', 'Dear', 'Respected', 'Sincerely', 'Thanking']
##########################################################
'''
# 3. Find the length of your list
len_lst = len(lst)
print(len_lst)
''' 
####################### OUTPUT ##########################
7
##########################################################
'''
# 4. Get the first item, the middle item and the last item of the list
first_item = lst[0]
last_item = lst[(len_lst-1)]
middle_item = lst[int(((len_lst)-1)/2)]
print("First item: ", first_item,
      "\nMiddle item: ", middle_item,
      "\nLast item: ", last_item)
''' 
####################### OUTPUT ##########################
First item:  Hey
Middle item:  Dear
Last item:  Thanking
##########################################################
'''
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address) 
mixed_data_types = ['Shreya', 'Parse', 27, 150, 'Unmarried', 'India']
print(mixed_data_types, "\n",type(mixed_data_types))
''' 
####################### OUTPUT ##########################
['Shreya', 'Parse', 27, 150, 'Unmarried', 'India'] 
 <class 'list'>
##########################################################
'''

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon. 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print(it_companies)
''' 
####################### OUTPUT ##########################
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
##########################################################
'''
# 8. Print the number of companies in the list
len_it = len(it_companies)
print("Number of IT Companies in list: ", len_it)
''' 
####################### OUTPUT ##########################
Number of IT Companies in list:  7
##########################################################
'''
# 9. Print the first, middle and last company
item_1 = it_companies[0]
item_last = it_companies[(len_it-1)]
item_middle = it_companies[(int((len_it-1)/2))]
print("First IT company: ", item_1,
      "\nMiddle IT Company: ", item_middle, 
      "\nLast IT Company: ", item_last) 
''' 
####################### OUTPUT ##########################
First IT company:  Facebook
Middle IT Company:  Apple
Last IT Company:  Amazon
##########################################################
'''
# 10. Print the list after modifying one of the companies
it_companies[6] = 'Samsung'
print(it_companies)
''' 
####################### OUTPUT ##########################
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Samsung']
##########################################################
'''
# 11. Add an IT company to it_companies
it_companies.append('Amazon')
print(it_companies)
''' 
####################### OUTPUT ##########################
['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Samsung', 'Amazon']
##########################################################
'''

# 12. Insert an IT company in the middle of the companies list
middle_index = int((len_it-1)/2)
it_companies.insert(middle_index, "LG") 
print(it_companies) 
''' 
####################### OUTPUT ##########################
'Facebook', 'Google', 'Microsoft', 'LG', 'Apple', 'IBM', 'Oracle', 'Samsung', 'Amazon']
##########################################################
'''
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())
''' 
####################### OUTPUT ##########################
FACEBOOK
##########################################################
'''
# 14. Join the it_companies with a string '#;  '
print("#".join(it_companies))
''' 
####################### OUTPUT ##########################
Facebook#Google#Microsoft#LG#Apple#IBM#Oracle#Samsung#Amazon
##########################################################
'''
# 15. Check if a certain company exists in the it_companies list.
print('LG' in it_companies)
''' 
####################### OUTPUT ##########################
True
##########################################################
'''
# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)
''' 
####################### OUTPUT ##########################
['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'LG', 'Microsoft', 'Oracle', 'Samsung']
##########################################################
'''
# 17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
''' 
####################### OUTPUT ##########################
['Samsung', 'Oracle', 'Microsoft', 'LG', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']
##########################################################
'''
# 18. Slice out the first 3 companies from the list
print(it_companies[:3])
''' 
####################### OUTPUT ##########################
['Samsung', 'Oracle', 'Microsoft']
##########################################################
'''
# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])
''' 
####################### OUTPUT ##########################
['Facebook', 'Apple', 'Amazon']
##########################################################
'''
# 20. Slice out the middle IT company or companies from the list
print(it_companies[middle_index])
''' 
####################### OUTPUT ##########################
LG
##########################################################
'''
# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
''' 
####################### OUTPUT ##########################
['Oracle', 'Microsoft', 'LG', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']
##########################################################
'''
# 22. Remove the middle IT company or companies from the list
i = it_companies[middle_index]
it_companies.remove(i)
print(it_companies)
''' 
####################### OUTPUT ##########################
['Oracle', 'Microsoft', 'LG', 'Google', 'Facebook', 'Apple', 'Amazon']
##########################################################
'''
# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)
''' 
####################### OUTPUT ##########################
['Oracle', 'Microsoft', 'LG', 'Google', 'Facebook', 'Apple']
##########################################################
'''
# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)
''' 
####################### OUTPUT ##########################
[]
##########################################################
'''
# 25. Destroy the IT companies list
del it_companies
print(it_companies)
''' 
####################### OUTPUT ##########################
NameError: name 'it_companies' is not defined
##########################################################
'''
#  26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print("Join using '+': ", front_end+back_end,
      "\nJoin using extend() method: ", front_end)
''' 
####################### OUTPUT ##########################
Join using '+':  ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB', 'Node', 'Express', 'MongoDB']
Join using extend() method:  ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
##########################################################
'''
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end + back_end
full_stack.extend(['Python', 'SQL'])
print(full_stack)
''' 
####################### OUTPUT ##########################
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB', 'Node', 'Express', 'MongoDB', 'Python', 'SQL']
##########################################################
'''

## Exercises: Level 2

# 1. The following is a list of 10 students ages, do as follows:
# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted list of ages: ", ages,
      "\nMax age: ", max_age,
      "\nMin age: ", min_age)
# Add the min age and the max age again to the list
ages.extend([min_age, max_age])
print("Added min and max to the list: ", ages)
# Find the median age (one middle item or two middle items divided by two)
middle_index = int((len(ages) - 1)/2)
median_age = ages[middle_index]/2
print("Median age: ", median_age)
# Find the average age (sum of all items divided by their number )
avg_age = sum(ages)/len(ages)
print("Average age: ", avg_age)
# Find the range of the ages (max minus min)
print("Range of ages: ", max_age-min_age)
# Compare the value of (min - average) and (max - average), use abs() method
print("Compare values: ", abs(min_age-avg_age)>abs(max_age-avg_age))
''' 
####################### OUTPUT ##########################
Sorted list of ages:  [19, 19, 20, 22, 24, 24, 24, 25, 25, 26] 
Max age:  26
Min age:  19
Added min and max to the list:  [19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]
Median age:  12.0
Average age:  22.75
Range of ages:  7
Compare values:  True
##########################################################
'''

# 2. Find the middle country(ies) in the countries list
read_file = {}
with open("countries.py", 'r') as country_file:
    exec(country_file.read(), read_file)

country_list = read_file.get('countries')
mid = int((len(country_list)-1)/2)
print("Middle Country: ", country_list[mid])
''' 
####################### OUTPUT ##########################
Middle Country:  Lesotho
##########################################################
'''
# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
country1 = country_list[:mid+1]
country2 = country_list[mid+1:]
print(len(country1), len(country2))
''' 
####################### OUTPUT ##########################
97 96
##########################################################
'''
# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
China, Russia, USA, *Scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(China, Russia, USA, Scandic_countries)
''' 
####################### OUTPUT ##########################
China Russia USA ['Finland', 'Sweden', 'Norway', 'Denmark']
##########################################################
'''