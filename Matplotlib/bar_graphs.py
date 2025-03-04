import numpy as np
import matplotlib.pyplot as plt
categories=['Category A','Category B',' Category C']
values=[10,15,7]
plt.bar(categories,values)
plt.title("Basic Bar Graph")
plt.xlabel('Categories')
plt.ylabel("Values")
plt.savefig('basic bar graph.png')
plt.show()


print("Horizontal Bar graph")
plt.barh(categories,values,color='skyblue')
plt.title("Horizontal Bar Graph")
plt.xlabel('Values')
plt.ylabel('Categories')
plt.savefig("Horizontal Bar Graph.png")
plt.show()


#help statement
help(plt.bar)
print("#Diff Colored Graph")
categories=['Category A','Category B',' Category C']
values=[10,15,7]
plt.bar(categories,values,color=['red','green','blue'],edgecolor='black')
plt.title("Coloured Graph")
plt.xlabel('Categories')
plt.ylabel("Values")
plt.savefig('colored_graph.png')
plt.show()


print("#Stacked Graph")
categories=['Category A','Category B','Category C']
values1=[10,15,7]
values2=[5,3,2]
plt.bar(categories,values1,label='Part 1')
plt.bar(categories,values2,bottom=values1,label='Part 2')
plt.title("Stacked Graph")
plt.xlabel('Categories')
plt.ylabel("Values")
plt.savefig('stacked_graph.png')
plt.show()

categories=['Category A','Category B',' Category C']
values=[10,15,7]
errors=[1,2,1.5]
plt.bar(categories,values,yerr=errors,capsize=5) #capsize controls the error bar size
plt.title("Error Bars")
plt.xlabel('Categories')
plt.ylabel("Values")
plt.savefig('error_bars.png')
plt.show()
