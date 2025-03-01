import numpy as np
print("Transposing a Matrix")
arr_2d=np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
transposed_arr=arr_2d.T
print("Original Array:\n",arr_2d)
print("Transposed Array:\n",transposed_arr)

#Using transpose function
print()
print(arr_2d.transpose())

print("*****Swapping Axes*****")
swapped_arr=(transposed_arr.swapaxes(0,1)) #Rearranging rows and columns
print(swapped_arr)

arr3d=np.array([[[1,2,3],
               [4,5,6],
                [7,8,9]],
               [[10,11,12],
               [13,14,15],
               [16,17,18]]])
print(arr3d.size)
print(arr3d)
print(arr3d.swapaxes(0,2))

print("****Pseudo Random number Generator:****")
random_integers=np.random.randint(1,10,size=5)
print(random_integers)

random_normal=np.random.normal(size=3)
print(random_normal)

#for 2D Array
random_integers_2d=np.random.randint(1,10,size=(3,3))
print(random_integers_2d)

random_normal_2d=np.random.normal(size=(2,2))
print(random_normal_2d)











