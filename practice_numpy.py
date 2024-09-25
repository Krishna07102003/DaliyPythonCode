import numpy as np
# 1. Convert the below list into numpy array then display the array

#  Input: my_list = [1, 2, 3, 4, 5] 

# 2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

#  Input: my_list = [1, 2, 3, 4, 5]
my_list = [1, 2, 3, 4, 5] 
np_array = np.array(my_list)
print("the list after converting into array is ",np_array)
#-------------------------------------------------------------
my_list = [1, 2, 3, 4, 5] 
np_array = np.array(my_list)
first_ind=(np_array[0])
print(f"the first index of array is",first_ind)
last_ind=(np_array[-1])
print(f"the last index of array is",last_ind)
mul_np=np_array*2
print("after multiplying by 2 the array is ",mul_np)