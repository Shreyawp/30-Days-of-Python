# Day 8: 30 Days of python programming

## Dictionary

# Exercise

# 1. Create an empty dictionary called dog
dog = dict()  
# >> {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {'Name':'Jerry', 'Color':'Gold', 'Breed':'Shih Tzu', 'legs': 4, 'age (in months)':2}
print(dog)
''' 
####################### OUTPUT ##########################
{'Name': 'Jerry', 'Color': 'Gold', 'Breed': 'Shih Tzu', 'legs': 4, 'age (in months)': 2}
##########################################################
'''
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, 
# city and address as keys for the dictionary
Student = {'first_name': 'Shreya', 'last_name':'Parse',
           'gender' : 'Female', 'age' : 27, 'marital status':'unmarried',
           'skills':['Python','SQL','Analytical'], 'country':'India',
           'city':'Pune', 'Address':'galaxy'}
print(Student)
''' 
####################### OUTPUT ##########################
{'first_name': 'Shreya', 'last_name': 'Parse', 'gender': 'Female', 'age': 27, 'marital status': 'unmarried', 'skills': ['Python', 'SQL', 'Analytical'], 'country': 'India', 'city': 'Pune', 'Address': 'galaxy'}
##########################################################
'''
# 4. Get the length of the student dictionary
print(len(Student)) 
# >> 9

# 5. Get the value of skills and check the data type, it should be a list
print('Skills: ',Student['skills'],
      '\ndata type of skills key: ', type(Student['skills']))
''' 
####################### OUTPUT ##########################
Skills:  ['Python', 'SQL', 'Analytical']
data type of skills key:  <class 'list'>
##########################################################
'''
# 6. Modify the skills values by adding one or two skills
Student['skills'].append('Web Development')
print(Student)
''' 
####################### OUTPUT ##########################
{'first_name': 'Shreya', 'last_name': 'Parse', 'gender': 'Female', 'age': 27, 'marital status': 'unmarried', 'skills': ['Python', 'SQL', 'Analytical', 'Web Development'], 'country': 'India', 'city': 'Pune', 'Address': 'galaxy'}
##########################################################
'''
# 7. Get the dictionary keys as a list
print(Student.keys())
''' 
####################### OUTPUT ##########################
dict_keys(['first_name', 'last_name', 'gender', 'age', 'marital status', 'skills', 'country', 'city', 'Address'])
##########################################################
'''
# 8. Get the dictionary values as a list
print(Student.values())
''' 
####################### OUTPUT ##########################
dict_values(['Shreya', 'Parse', 'Female', 27, 'unmarried', ['Python', 'SQL', 'Analytical', 'Web Development'], 'India', 'Pune', 'galaxy'])
##########################################################
'''
# 9. Change the dictionary to a list of tuples using items() method
print(Student.items())
''' 
####################### OUTPUT ##########################
dict_items([('first_name', 'Shreya'), ('last_name', 'Parse'), ('gender', 'Female'), ('age', 27), ('marital status', 'unmarried'), ('skills', ['Python', 'SQL', 'Analytical', 'Web Development']), ('country', 'India'), ('city', 'Pune'), ('Address', 'galaxy')])
##########################################################
'''
# 10. Delete one of the items in the dictionary
Student.pop('Address')
print(Student)
''' 
####################### OUTPUT ##########################
{'first_name': 'Shreya', 'last_name': 'Parse', 'gender': 'Female', 'age': 27, 'marital status': 'unmarried', 'skills': ['Python', 'SQL', 'Analytical', 'Web Development'], 'country': 'India', 'city': 'Pune'}
##########################################################
'''
# 11. Delete one of the dictionaries
del Student
print(Student)
''' 
####################### OUTPUT ##########################
NameError: name 'Student' is not defined
##########################################################
'''