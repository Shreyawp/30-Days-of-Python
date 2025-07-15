# Day 18: 30 Days of python programming

# Regular Expressions
import re

## re.match(sunstring, string, re.I)
txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match)
# >> <re.Match object; span=(0, 15), match='I love to teach'>

span = match.span()
print(span)
# >> (0, 15)
start, end = span
print(start, end)
# >> 0 15
substring = txt[start:end]
print(substring)
# >> I love to teach

match1 = re.match('I like to teach', txt, re.I)
print(match1)
# >> None

## re.search(substring, string, re.I)
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search('first', txt, re.I)
print(match)
# >> <re.Match object; span=(100, 105), match='first'>
span = match.span()
print(span)
# >> (100, 105)
start, end = span
print(start, end)
# >> 100 105
substring = txt[start:end]
print(substring)
# >> first

## re.findall(sunstring, string, re.I) - list all matches
matches = re.findall('language', txt, re.I)
print(matches)
# >> ['language', 'language']

matches = re.findall('python', txt, re.I)
print(matches)
# >> ['Python', 'python']

matches = re.findall('Python|python', txt)
print(matches)
# >> ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)
# >> ['Python', 'python']

## re.sub(substr1, substr2, string, re.I) - replace string
# NOTE: only one case of 'Python' string is replaced
match_replaced = re.sub('Python', 'Javascript', txt, re.I)
print(match_replaced)
# >> Javascript is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language

match_replaced = re.sub('Python|python', 'Javascript', txt, re.I)
print(match_replaced)
# >> Javascript is the most beautiful language that a human being has ever created.
# I recommend Javascript for a first programming language

match_replaced = re.sub('[Pp]ython', 'Javascript', txt, re.I)
print(match_replaced)
# >> Javascript is the most beautiful language that a human being has ever created.
# I recommend Javascript for a first programming language

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
matches = re.sub('%', '', txt)
print(matches)
''' 
####################### OUTPUT ##########################
I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?
##########################################################
'''

## re.split(pattern_to_split, string) - split text to list
print(re.split('\n', matches))
''' 
####################### OUTPUT ##########################
['I am teacher and  I love teaching. ', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs. ', 'Does this motivate you to be a teacher?']
##########################################################
'''

## RegEx variable {r'' or r" "}
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)
# >> ['apple']

matches = re.findall(regex_pattern, txt, re.I)
print(matches)
# >> ['Apple', 'apple']

regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)
# >> ['Apple', 'apple']

regex_pattern = r'[Aa]pple|[Bb]anana'
matches = re.findall(regex_pattern, txt)
print(matches)
# >> ['Apple', 'banana', 'apple', 'banana']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
match = re.findall(r'\d', txt)
print(match)
# >> ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

matches = re.findall(r'\d+', txt)
print(matches)
# >> ['6', '2019', '8', '2021']

txt = '''Apple and banana are fruits'''
match = re.findall('[a].', txt)             # or (r'[a].', txt)
print(match)
# >>  ['an', 'an', 'an', 'a ', 'ar']

matches = re.findall('[a].+', txt)
print(matches)
# >> ['and banana are fruits']

match = re.findall(r'[a].*', txt)
print(match)
# >> ['and banana are fruits']

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
a = re.findall(r'[Ee]-?mail', txt)
print(a)
# >> ['e-mail', 'email', 'Email', 'E-mail']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
m = re.findall(r'\d{4}', txt)
print(m)
# >> ['2019', '2021']

m1 = re.findall(r'\d{1,4}', txt)
print(m1)
# >> ['6', '2019', '8', '2021']

m3 = re.findall('^This', txt)   # (^) starts with
print(m3)
# >> ['This']

reg_pat = r'[^a-zA-Z ]+'         # (^) here is negation
m4 = re.findall(reg_pat, txt)
print(m4)
# >> ['6,', '2019', '8,', '2021']

## Exercise

# 1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

def count_words(txt):
    words_dict = {}
    txt = txt.replace('.', '')
    for i in txt.lower().split(' '):
        if i in words_dict:
            words_dict[i] += 1
        else:
            words_dict[i] = 1
    return sorted(words_dict.items(), key=lambda x:x[1], reverse=True)
    
print(count_words(paragraph))
''' 
####################### OUTPUT ##########################
[('love', 6), ('you', 5), ('can', 3), ('i', 2), ('teaching', 2), ('if', 2), ('do', 2), ('not', 2), ('what', 2), ('else', 2), ('python', 1), ('something', 1), ('which', 1), ('give', 1), ('all', 1), ('the', 1), ('capabilities', 1), ('to', 1), ('develop', 1), ('an', 1), ('application', 1)]
##########################################################
'''

# 2. The position of some particles on the horizontal x-axis are 
# -12, -4, -3 and -1 in the negative direction, 0 at origin,
# 4 and 8 in the positive direction. Extract these numbers from
# this whole text and find the distance between the two furthest particles.

points = ['-12', '-4', '-3', '-1', '0', '4', '8']

def distance_between_particles(points):
    sorted_points = list(map(int,points))
    distance = sorted_points[-1] - sorted_points[0]
    print(distance)

distance_between_particles(points)
# >> 20


# 3. Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(var):
    valid_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    if re.fullmatch(valid_pattern, var):
        print(True)
    else: 
        print(False)


is_valid_variable('first_name')
is_valid_variable('first-name') 
is_valid_variable('1first_name') 
is_valid_variable('firstname') 
''' 
####################### OUTPUT ##########################
True
False
False
True
##########################################################
'''

# 4. Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_txt(txt):
    clean = re.sub(r'[^A-Za-z0-9\s]', '', txt)
    return clean

cleaned_txt = clean_txt(sentence)
def most_frequent_words(txt):
    word_dict = {}
    for word in txt.lower().split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return sorted(word_dict.items(), key=lambda x:x[1], reverse=True)[:3]

cleaned_txt = clean_txt(sentence)
print(cleaned_txt)
print(most_frequent_words(cleaned_txt))
''' 
####################### OUTPUT ##########################
I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
[('i', 3), ('a', 2), ('teacher', 2)]
##########################################################
'''

