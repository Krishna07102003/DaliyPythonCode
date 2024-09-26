# 1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

# 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# 3. Write a NumPy program to create an array with values ranging from 12 to 38.

# 4. Write a NumPy program to convert a list and tuple into arrays. Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8] 
import numpy as np
zero=np.zeros((1,10))
print("array of 10 zeroes",zero)
#----------------------------------------
one=np.ones((1,10))
print("array of 10 ones",one)
#----------------------------------------
five=np.full(10,5)
print("array of 10 fives",five)
#  2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
arr=np.arange(2,11)
print(arr)
#Reshaping the array into 3x3 matrix
mat_arr=arr.reshape(3,3)
print(mat_arr)
#  3. Write a NumPy program to create an array with values ranging from 12 to 38.
arr=np.arange(12,39)
print(arr)
# 4. Write a NumPy program to convert a list and tuple into arrays. Input: my_list = [1, 2, 3, 4, 5, 6, 7, 8] 
#Convert list into Numpy arrays
my_list=[1, 2, 3, 4, 5, 6,7,8]
arr_list=np.array(my_list)
print(arr_list)
#Convert tuple into Numpy arrays
my_tuple = ([8, 4, 6], [1, 2, 3])
arr_tuple=np.array(my_tuple)
print(arr_tuple)