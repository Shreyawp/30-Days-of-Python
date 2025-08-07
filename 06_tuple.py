# Day 6: 30 Days of python programming

# Tuple

## Exercises: Level 1

# 1. Create an empty tuple
empty_tup = ()
print(empty_tup)
empty_tuple = tuple()
print(empty_tuple)
''' 
####################### OUTPUT ##########################
()
()
##########################################################
'''
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Ron', 'Percy', 'Fred', 'George', 'Bill', 'Charlie')
sister = ("Ginny",)         # single item tuple sufix ,
print("Brother: ", brothers,
      "\nSister: ", sister)
''' 
####################### OUTPUT ##########################
Brother:  ('Ron', 'Percy', 'Fred', 'George', 'Bill', 'Charlie')
Sister:  ('Ginny',)
##########################################################
'''
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers+sister
print("Siblings: ", siblings)
''' 
####################### OUTPUT ##########################
Siblings:  ('Ron', 'Percy', 'Fred', 'George', 'Bill', 'Charlie', 'Ginny')
##########################################################
'''
# 4. How many siblings do you have?
print("No. of Siblings: ", len(siblings))
''' 
####################### OUTPUT ##########################
No. of Siblings:  7
##########################################################
'''
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Arthur", 'Molly')
family_members = parents + siblings
print("Family member: ", family_members)
''' 
####################### OUTPUT ##########################
Family member:  ('Arthur', 'Molly', 'Ron', 'Percy', 'Fred', 'George', 'Bill', 'Charlie', 'Ginny')
##########################################################
'''

## Exercises: Level 2

# 1. Unpack siblings and parents from family_members
parents1 = family_members[:2]
siblings1 = family_members[2:]
print("After unpacking family members: ",
      "\nParents: ", parents1,
      '\nSiblings: ', siblings1)
''' 
####################### OUTPUT ##########################
After unpacking family members:
Parents:  ('Arthur', 'Molly')
Siblings:  ('Ron', 'Percy', 'Fred', 'George', 'Bill', 'Charlie', 'Ginny')
##########################################################
'''
# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Orange', 'Watermelon', 'Berries')
vegetables = ('Onion', 'Coriander', 'Cauliflower', 'French Beans', 'Eggplant', 'Cabbage', 'Lettuce')
animal_products = ('Milk', 'Cottage Cheese', 'Mozarella', 'Fish', 'Chicken', 'Oyester')
food_stuff_tp = fruits + vegetables + animal_products
print("Food List: ", food_stuff_tp)
''' 
####################### OUTPUT ##########################
Food List:  ('Apple', 'Orange', 'Watermelon', 'Berries', 'Onion', 'Coriander', 'Cauliflower', 
'French Beans', 'Eggplant', 'Cabbage', 'Lettuce', 'Milk', 'Cottage Cheese', 
'Mozarella', 'Fish', 'Chicken', 'Oyester')
##########################################################
'''
# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
print(type(food_stuff_tp))
food_stuff_list = list(food_stuff_tp)
print(type(food_stuff_list))
''' 
####################### OUTPUT ##########################
<class 'tuple'>
<class 'list'>
##########################################################
'''
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = int((len(food_stuff_tp)-1)/2)
print("Middle Item in food tuple: ", food_stuff_tp[middle_index])
''' 
####################### OUTPUT ##########################
Middle Item in food tuple:  Eggplant
##########################################################
'''
# 5. Slice out the first three items and the last three items from food_staff_lt list
print('First 3 items from food list: ', food_stuff_tp[:3],
      "\nLast 3 items: ", food_stuff_tp[-3:])
''' 
####################### OUTPUT ##########################
First 3 items from food list:  ('Apple', 'Orange', 'Watermelon')
Last 3 items:  ('Fish', 'Chicken', 'Oyester')
##########################################################
'''
# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp
print(food_stuff_tp)
''' 
####################### OUTPUT ##########################
NameError: name 'food_stuff_tp' is not defined. Did you mean: 'food_stuff_list'?
##########################################################
'''
# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)
#Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
''' 
####################### OUTPUT ##########################
False
True
##########################################################
'''