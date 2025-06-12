from random import random, randint, randrange
import string
dir(string)
def random_user_id():
    print(randrange(1,6))

#random_user_id()

def rgb_color_gen():
    r,g,b = randint(0,256), randint(0,256), randint(0,256)
    print(f'rgb({r},{g},{b})')

#rgb_color_gen()