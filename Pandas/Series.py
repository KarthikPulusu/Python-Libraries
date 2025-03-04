import pandas as pd
import numpy as np
s=pd.Series([1,2,3,4,5])
print(s)
print(s.describe())
print("Mean:",s.mean())
print("std:",s.std())
print("Min:",s.min())
print("Max:",s.max())

print("Data Manipulation")
doubled=s.map(lambda x:x*2)
print("using Map:\n",doubled)

sqrt=s.apply(lambda x: x*0.5)
print("Using apply:\n",sqrt)

t=pd.Series([3,2,5,1,7])
sorted=t.sort_values()
print("Sorted:\n",sorted)

print("Dropping elements:")
dropped=t.drop(1)
print(dropped)

print("IS NULL:\n",t.isnull())
print("IS NOT NULL:\n",t.notnull())

null_values=pd.Series([1,2,3,None,4,np.nan])
print(null_values)
print("Is null with null values:\n",null_values.isnull())

print(null_values.fillna("default_value"))
print("Dropping Null:\n",null_values.dropna())

print("\nIndexing and Slicing and Filtering")
s=pd.Series([1,3,5,7,9])
print("s is\n",s)
print("First simple indexing first elements is",s[0])
print("using iloc First elements is",s.iloc[0])
print("Slicing:\n",s[0:4])

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("s is\n",s)
print(s.iloc[0])  # 10 gives first row element
print(s.loc['a'])#10 with custom index
print("Selecting multiple elements:\n",s.loc['b':'c'])
#print(s[0])    #Error as there no integer index
print(s[0:3])

print("Filtering")
filtered=s[s>12]
print("prints values more than 12",filtered)

print("\nAggregation:")
print("Sum is",s.sum())
print("Cumulative sum \n",s.cumsum())
aggregated=s.aggregate(["sum","mean","std"])
print("Functions using aggregate:\n",aggregated)









