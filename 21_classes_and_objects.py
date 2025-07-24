# Day 21: 30 Days of python programming

# create class
class Person:
    pass
print(Person)
# >> <class '__main__.Person'>

# Create object
p = Person()
print(p)
# >> <__main__.Person object at 0x0000021F0A16AEF0>

# class constructor using __init__() with self parameter
class Person:
    def __init__(self, name):
        self.name = name

p = Person('Shreya')
print(p.name)        
print(p)
####################### OUTPUT ##########################
# >> Shreya
# >> <__main__.Person object at 0x000001431E86BE80>
##########################################################

class Person:
    def __init__(self, fname, lname, age, country, city):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.country = country
        self.city = city

p = Person('Shreya', 'Parse', 26, 'India', 'Delhi')
print(p.fname)
print(p.lname)
print(p.age)
print(p.country)
print(p.city)
''' 
####################### OUTPUT ##########################
Shreya
Parse
26
India
Delhi
##########################################################
'''

# Object Methods
class Person:
    def __init__(self, fname, lname, age, country, city):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.fname} {self.lname} is {self.age} years old. She lives in {self.city}, {self.country}'
    
p = Person('Shreya', 'Parse', 26, 'India', 'Delhi')
print(p.person_info())
# >> Shreya Parse is 26 years old. She lives in Delhi, India

# Default values
class Person:
    def __init__(self, fname='Shreya', lname='Parse', age=26, country='India', city='Delhi'):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.fname} {self.lname} is {self.age} years old. She lives in {self.city}, {self.country}'
    
    def add_skill(self, skill):
        self.skills.append(skill)
    
p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')

p2 = Person('Jenny', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

print(p1.skills)
print(p2.skills)
''' 
####################### OUTPUT ##########################
Shreya Parse is 26 years old. She lives in Delhi, India
Jenny Doe is 30 years old. She lives in Noman city, Nomanland
['HTML', 'CSS', 'JavaScript']
[]
##########################################################
'''

## Inheritance
class Student(Person):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)
''' 
####################### OUTPUT ##########################
Eyob Yetayeh is 30 years old. She lives in Helsinki, Finland
['JavaScript', 'React', 'Python']
##########################################################
'''


print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
''' 
####################### OUTPUT ##########################
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland
['Organizing', 'Marketing', 'Digital Marketing']
##########################################################
'''

# Overriding parent method
class Student(Person):
    def __init__(self, fname='Shreya', lname='Parse', age=26, country='India', city='Delhi', gender='Female'):
        self.gender = gender
        super().__init__(fname, lname, age, country, city)
    
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.fname} {self.lname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)
''' 
####################### OUTPUT ##########################
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
##########################################################
'''

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
''' 
####################### OUTPUT ##########################
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
##########################################################
'''


## Exercise

# 1. create a class called Statistics and create all the functions that do 
# statistical calculations as methods for the Statistics class.
class Statistics:
    def __init__(self, num_list):
        self.num_list = num_list
    def count(self):
        return len(self.num_list)
    def sum(self):
        return sum(self.num_list)
    def min(self):
        return min(self.num_list)
    def max(self):
        return max(self.num_list)
    def range(self):
        return self.max() - self.min()
    def mean(self):
        mean = self.sum()/self.count()
        return round(mean)
    def median(self):
        mid_idx = int(self.count()/2)
        median = self.num_list[mid_idx]
        return median
    # def mode(self):
    #     return mode
    def variance(self):
        return sum((x - self.mean())**2 for x in self.num_list)/self.count()
    def standard_deviation(self):
        import math
        return math.sqrt(self.variance())
    def frequency_distribution(self):
        freq = {}
        for i in self.num_list:
            freq[i] = freq.get(i, 0) + 1
        return freq


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count: ', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
#print('Mode: ', data.mode())
print('Variance: ', data.variance())
print('Standard Deviation: %.2f' %data.standard_deviation())
print('Freqency Distribution: ', data.frequency_distribution())

''' 
####################### OUTPUT ##########################
Count:  25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  32
Variance:  17.6
Standard Deviation: 4.20
Freqency Distribution:  {31: 2, 26: 5, 34: 2, 37: 2, 27: 4, 32: 3, 24: 2, 33: 2, 25: 1, 38: 
1, 29: 1}
##########################################################
'''

# 2. Create a class called PersonAccount. It has firstname, lastname, 
# incomes, expenses properties and it has total_income, total_expense, 
# account_info, add_income, add_expense and account_balance methods. 
# Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.incomes = []
        self.expenses = []
    def total_income(self):
        sum = 0
        for item in self.incomes:            
            sum += item[1]
        return sum
    def total_expense(self):
        sum = 0
        for item in self.expenses:
            sum += item[1]
        return sum
    def account_info(self):
        str = f'Name: {self.f_name} {self.l_name}\n Total Income: {self.total_income()}\n Total Expense: {self.total_expense()}\n Account Balance: {self.account_balance()}'
        return str
    def add_income(self, income):
        return self.incomes.append(income)
    def add_expense(self, expense):
        return self.expenses.append(expense)
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
p1 = PersonAccount('John', 'Doe')
incomes = ('Salary', 5000), ('Freelance',1200)
expenses = [('Rent',1500), ('groceries', 400)]
for i in incomes:
    p1.add_income(i)
for e in expenses:
    p1.add_expense(e)

print('Total Income:', p1.total_income())
print('Total expense: ', p1.total_expense())
print('Account Balnce: ', p1.account_balance())
print('Account Info: \n', p1.account_info())
''' 
####################### OUTPUT ##########################
Total Income: 6200
Total expense:  1900
Account Balnce:  4300
Account Info:
 Name: John Doe
 Total Income: 6200
 Total Expense: 1900
 Account Balance: 4300
##########################################################
'''

