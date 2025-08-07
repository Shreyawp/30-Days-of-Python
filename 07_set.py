# Day 7: 30 Days of python programming

## Sets

## Exercises: Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set it_companies
print("Length of it_companies set: ", len(it_companies))
''' 
####################### OUTPUT ##########################
Length of it_companies set:  7
##########################################################
'''
# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
''' 
####################### OUTPUT ##########################
{'IBM', 'Google', 'Amazon', 'Microsoft', 'Facebook', 'Twitter', 'Oracle', 'Apple'}
##########################################################
'''
# 3. Insert multiple IT companies at once to the set it_companies
it_comp = {'Samsung', 'LG', 'Huawei', 'Sony'}
print("Added multiple companies using union(): ",it_companies.union(it_comp))
it_companies.update(it_comp)
print("Added multiple companies using update(): ",it_companies)
''' 
####################### OUTPUT ##########################
Added multiple companies using union():  {'Microsoft', 'Huawei', 'Apple', 'Amazon', 'IBM', 'Google', 'Oracle', 'LG', 'Samsung', 'Sony', 'Facebook', 'Twitter'}
Added multiple companies using update():  {'Huawei', 'Apple', 'Amazon', 'Oracle', 'IBM', 'Google', 'Microsoft', 'Samsung', 'Facebook', 'LG', 'Sony', 'Twitter'}
##########################################################
'''
# 4. Remove one of the companies from the set it_companies
it_companies.remove('LG')
#This will throw an error second time
#it_companies.remove('LG')   # KeyError: 'LG'
print("Removed company using remove(): ", it_companies)
''' 
####################### OUTPUT ##########################
Removed company using remove():  {'Huawei', 'Apple', 'Amazon', 'Oracle', 'IBM', 'Google', 'Microsoft', 'Samsung', 'Facebook', 'Sony', 'Twitter'}
##########################################################
'''
# 5. What is the difference between remove and discard
it_companies.discard('LG')
print("Remove company using discard(): ", it_companies)
''' 
####################### OUTPUT ##########################
Remove company using discard():  {'Huawei', 'Apple', 'Amazon', 'Oracle', 'IBM', 'Google', 'Microsoft', 'Samsung', 'Facebook', 'Twitter'}
##########################################################
Unlike remove(), discard() raise no error if item is not in set
'''

## Exercises: Level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B
print("Join A and B using union(): ",A.union(B))
# 2. Find A intersection B
print("A intersection B: ",A.intersection(B))
# 3. Is A subset of B
print("Is A subset of B: ",A.issubset(B))
# 4. Are A and B disjoint sets
print("Are A and B disjoint sets: ",A.isdisjoint(B))
# 5. Join A with B and B with A
print("Join A with B: ", A.union(B), 
      "\nJoin B with A: ", B.union(A))
# 6. What is the symmetric difference between A and B
print("symmetric difference between A and B: ",A.symmetric_difference(B))
# 7. Delete the sets completely
del A, B
#print(A, B)
''' 
####################### OUTPUT ##########################
Join A and B using union():  {19, 20, 22, 24, 25, 26, 27, 28}
A intersection B:  {19, 20, 22, 24, 25, 26}
Is A subset of B:  True
Are A and B disjoint sets:  False
Join A with B:  {19, 20, 22, 24, 25, 26, 27, 28}
Join B with A:  {19, 20, 22, 24, 25, 26, 27, 28}
symmetric difference between A and B:  {27, 28}
print(A, B) >> NameError: name 'A' is not defined
##########################################################
'''

## Exercises: Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print("Is list of age more than set: " , len(age) > len(age_set))
''' 
####################### OUTPUT ##########################
Is list of age more than set: True
##########################################################
'''
# 2. Explain the difference between the following data types: string, list, tuple and set
"""
String are characters quoted with single or double quotes.
List is collection of different data type objects. It is mutable. enclosed in []
Tuple is same as list containing order items but are immutable enclosed in ()
Set is collection of unique/distinct unordered items enclosed in {}
"""
# 3.  How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
string = 'I am a teacher and I love to inspire and teach people.'
str_set = set(string.split())
print("Set of unique words in given string: ", len(str_set))
print(str_set)
''' 
####################### OUTPUT ##########################
Set of unique words in given string:  10
{'and', 'teach', 'a', 'I', 'people.', 'to', 'love', 'teacher', 'am', 'inspire'}
##########################################################
'''