import numpy as np
arr=np.arange(10)
print(arr)

arr1D=np.array([1,2,3,4,5])
print(arr1D)
print("Type of the array is:",arr1D.dtype)
print("size is",arr1D.size)

arr2D=np.array([[1,2,3],[4,5,6]])
print(arr2D)
print("Item size is",arr2D.itemsize)
print("size is",arr2D.size)
print("Shape of the array is:",arr2D.shape)
print("Type of the array is:",arr2D.dtype)


floatarr=np.array([1.22,3.44,5.66],dtype=np.float64)
print(floatarr)
print("Item size is",floatarr.itemsize)
print("Type of the floatarray is:",floatarr.dtype)
print("size is",floatarr.size)

floatarr2=np.array([1.22,3.44,5.66],dtype=np.int32) #removes decimal points
print(floatarr2)
print("Type of the array is:",floatarr2.dtype)
print("Item size is",floatarr2.itemsize)
print("size is",floatarr2.size)

arr3D=np.zeros([2,3,4])
print(arr3D)
print("Size is",arr3D.size)
print("Item size is",arr3D.itemsize)
print("Type of the array is:",arr3D.dtype)

arr4D=np.ones([2,3,4,5])
print(arr4D)
print("size is",arr4D.size)
print("Type of the array is:",arr4D.dtype)
print("Item size is",arr4D.itemsize)
print("Number of dimensions:",arr4D.ndim)

#More ABout specific data types
float_arr64=np.array([1.22,3.44,5.66],dtype=np.float64)
print("Type of the float_array64 is:",float_arr64.dtype)
print("Memory size of float_arr64:",float_arr64.itemsize*float_arr64.size)
    
Int_arr32=np.array([1,2,3],dtype=np.int32)
print("Type of the Int_array32 is:",Int_arr32.dtype)
print("Memory size of float_arr64:",Int_arr32.itemsize*Int_arr32.size)

print("Slicing is done")
print(arr1D[::])



