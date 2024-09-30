#How do you create a NumPy array?
# To create a numpy array first we used to import a numpy module then using array functions to create a numpy array.
import numpy as np
arr=np.array([12,23,34,45,64])
print("Created array",arr)
#How do you create a 2D array (matrix) in NumPy?		
# To create a 2D array in numpy we used array function with 2 dimensions with using multiple [] we can define array
arr1=np.array([[12,23,22],[2,43,32]])
print("2D array", arr1)
#How do you find the shape of an array?		
# To find the shape of an array we used to use shape function in numpy
arr_shape=np.array([12,23,34,45,64])
shapes=np.shape(arr_shape)
print("the shape of array is" ,shapes)
#How do you get the data type of a NumPy array?		
# To get the data type of a numpy array we used dtype function in numpy
arr=np.array([12,23,34,45,64])
arr1=np.array([12.0,2.3,3.4,0.45,6.4])
print("the datatype of array is", arr.dtype)
print("the datatype of array is", arr1.dtype)
#How do you slice a NumPy array?		
# To slice a numpy array we used to use slicing operator in numpy this slicing method is used to return the array using specified index
arr=np.array([12,23,34,45,64])
print(arr[:2])
print(arr[:-1])
#How do you add or subtract two NumPy arrays?		
# To add or subtract two numpy array we used to use + and -(arithematic operator) operator in numpy
arr=np.array([12,23,34,45,64])
add_arr=arr + 5
print("After adding 5 the array is", add_arr)
sub_arr=arr-5
print("After subtracting 5 the array is", sub_arr)
# How do you transpose a 2D NumPy array?		
# To transpose a 2D array we used the transpose function in numpy,this functions swaps the rows and columns elements
arr=np.array([[12,23,22],[2,43,32]])
t=np.transpose(arr)
print("After swapping rows into columns the array is", t)
#How do you flatten a NumPy array?		
# To flatten a numpy array we used to use flatten function in numpy,this function is used to converting a multi-dimensional array into one dimesnional
arr=np.array([[12,23,22],[2,43,32]])
flat_arr=arr.flatten()
print("After coverting the multi-dimensional array into one dimensional is", flat_arr)
#How do you perform element-wise multiplication in NumPy?			
# To perform element-wise multiplication in numpy we used to use * operator in numpy arrays 
arr=np.array([12,23,34,45,64])
multi=arr *2
print("After multiplying the array with 2 the array is", multi)
#How do you calculate the sum of elements in a NumPy array?			
# To calculate the sum of all elements we used sum functions to sum up the all elements in numpy array
arr=np.array([12,23,34,45,64])
print("Sum of all elements in array is", arr.sum())
#How do you create an array of evenly spaced values?			
# To create an array of evenly spaced values we used to use linspace function in numpy
arr=np.linspace(1,10,10)
print("Array of evenly spaced values is", arr)
#How do you create an array filled with zeros or ones?			
# To create an arra that filled with zeros and ones we used zeroes and ones functions, which returns the array which contain only zeros and ones
zero=np.zeros(5)
print("The array that conatins only zeros", zero)
one=np.ones(5)
print("the array that contains only ones is", one)
#Give a demonstartions of statistical operation on array			
#Statistical operations are Mean, Median, Mode, Variance, Standard deviation, Percentile
Stat_mean=np.array([12,23,34,45,23,64])
print("Mean of the array is", np.mean(Stat_mean))
print("Median of the array is", np.median(Stat_mean))
print("Mode of the array is", np.bincount(Stat_mean).argmax())
print("Variance of the array is", np.var(Stat_mean))
print("Standard deviation of the array is", np.std(Stat_mean))
print("Percentile of the array is", np.percentile(Stat_mean, 50))
#Why do we need statistical functions 		
#Statistical functions are used to calculate the mean, median, mode, variance, standard deviation,percentile of a equation pr array 
Stat_mean=np.array([12,23,34,45,23,64])
print("Mean of the array is", np.mean(Stat_mean))
print("Median of the array is", np.median(Stat_mean))
print("Mode of the array is", np.bincount(Stat_mean).argmax())
print("Variance of the array is", np.var(Stat_mean))
print("Standard deviation of the array is", np.std(Stat_mean))
print("Percentile of the array is", np.percentile(Stat_mean, 50))
#WAP  for variance, std deviation
arr=np.array([12,23,34,45,23,64])		
print("Variance of the array is", np.var(Stat_mean))
print("Standard deviation of the array is", np.std(Stat_mean))

# str1=np.array("Car","Bike","Bus")
# print(str1.dtype)