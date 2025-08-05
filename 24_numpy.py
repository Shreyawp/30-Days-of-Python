import numpy as np

print('Numpy version: ', np.__version__)
# >> Numpy version:  2.2.6

#print(dir(np))

python_list = [1,2,3,4,5]
print(type(python_list))
# >> <class 'list'>
print(python_list)
# >> [1, 2, 3, 4, 5]

two_dimensional_list = [[0,1,2],[3,4,5],[6,7,8]]
print(type(two_dimensional_list))
# >> <class 'list'>
print(two_dimensional_list)
# >> [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

## Crete numpy from python_list
numpy_arr_from_pylist = np.array(python_list)
print(type(numpy_arr_from_pylist))
# >> <class 'numpy.ndarray'>
print(numpy_arr_from_pylist)
# >> [1 2 3 4 5]

## Create float numpy array
float_arr = np.array(python_list, dtype=float)
print(type(float_arr))
# >> <class 'numpy.ndarray'>
print(float_arr)
# >> [1. 2. 3. 4. 5.]

## Create boolean numpy array
bool_Arr = np.array([0,1,-1,0,0], dtype=bool)
print(type(bool_Arr))
# >> <class 'numpy.ndarray'>
print(bool_Arr)
# >> [False  True  True False False]

## Crete numpy from two_dimensional_list or say multi-dimensional
numpy_arr_from_2Dlist = np.array(two_dimensional_list)
print(type(numpy_arr_from_2Dlist))
# >> <class 'numpy.ndarray'>
print(numpy_arr_from_2Dlist)
# >> [[0 1 2]
#  [3 4 5]
#  [6 7 8]]


## convert numpy to list
np_to_list = numpy_arr_from_pylist.tolist()
print(type(np_to_list))
# >> <class 'list'>
print('1-D arr to list: ', np_to_list)
# >> 1-D arr to list:  [1, 2, 3, 4, 5]
print('2-D arr to list: ', numpy_arr_from_2Dlist.tolist())
# >> 2-D arr to list:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

## Tuple to numpy array
py_tup = (1,2,3,4,5)
print(type(py_tup))
# >> <class 'tuple'>
print(py_tup)
# >> (1, 2, 3, 4, 5)

arr_from_tup = np.array(py_tup)
print(type(arr_from_tup))
# >> <class 'numpy.ndarray'>
print(arr_from_tup)
# >> [1 2 3 4 5]

## arr.shape() - (rows, cols)
print('Shape of 1-D arr: ', numpy_arr_from_pylist.shape)
print('Shape of 2-D arr: ', numpy_arr_from_2Dlist.shape)
print('Shape of tup-to-arr: ', arr_from_tup.shape)
''' 
####################### OUTPUT ##########################
Shape of 1-D arr:  (5,)
Shape of 2-D arr:  (3, 3)
Shape of tup-to-arr:  (5,)
##########################################################
'''

## Data type of arr
print('Data type of 1-D: ', numpy_arr_from_pylist.dtype)
print('Data type of float arr: ', float_arr.dtype)
print('Data type of boolean arr: ',bool_Arr.dtype)
print('Data type of tup_arr: ', arr_from_tup.dtype) 
''' 
####################### OUTPUT ##########################
Data type of 1-D:  int64
Data type of float arr:  float64
Data type of boolean arr:  bool
Data type of tup_arr:  int64
##########################################################
'''

## arr.size
print('Size of 1-D: ', numpy_arr_from_pylist.size)
print('Size of 2-D: ', numpy_arr_from_2Dlist.size)
print('Size of float arr: ', float_arr.size)
print('Size of boolean arr: ',bool_Arr.size)
print('Size of tup_arr: ', arr_from_tup.size) 
''' 
####################### OUTPUT ##########################
Size of 1-D:  5
Size of 2-D:  9
Size of float arr:  5
Size of boolean arr:  5
Size of tup_arr:  5
##########################################################
'''

## Airthmetic Operations on array
add_10_to_1D_arr = numpy_arr_from_pylist + 10
print(add_10_to_1D_arr)
# >> [11 12 13 14 15]

subtract_10_from_1D = numpy_arr_from_pylist - 10
print(subtract_10_from_1D)
# >> [-9 -8 -7 -6 -5]

mul_10 = numpy_arr_from_pylist * 10
print(mul_10)
# >> [10 20 30 40 50]

div_10 = numpy_arr_from_pylist/10
print(div_10)
# >> [0.1 0.2 0.3 0.4 0.5]

modulus_of_3 = numpy_arr_from_pylist % 3
print(modulus_of_3)
# >> [1 2 0 1 2]

floor_div_3 = numpy_arr_from_pylist//3
print(floor_div_3)
# >> [0 0 1 1 1]

exponent_2 = numpy_arr_from_pylist**2
print(exponent_2)
# >> [ 1  4  9 16 25]

## Converting data types
arr_int_to_float = np.array(python_list, dtype='float')
print(arr_int_to_float)
# >> [1. 2. 3. 4. 5.]

arr_float_to_int = np.array(arr_int_to_float, dtype='int')
print(arr_float_to_int)
# >> [1 2 3 4 5]

arr_to_bool = np.array([-3,-2,-1,0,1,2,3], dtype='bool')
print(arr_to_bool)
# >> [ True  True  True False  True  True  True]

arr_int_to_str = np.array(python_list, dtype='str')
print(arr_int_to_str)
# >> ['1' '2' '3' '4' '5']


## Multi deimensional arrays
## getting items from array
two_D_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
first_row = two_D_arr[0]
sec_row = two_D_arr[1]
third_row = two_D_arr[2]
print('First row: ', first_row,
      '\nSecond row: ', sec_row,
      '\nthird row: ', third_row)

''' 
####################### OUTPUT ##########################
First row:  [1 2 3]
Second row:  [4 5 6]
third row:  [7 8 9]
##########################################################
'''

## Slicing array
first_2_rows_and_cols = two_D_arr[0:2, 0:2]
print(first_2_rows_and_cols)
''' 
####################### OUTPUT ##########################
[[1 2]
 [4 5]]
##########################################################
'''

## Reverse whole arr
print(two_D_arr[::])
''' 
####################### OUTPUT ##########################
[[1 2 3]
 [4 5 6]
 [7 8 9]]
##########################################################
'''

# Reverse rows and cols position
print(two_D_arr[::-1,::-1])
''' 
####################### OUTPUT ##########################
[[9 8 7]
 [6 5 4]
 [3 2 1]]
##########################################################
'''

# Change values 
two_D_arr[1,1] = 55
two_D_arr[1,2] = 44
print(two_D_arr)
''' 
####################### OUTPUT ##########################
[[ 1  2  3]
 [ 4 55 44]
 [ 7  8  9]]
##########################################################
'''

## arr of zeros
numpy_zeros = np.zeros((3,3), dtype=int, order='C')
print(numpy_zeros)
''' 
####################### OUTPUT ##########################
[[0 0 0]
 [0 0 0]
 [0 0 0]]
##########################################################
'''

## arr of ones
numpy_ones = np.ones((3,3), dtype=int, order='C')
print(numpy_ones)
''' 
####################### OUTPUT ##########################
[[1 1 1]
 [1 1 1]
 [1 1 1]]
##########################################################
'''

print(numpy_ones*2)
''' 
####################### OUTPUT ##########################
[[2 2 2]
 [2 2 2]
 [2 2 2]]
##########################################################
'''

## Reshape array
first_shape = np.array([[1,2,3],[4,5,6]])
print('First Shape: \n', first_shape)
''' 
####################### OUTPUT ##########################
First Shape:
 [[1 2 3]
 [4 5 6]]
##########################################################
'''

reshaped = first_shape.reshape(3,2)
print('reshaped: \n', reshaped)
''' 
####################### OUTPUT ##########################
reshaped:
 [[1 2]
 [3 4]
 [5 6]]
##########################################################
'''

## Flattening array
flattened = reshaped.flatten()
print(flattened)
''' 
####################### OUTPUT ##########################
[1 2 3 4 5 6]
##########################################################
'''

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

## Adding 2D arr
print('Sum : ', arr1 + arr2)
# >> Sum :  [5 7 9]

## Horizontal and Vertical stack 
#print('Horizontal Append: \n', np.hstack(arr1,arr2))

#print('Vertical Stack: \n', np.vstack(arr1,arr2))

## Generating random numbers
# np.random.normal(mu, sigma, size)
normal_arr = np.random.normal(79,15,80)
print(normal_arr)
''' 
####################### OUTPUT ##########################
[108.94308456  78.63531333  91.07106802  77.28699276  95.1065978
  70.77396539  82.96077411  21.06246419 ...] 
##########################################################
'''

## Ploting histogram/frequency table using normal arr
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
array, bin, patches = plt.hist(normal_arr, color='grey', bins=50)
print(array, bin, patches)
''' 
####################### OUTPUT ##########################
[1. 0. 0. 2. 0. 1. 0. 0. 2. 2. 3. 3. 0. 4. 4. 3. 1. 3. 6. 5. 5. 4. 4. 4.
 0. 4. 3. 2. 1. 1. 1. 1. 3. 2. 0. 0. 0. 0. 1. 0. 1. 0. 0. 1. 0. 0. 1. 0.
 0. 1.] [ 50.87005528  52.28052059  53.6909859   55.10145121  56.51191652
  57.92238183  59.33284714  60.74331245  62.15377775  63.56424306
  64.97470837  66.38517368  67.79563899  69.2061043   70.61656961
  72.02703492  73.43750023  74.84796553  76.25843084  77.66889615
  79.07936146  80.48982677  81.90029208  83.31075739  84.7212227
  86.13168801  87.54215331  88.95261862  90.36308393  91.77354924
  93.18401455  94.59447986  96.00494517  97.41541048  98.82587579
 100.2363411  101.6468064  103.05727171 104.46773702 105.87820233
 107.28866764 108.69913295 110.10959826 111.52006357 112.93052888
 114.34099418 115.75145949 117.1619248  118.57239011 119.98285542
 121.39332073] <BarContainer object of 50 artists>
##########################################################
'''


## Matrix in numpy
matrix_4x4 = np.matrix(np.ones((4,4), dtype=float))
print(matrix_4x4)
''' 
####################### OUTPUT ##########################
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
##########################################################
'''

np.asarray(matrix_4x4)[2] = 2
print(matrix_4x4)
''' 
####################### OUTPUT ##########################
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [2. 2. 2. 2.]
 [1. 1. 1. 1.]]
##########################################################
'''

## numpy.arange(strat, stop, step)
whole_num = np.arange(0,20,1)
print(whole_num)
# >> [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

natural_num = np.arange(1,20,1)
print(natural_num)
#  >> [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

odd_num = np.arange(1,20,2)
print(odd_num)
# >> [ 1  3  5  7  9 11 13 15 17 19]

even_num = np.arange(0,20,2)
print(even_num)
# >> [ 0  2  4  6  8 10 12 14 16 18]

## np.linspace(start, stop, num) -- creates num range of values between start and stop
print(np.linspace(1,5, num=10, endpoint=False))     #enpoint - excludes stop num
''' 
####################### OUTPUT ##########################
[1.  1.4 1.8 2.2 2.6 3.  3.4 3.8 4.2 4.6]
##########################################################
'''

## np.logspace(start, stop, num, endpoint) -- retuens value num range on log scale
print(np.logspace(2,4.0, num=4))
''' 
####################### OUTPUT ###############################
[  100.           464.15888336  2154.43469003 10000.        ]
##############################################################
'''

## generate array of complex values
complex_arr = np.array([1,2,3], dtype=np.complex128)
print(complex_arr)
# >> [1.+0.j 2.+0.j 3.+0.j]
print('Size of complex arr: ', complex_arr.itemsize)
# >> Size of complex arr:  16

## Array Indexing
np_list = np.array([(1,2,3),[4,5,6]])
print('First row: ',np_list[0],
      '\nSecond row: ', np_list[1])
''' 
####################### OUTPUT ##########################
First row:  [1 2 3]
Second row:  [4 5 6]
##########################################################
'''

## Array Slicing and indexing
print('First col: ', np_list[:,0],
        '\nSecond col: ', np_list[:,1],
        '\nThird col: ', np_list[:,2])

''' 
####################### OUTPUT ##########################
First col:  [1 4]
Second col:  [2 5]
Third col:  [3 6]
##########################################################
'''

## Numpy statistical functions
arr = np.array([(1,2,3),(4,5,6),(7,8,9)])

print(f'''min: {arr.min()} 
max: {arr.max()} 
mean: {arr.mean()}
median: {np.median(arr)}
Standard Deviation: {arr.std()}
Variance: {arr.var()}''')
''' 
####################### OUTPUT ##########################
min: 1 
max: 9
mean: 5.0
median: 5.0
Standard Deviation: 2.581988897471611
Variance: 6.666666666666667
##########################################################
'''

print(f'''{arr}
****** Column ******
Col with min: {np.amin(arr, axis=0)}
col with max: {np.amax(arr, axis=0)}
****** Row ******
row with min: {np.amin(arr, axis=1)}
row with max: {np.amax(arr, axis=1)}''')
''' 
####################### OUTPUT ##########################
[[1 2 3]
 [4 5 6]
 [7 8 9]]
****** Column ******
Col with min: [1 2 3]
col with max: [7 8 9]
****** Row ******
row with min: [1 4 7]
row with max: [3 6 9]
##########################################################
'''

## Create repeating sequence
a = [1,2,3]
print('Tile: ', np.tile(a,2))   
# >> Tile:  [1 2 3 1 2 3]
print('Repeat: ', np.repeat(a,2))
# >> Repeat:  [1 1 2 2 3 3]


## Generate random numbers with numpy
# numpy.random (like random module) generate values between (0,1)

print(np.random)
# >> <module 'numpy.random' from 'C:\\...Python310\\site-packages\\numpy\\random\\__init__.py'>

numpy_random_num = np.random.random()
print(numpy_random_num)
# >> 0.9682965305619128

r = np.random.random(size=[2,3])
print(r)
''' 
####################### OUTPUT ##########################
[[0.83023928 0.3318957  0.10053259]
 [0.47401456 0.31183716 0.677379  ]]
##########################################################
'''

choice = np.random.choice(['a','e','i','o','u'])
print(choice)
# >> a

choice = np.random.choice(['a','e','i','o','u'], size=10)
print(choice)
# >> ['i' 'i' 'a' 'u' 'o' 'i' 'u' 'e' 'i' 'o']

print(''.join(choice))
# >> ioaoiuioea

## np.random.rand() -- returns random number arr of shape (here, (2,2)) between values [0,1]
rand = np.random.rand(2,2)
print(rand)
''' 
####################### OUTPUT ##########################
[[0.6328717  0.26717209]
 [0.15310407 0.45992686]]
##########################################################
'''

randn = np.random.randn(2,2)
print(randn)
''' 
####################### OUTPUT ##########################
[[ 0.36318745 -0.93559664]
 [-1.74168478  0.41184456]]
##########################################################
'''

## np.random.randint(start, stop, size=(a,b)) -- returns random number arr of size (here, (5,3)) between values (start,stop) (here, (0,10))
rand_int = np.random.randint(0,10, size=[5,3])
print(rand_int)
''' 
####################### OUTPUT ##########################
[[9 2 7]
 [5 6 4]
 [8 6 5]
 [9 2 6]
 [0 2 8]]
##########################################################
'''

## Matrix algebra

# Dot product of 2 arrays
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a,b))
# >> 32

# matrix multiplication np.matmul(a,b)
print(np.matmul(a,b))
# >> 32

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print('x: \n', x, '\ny: \n', y)
print('matrix multiplication:\n',np.matmul(x,y))
''' 
####################### OUTPUT ##########################
x:
 [[1 2]
 [3 4]]
y:
 [[5 6]
 [7 8]]
matrix multiplication:
 [[19 22]
 [43 50]]
##########################################################
'''

## Determinant of 2*2 Matrix 
print('Determinant of x: ', np.linalg.det(x))
# >> Determinant of x:  -2.0000000000000004

print('Determinant of y: ', np.linalg.det(y))
# >> Determinant of y:  -2.000000000000005