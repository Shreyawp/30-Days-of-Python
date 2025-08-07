# Day 25: 30 Days of python programming

## PANDAS ##

import pandas as pd
import numpy as np

## Creating Pandas Series
nums  = [1,2,3,4,5]
s = pd.Series(nums)
print(s)
''' 
####################### OUTPUT ##########################
0    1
1    2
2    3
3    4
4    5
dtype: int64
##########################################################
'''

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1,2,3])
print(fruits)
''' 
####################### OUTPUT ##########################
1    Orange
2    Banana
3     Mango
dtype: object
##########################################################
'''

## Create Pandas Series using Dictionary
dct = {'name':'Shreya', 'country':'India', 'city':'Delhi'}
s = pd.Series(dct)
print(s)
''' 
####################### OUTPUT ##########################
name       Shreya
country     India
city        Delhi
dtype: object
##########################################################
'''

## Create constant Pandas Series
s = pd.Series(10, index=[1,2,3])
print(s)
''' 
####################### OUTPUT ##########################
1    10
2    10
3    10
dtype: int64
##########################################################
'''

## Create series using np.linspace()
s = pd.Series(np.linspace(5,20,10))
print(s)
''' 
####################### OUTPUT ##########################
0     5.000000
1     6.666667
2     8.333333
3    10.000000
4    11.666667
5    13.333333
6    15.000000
7    16.666667
8    18.333333
9    20.000000
dtype: float64
##########################################################
'''

## DataFrames

data = [
    ['Belly', 'FInland', 'Helsink'],
    ['Conrad', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]

df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)
''' 
####################### OUTPUT ##########################
    Names  Country       City
0   Belly  FInland    Helsink
1  Conrad       UK     London
2    John   Sweden  Stockholm
##########################################################
'''

## Create Dataframes using Dictionary
data = {
    'Name': ['Belly', 'Conrad', 'John'],
    'Country':['Finland', 'UK', 'Sweden'],
    'City':['Helsink', 'London', 'Stockholm']
}

df = pd.DataFrame(data)
print(df)
''' 
####################### OUTPUT ##########################
     Name  Country       City
0   Belly  Finland    Helsink
1  Conrad       UK     London
2    John   Sweden  Stockholm
##########################################################
'''

## Create df from List of Dictionaries
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}
]

df = pd.DataFrame(data)
print(df)
''' 
####################### OUTPUT ##########################
       Name  Country       City
0  Asabeneh  Finland   Helsinki
1     David       UK     London
2      John   Sweden  Stockholm
##########################################################
'''

## Create df from reading csv file
df = pd.read_csv('./data/weight-height.csv')
print(df)
''' 
####################### OUTPUT ##########################
      Gender     Height      Weight
0       Male  73.847017  241.893563
1       Male  68.781904  162.310473
2       Male  74.110105  212.740856
3       Male  71.730978  220.042470
4       Male  69.881796  206.349801
...      ...        ...         ...
9999  Female  61.944246  113.649103

[10000 rows x 3 columns]
##########################################################
'''

## Read first 5 rows
print(df.head())
''' 
####################### OUTPUT ##########################
  Gender     Height      Weight
0   Male  73.847017  241.893563
1   Male  68.781904  162.310473
2   Male  74.110105  212.740856
3   Male  71.730978  220.042470
4   Male  69.881796  206.349801
##########################################################
'''

## Last 5 rows of df
print(df.tail())
''' 
####################### OUTPUT ##########################
      Gender     Height      Weight
9995  Female  66.172652  136.777454
9996  Female  67.067155  170.867906
9997  Female  63.867992  128.475319
9998  Female  69.034243  163.852461
9999  Female  61.944246  113.649103
##########################################################
'''

## shape -- to know df (rows,cols)
print(df.shape)
# >> (10000, 3)

## columns -- return names of cols or col head
print(df.columns)
# >> Index(['Gender', 'Height', 'Weight'], dtype='object')

## Select specific col to get a series
Height = df['Height']
print(Height)
''' 
####################### OUTPUT ##########################
0       73.847017
1       68.781904
2       74.110105
3       71.730978
4       69.881796
          ...
9995    66.172652
9996    67.067155
9997    63.867992
9998    69.034243
9999    61.944246
Name: Height, Length: 10000, dtype: float64
##########################################################
'''

Weight = df['Weight']
print(Weight)
''' 
####################### OUTPUT ##########################
0       241.893563
1       162.310473
2       212.740856
3       220.042470
4       206.349801
           ...
9995    136.777454
9996    170.867906
9997    128.475319
9998    163.852461
9999    113.649103
Name: Weight, Length: 10000, dtype: float64
##########################################################
'''

print(len(Height) == len(Weight))
# >> True

print(Height.describe())
''' 
####################### OUTPUT ##########################
count    10000.000000
mean        66.367560
std          3.847528
min         54.263133
25%         63.505620
50%         66.318070
75%         69.174262
max         78.998742
Name: Height, dtype: float64
##########################################################
'''

print(Weight.describe())
''' 
####################### OUTPUT ##########################
count    10000.000000
mean       161.440357
std         32.108439
min         64.700127
25%        135.818051
50%        161.212928
75%        187.169525
max        269.989699
Name: Weight, dtype: float64
##########################################################
'''

print(df.describe())
''' 
####################### OUTPUT ##########################
             Height        Weight
count  10000.000000  10000.000000
mean      66.367560    161.440357
std        3.847528     32.108439
min       54.263133     64.700127
25%       63.505620    135.818051
50%       66.318070    161.212928
75%       69.174262    187.169525
max       78.998742    269.989699
##########################################################
'''

## Adding new column to df
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}
]

df = pd.DataFrame(data)

weights = [74, 78, 68]
df['weights'] = weights
print(df)
''' 
####################### OUTPUT ##########################
       Name  Country       City  weights
0  Asabeneh  Finland   Helsinki       74
1     David       UK     London       78
2      John   Sweden  Stockholm       68
##########################################################
'''

height = [173,175,160]
df['height'] = height
print(df)
''' 
####################### OUTPUT ##########################
       Name  Country       City  weights  height
0  Asabeneh  Finland   Helsinki       74     173
1     David       UK     London       78     175
2      John   Sweden  Stockholm       68     160
##########################################################
'''

## Calculate BMI
# Modify column values height cm -> ms
df['height'] = df['height'] * 0.01
print(df)
''' 
####################### OUTPUT ##########################
       Name  Country       City  weights  height
0  Asabeneh  Finland   Helsinki       74    1.73
1     David       UK     London       78    1.75
2      John   Sweden  Stockholm       68    1.60
##########################################################
'''

def calc_bmi():
    weights = df['weights']
    heights = df['height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h**2)
        bmi.append(b)
    return bmi

df['BMI'] = calc_bmi()
print(df)
''' 
####################### OUTPUT ##########################
       Name  Country       City  weights  height        BMI
0  Asabeneh  Finland   Helsinki       74    1.73  24.725183
1     David       UK     London       78    1.75  25.469388
2      John   Sweden  Stockholm       68    1.60  26.562500
##########################################################
'''

## Fromating df
df['BMI'] = round(df['BMI'], 1)
print(df)
''' 
####################### OUTPUT ##########################
       Name  Country       City  weights  height   BMI
0  Asabeneh  Finland   Helsinki       74    1.73  24.7
1     David       UK     London       78    1.75  25.5
2      John   Sweden  Stockholm       68    1.60  26.6
##########################################################
'''

birth_year = ['1769','1985','1990']
current_year = pd.Series(2025, index=[0,1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)
''' 
####################### OUTPUT ##########################
       Name  Country       City  weights  height   BMI Birth Year  Current Year
0  Asabeneh  Finland   Helsinki       74    1.73  24.7       1769          2025
1     David       UK     London       78    1.75  25.5       1985          2025
2      John   Sweden  Stockholm       68    1.60  26.6       1990          2025
##########################################################
'''

## Data types of col values
print(df.weights.dtype)
# >> int64

print(df['Birth Year'].dtype)
# >> object

## Change data type
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype)
# >> int64

df['Current Year'] = df['Current Year'].astype('int')
print(df['Current Year'].dtype)
# >> int64

ages = df['Current Year'] - df['Birth Year']
print(ages)
''' 
####################### OUTPUT ##########################
0    256
1     40
2     35
dtype: int64
##########################################################
'''

df['Age'] = ages
print(df)
''' 
####################### OUTPUT ##########################
       Name  Country       City  weights  height   BMI  Birth Year  Current Year  Age
0  Asabeneh  Finland   Helsinki       74    1.73  24.7        1769          2025  256      
1     David       UK     London       78    1.75  25.5        1985          2025   40      
2      John   Sweden  Stockholm       68    1.60  26.6        1990          2025   35    
##########################################################
'''

mean = (35 + 40)/2
print('Mean: ', mean)
# >> 

## Boolean Indexing -- use T/F mask to select rows or filter data
print(df[df['Age']>120])
''' 
####################### OUTPUT ##########################
       Name  Country      City  weights  height   BMI  Birth Year  Current Year  Age
0  Asabeneh  Finland  Helsinki       74    1.73  24.7        1769          2025  256 
##########################################################
'''

print(df[df['Age']<120])
''' 
####################### OUTPUT ##########################
    Name Country       City  weights  height   BMI  Birth Year  Current Year  Age
1  David      UK     London       78    1.75  25.5        1985          2025   40
2   John  Sweden  Stockholm       68    1.60  26.6        1990          2025   35
##########################################################
'''

df.loc[df['Age']>120, 'Age'] = round(mean)
print(df)
''' 
####################### OUTPUT ##########################
       Name  Country       City  weights  height   BMI  Birth Year  Current Year  Age
0  Asabeneh  Finland   Helsinki       74    1.73  24.7        1769          2025   38      
1     David       UK     London       78    1.75  25.5        1985          2025   40      
2      John   Sweden  Stockholm       68    1.60  26.6        1990          2025   35  
##########################################################
'''

## Exercise

# Read the hacker_news.csv file from data directory
df = pd.read_csv('./data/hacker_news.csv')

# Get the first five rows
print(df.head())
''' 
####################### OUTPUT ##########################
         id                                              title                                                url  num_points  num_comments      author       created_at
0  12224879                          Interactive Dynamic Video            http://www.interactivedynamicvideo.com/         386            52    ne0phyte   8/4/2016 11:52
1  11964716  Florida DJs May Face Felony for April Fools' W...  http://www.thewire.com/entertainment/2013/04/f...           2             1    vezycash  6/23/2016 22:20
2  11919867       Technology ventures: From Idea to Enterprise  https://www.amazon.com/Technology-Ventures-Ent...           3             1     hswarna   6/17/2016 0:01
3  10301696  Note by Note: The Making of Steinway L1037 (2007)  http://www.nytimes.com/2007/11/07/movies/07ste...           8             2  walterbell   9/30/2015 4:12
4  10482257  Title II kills investment? Comcast and other I...  http://arstechnica.com/business/2015/10/comcas...          53            22      Deinos  10/31/2015 9:48
##########################################################
'''

# Get the last five rows
print(df.tail())
''' 
####################### OUTPUT ##########################
             id                                              title                                                url  num_points  num_comments         author        created_at
20094  12379592  How Purism Avoids Intels Active Management Tec...  https://puri.sm/philosophy/how-purism-avoids-i...          10             6  AdmiralAsshat    8/29/2016 2:22
20095  10339284          YC Application Translated and Broken Down  https://medium.com/@zreitano/the-yc-applicatio...           4             1       zreitano   10/6/2015 14:57
20096  10824382  Microkernels are slow and Elvis didn't do no d...  http://blog.darknedgy.net/technology/2016/01/0...         169           132    vezzy-fnord     1/2/2016 0:49
20097  10739875                      How Product Hunt really works  https://medium.com/@benjiwheeler/how-product-h...         695           222          brw12  12/15/2015 19:32
20098  11680777  RoboBrowser: Your friendly neighborhood web sc...              https://github.com/jmcarp/robobrowser         182            58      pmoriarty    5/12/2016 1:43
##########################################################
'''

# Get the title column as pandas series
print(df.columns)
''' 
####################### OUTPUT ##########################
Index(['id', 'title', 'url', 'num_points', 'num_comments', 'author',
       'created_at'],
      dtype='object')
##########################################################
'''

# Count the number of rows and columns
print(df.shape)
# >> (20099, 7)

# Filter the titles which contain python
print(df[df['title'].apply(lambda title: 'python' in title.lower())])
''' 
####################### OUTPUT ##########################
             id                                              title                                                url  num_points  num_comments        author        created_at
102    10974870                From Python to Lua: Why We Switched  https://www.distelli.com/blog/using-lua-for-ou...         243           188      chase202   1/26/2016 18:17
103    11244541          Ubuntu 16.04 LTS to Ship Without Python 2  http://news.softpedia.com/news/ubuntu-16-04-lt...           2             1       _snydly    3/8/2016 10:39
144    10963528  Create a GUI Application Using Qt and Python i...                      http://digitalpeer.com/s/c63e          21             1        zoodle   1/24/2016 19:01
196    10716331  How I Solved GCHQ's Xmas Card with Python and ...  http://matthewearl.github.io/2015/12/10/gchq-x...           6             1          kipi  12/11/2015 10:38
436    11895088  Unikernel Power Comes to Java, Node.js, Go, an...  http://www.infoworld.com/article/3082051/open-...           3             1  syslandscape   6/13/2016 16:23
...         ...                                                ...                                                ...         ...           ...           ...               ...

[160 rows x 7 columns]
##########################################################
'''

# Filter the titles which contain JavaScript
print(df[df['title'].apply(lambda title:'javascript' in title.lower())])
''' 
####################### OUTPUT ##########################
            id                                              title                                                url  num_points  num_comments          author        created_at
267    12352636   Show HN: Hire JavaScript - Top JavaScript Talent                            https://www.hirejs.com/           1             1        eibrahim   8/24/2016 15:16
580    10871330  Python integration for the Duktape Javascript ...             https://pypi.python.org/pypi/pyduktape           3             1         stefano    1/9/2016 14:26
811    10741251  Ask HN: Are there any projects or compilers wh...                                                NaN           1             2         ggonweb  12/15/2015 23:26
1046   11343334  If you write JavaScript tools or libraries, bu...  https://medium.com/@Rich_Harris/how-to-not-bre...          48            19     callumlocke   3/23/2016 10:54
1093   10422726  Rollup.js: A next-generation JavaScript module...                                http://rollupjs.org          57            17         dmmalam   10/21/2015 0:02
...         ...                                                ...                                                ...         ...           ...             ...               ...

[170 rows x 7 columns]
##########################################################
'''

# Explore the data and make sense of it
print(df.describe())
''' 
####################### OUTPUT ##########################
                 id    num_points  num_comments
count  2.009900e+04  20099.000000  20099.000000
mean   1.131755e+07     50.296632     24.803025
std    6.964531e+05    107.110322     56.108639
min    1.017691e+07      1.000000      1.000000
25%    1.070172e+07      3.000000      1.000000
50%    1.128452e+07      9.000000      3.000000
75%    1.192613e+07     54.000000     21.000000
max    1.257898e+07   2553.000000   1733.000000
##########################################################
'''








