import numpy as np
print("Reshape")
a=np.arange(12)
print("Original:",a)
b=np.reshape(a,(3,4))
print("Reshaped:\n",b)

print("Resize")
a=np.arange(10)
c=np.resize(a,(4,3))
print(c)

a.resize(4,4)
print(a)
