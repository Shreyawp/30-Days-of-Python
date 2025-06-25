import random

a = [1,2,3,4,5,6,7,8,9]
print(random.choice(a))

b = ('a', 56, "abc", 100, '87', 'python')
print(random.choices(b, k=3))

s = "Python for all"
print(random.choice(s))
''' 
####################### OUTPUT ##########################
9
['abc', '87', 'a']
o
##########################################################
'''

# seed() generates same random number on every run
print('*'*10, 'seed()','*'*10)
for i in range(2):
    random.seed(0)
    print(random.randint(1,10))

## reproduce same random list
random.seed()
print(random.sample(range(1,10),6))

## data splitting
x = list(range(100))
random.seed(10)
random.shuffle(a)
print(a)
''' 
####################### OUTPUT ##########################
********** seed() **********
7
7
[2, 8, 1, 7, 6, 4]
[6, 3, 8, 2, 9, 5, 4, 7, 1]
##########################################################
'''
# randint() to generate random integers
print('*'*10, 'randint()','*'*10)
print(random.randint(5,15))
print(random.randint(-12, -6))
''' 
####################### OUTPUT ##########################
********** randint() **********
9
-7
##########################################################
'''

# randrange(start,stop,step)
print('*'*10, 'randrange()','*'*10)
print('multiple of 3 between 1-51: ', random.randrange(1,51,3))

dice_roll = random.randrange(1,7)
print(f'dice roll: {dice_roll}')

z = [10, 80, 45, 35, 72, 56]
random_index = random.randrange(len(z))
print(z[random_index])
''' 
####################### OUTPUT ##########################
********** randrange() **********
multiple of 3 between 1-51:  16
dice roll: 1
72
##########################################################
'''
# getstate() returns an object with the current internal state 
print('*'*10, 'getstate() & setstate()','*'*10)
state = random.getstate()
print(random.sample(range(20), k=10))
#setstate() method is used to restore the state
random.setstate(state)
print(random.sample(range(20), k=5))
''' 
####################### OUTPUT ##########################
********** getstate() & setstate() **********
[5, 1, 16, 15, 10, 18, 3, 11, 19, 0]
[5, 1, 16, 15, 10]
##########################################################
'''

state1 = random.getstate()
num = random.random()
print("random number of captured state: ", num)
num2 =  random.random()
print("random number 2 of captured state: ", num2)
random.setstate(state1)
num3 = random.random()
print("random number of previously captured state: ", num3)
''' 
####################### OUTPUT ##########################
random number of captured state:  0.07608934678134815
random number 2 of captured state:  0.9523992311419316
random number of previously captured state:  0.07608934678134815
##########################################################
'''

# random() generates a float number in the range [0.0, 1.0]
print('*'*10, 'random()','*'*10)
from random import random
print(random())
lst = []
for i in range(10):
    lst.append(random())
print(lst)
''' 
####################### OUTPUT ##########################
********** random() **********
0.9523992311419316
[0.745546698544599, 0.3611586246233909, 0.4203962002706605, 0.138689276599814, 0.35508168773059534, 0.4212639948995278, 0.8268482288343075, 0.26232111049317675, 0.17467058960990223, 0.3031051133710616]
##########################################################
'''

# Select Multiple Unique Random Items w/o repeating
print('*'*10, 'sample()','*'*10)
from random import sample
print(sample(a,2))
print(sample(b,5))
print(sample(s,3))
''' 
####################### OUTPUT ##########################
********** sample() **********
[5, 8]
[100, 56, 'python', 'abc', '87']
['P', 'r', 'l']
##########################################################
'''

# Shuffle Elements in a List
print('*'*10, 'shuffle()','*'*10)
from random import shuffle
print("Before shuffle: ", a)
shuffle(a)
print("After shuffle: ", a)
''' 
####################### OUTPUT ##########################
Before shuffle:  [6, 3, 8, 2, 9, 5, 4, 7, 1]
After shuffle:  [1, 4, 6, 5, 9, 7, 3, 8, 2]
##########################################################
'''

# uniform(lower_bound, upper_bound) - generates random floating-point number
print('*'*10, 'uniform()','*'*10)
from random import uniform
print(uniform(1,5))

lat = uniform(-90, 90)
lon = uniform(-180, 180)
print(f"Random location: {lat}, {lon}")
''' 
####################### OUTPUT ##########################
********** uniform() **********
3.6667598053509645
Random location: -8.887859743195989, -10.809371893123512
##########################################################
'''
