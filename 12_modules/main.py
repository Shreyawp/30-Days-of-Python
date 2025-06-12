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

# OS module
import os
cwd = os.getcwd()
print("Current wokring directory: ", cwd)
 
####################### OUTPUT ##########################
# Current wokring directory:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode
##########################################################

os.chdir('12_modules')                           #Change directory
print("Current wokring directory: ", os.getcwd()) 
####################### OUTPUT ##########################
# >> Current wokring directory:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode\12_modules
##########################################################

path = os.path.join(cwd, "dummy_dir")  
os.mkdir(path)         #Create new directory
print("Created new directory")
####################### OUTPUT ##########################
#>> Created new directory
##########################################################


