import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
multiplication=np.matmul(arr1,arr2)
print("Multiplication:\n",multiplication)

print("\nReshaping Matrices")
arr=np.arange(1,10)
print(arr)
print("shape is",arr.shape)
reshaped_arr=arr.reshape((3,3))
print(reshaped_arr)
print("Reshaped array shape:",reshaped_arr.shape)
print("Reshaped array size:",reshaped_arr.size)

print("\nAggregate Functions:")
matrix=np.array([[1,2,3],[4,5,6]])
print("Sum of all elements:",np.sum(matrix))
print("Max element:",np.max(matrix))
print("Min element:",np.min(matrix))
print("Mean of all elements:",np.mean(matrix))

#Universal functions
#Exponential and logarithmic functions
print("Exponential and logarithmic functions")
arr3=np.array([1,2,3,4,5])
result_exp=np.exp(arr)
print("Exponential:",result_exp)
result_log=np.log(arr)
print("Natural Logarithm:",result_log)

#Statistical Functions
print("\nStatistical Functions")
result_mean=np.mean(arr)
print("Mean:",result_mean)
result_std=np.std(arr)
print("Standard Deviation:",result_std)

print("\nComparison Functions:")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([2, 3, 3, 4, 4])
# Greater than
result_gt = np.greater(arr1, arr2)
print("Greater Than:", result_gt)
# Less than or equal to
result_lte = np.less_equal(arr1, arr2)
print("Less Than or Equal To:", result_lte)

#Broadcasting
arr=np.array([[1,2,3],[4,5,6]])
result_broadcast=arr+2
print("Broadcasting with Scalar:", result_broadcast)





