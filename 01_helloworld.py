# Day 1 - 30DaysOfPython Challenge

def hello(s):
    print("Hello " + s)

#s = input("Enter Name: ")
hello("World")

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)
''' 
####################### OUTPUT ##########################
Hello World
5
2
6
1.5
9
1
1
'''

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
'''
####################### OUTPUT ##########################
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'set'>
<class 'tuple'>
'''

print(type(2))
print(type(9.8))
print(type(4+4j))
print(type(['SHreya', "Parse", 22]))
print(type('SHreya'))
print(type('Parse'))
print(type("India"))
'''
####################### OUTPUT ##########################
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'list'>
<class 'str'>
<class 'str'>
<class 'str'>
'''
# Euclidian Distance
def Euclidian_dist(x1,y1,x2,y2):
    print((x2-x1)**2 + (y2-y1)**2)

Euclidian_dist(2,3,10,8)
'''
####################### OUTPUT ##########################
89
'''
