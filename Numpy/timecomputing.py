import sys
import numpy as np
# Create a list of 1000000 integers
list_1000000 = list(range(1000000))

# Create a NumPy array of 1000000 integers
array_1000000 = np.arange(1000000)

# Print the size of the list and the array in bytes

print(f"Size of list: {sys.getsizeof(list_1000000)} bytes")
print(f"Size of array: {array_1000000.nbytes} bytes")

# Time how long it takes to sum the list and the array
import time

# Sum the list
start_time = time.time()
sum_list = sum(list_1000000)
end_time = time.time()
list_sum_time = (end_time - start_time) * 1000

# Sum the array
start_time = time.time()
sum_array = np.sum(array_1000000)
end_time = time.time()
array_sum_time = (end_time - start_time) * 1000

# Print the time it took to sum the list and the array
print(f"Time to sum list: {list_sum_time:.2f} milliseconds")
print(f"Time to sum array: {array_sum_time:.2f} milliseconds")


















