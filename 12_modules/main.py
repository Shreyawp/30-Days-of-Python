# Creating and calling new module 
import mymodule 
mymodule.gen_full_name('Shreya','Parse')

from mymodule import add_2_num, gravity as g
print(add_2_num(22, 6))

print(f'weight = {30 * g}')
''' 
####################### OUTPUT ##########################
Hello, Shreya Parse!
28
weight = 294.0
##########################################################
'''

# Some of the common built-in modules: 
# math, datetime, os,sys, random, statistics, collections, json,re