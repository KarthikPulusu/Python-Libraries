import numpy as np
#Indexing and slicing for 2D Arrays
arr_2d=np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
#Indexing for Middle element
print(arr_2d[1,1]) #5
#Negative Indexing
print(arr_2d[-2,-3])   #4

#print 2&3 rows
print(arr_2d[1:3,:],"\n")
#print 2&3 rows, 1&2 columns
print(arr_2d[1:3,:2])

#Omitted Indices
#for elements from sec row
print(arr_2d[1:])
print(arr_2d[:,0:1:2])

print("Boolean Indexing") #Retrieving ele based on Condition
arr_1d=np.array([1,2,3,4,5])
mask_arr=arr_1d>3
print(arr_1d[mask_arr])

print("Boolean Indexing For 2D Arrays") #Use above matrix
greaterthan5_2d=arr_2d>5
print(arr_2d[greaterthan5_2d])

print("Fancy Indexing")
indices=[0,2,4]
print(arr_1d[indices])

indices_2d=[[0,1],[1,2]] #Print 1st 2nd ,2nd 3rd rows
print(arr_2d[indices_2d])







