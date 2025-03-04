import matplotlib.pyplot as plt
import numpy as np
print("Generating Linear Equation Graph")
x = np.linspace(start=-10, stop=10, num=200)
#print(x)
n=2
c=3
y=n*x+c
plt.plot(x,y,label='y=nx+c')
plt.title('Plot of the Linear graph')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.xlim(0,5)
plt.ylim(0,10)
plt.savefig('linear-quation.png')
plt.show()

print("Generating Quadatic Equation Graph")
x=np.linspace(start=-1,stop=7,num=200)
a=1
b=-4
c=4
y=a*x**2+b*x+c
plt.plot(x,y,label='y=x^2 - 4x + 4')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Plot of the Quadratic graph")
plt.xlim(-5,5)
plt.ylim(-5,10)
plt.grid(True)
plt.legend()
plt.savefig('quadratic-equation.png')
plt.show()

print("\nCreating a figure object:")
fig=plt.figure()
#Add axes to the figure(left,bottom,width,height)
ax=fig.add_axes([0.1,0.1,0.8,0.8])
plt.show()

x=np.linspace(0,10,100)
y=np.sin(x)
fig=plt.figure(figsize=(1,5)) #create a new fig with specific size
ax=fig.add_axes([0.1,0.1,0.85,0.85])
ax.plot(x,y,label='sin(x)',color='green')
ax.set_title('simple Plot of sin(x)')
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Amplitude')
plt.savefig('sin_wave.png')
plt.show()

x=np.linspace(0,10,100)
fig=plt.figure(figsize=(10,8))

axes_top=fig.add_axes([0.3,0.8,0.4,0.15])
axes_top.plot(x,2*x+1)
axes_top.set_title('Top plot: y=2x+1')

axes_center=fig.add_axes([0.3,0.3,0.4,0.4])
axes_center.plot(x,x+1)
axes_center.set_title('Center plot: y=x+1')

axes_left=fig.add_axes([0.05,0.3,0.2,0.4])
axes_left.plot(x,3*x+1)
axes_left.set_title('Left plot: y=3x+1')

axes_right=fig.add_axes([0.75,0.3,0.2,0.4])
axes_right.plot(x,0.5*x+1)
axes_right.set_title('Right plot: y=0.5*x+1')

axes_bottom=fig.add_axes([0.3,0.05,0.4,0.15])
axes_bottom.set_title('Bottom plot: y=-x+1')
axes_bottom.plot(x,-x+1)

axes_top_right=fig.add_axes([0.75,0.8,0.15,0.15])
axes_top_right.set_title('Top Right plot: y=4x+1')
axes_top_right.plot(x,4*x+1)
plt.savefig('plotting_axes.png')
plt.show()


print("Set of subplots")
fig,ax=plt.subplots()
ax.plot([1,2,3,4,5],[1,4,9,16,25],label='y=x^2')
ax.legend()
ax.set_title('Squares')
plt.show()

print("Adding rows and columns of subplots")
fig,axes=plt.subplots(2,2)
axes[0,0].plot([1,2,3,4,5],[1,4,9,16,25],label='sqaures')
axes[0,1].plot([1,2,3,4,5],[1,2,3,4,5],label='x=y')
axes[1,0].plot([1,2,3,4,5],[5,4,3,2,1],label='y=6-x')
axes[1,1].plot([1,2,3,4,5],[25,16,9,4,1],label='y=(6-x)^2')
axes[0,0].legend()
axes[0,0].set_title('Squares')
axes[0,1].set_title('proportional')
axes[1,0].set_title('Reverse')
axes[1,1].set_title('inverse squares')
plt.tight_layout()
plt.savefig('graph matrix_subplots.png')

plt.show()








        
