import numpy as np
import matplotlib.pyplot as plt
import cvxpy  as cp

#import sys, os
#sys.path.insert(0,'/home/krishna/Krishna/python/codes/CoordGeo')

#if using termux
import subprocess
import shlex
#Defining f(x)
def f(x,b):
#	return (b*(np.sin(2*x))+(c*np.sin(x)))
    return ((np.cos(x))+(np.cos(b*x)))
b = np.sqrt(2)
label_str = "$(np.cos(x))+(np.cos(b*x))`$"

#For minima using gradient ascent
cur_x = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
#df = lambda x: c*(np.cos(2*x)+np.cos(x))
df = lambda x: -b*((np.sin(b*x))-np.sin(x))

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

max_val = f(cur_x,b)
print("Maximum value of f(x) is ", max_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x,b)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,max_val,'o')
plt.text(cur_x, max_val,f'P({cur_x:.4f},{max_val:.4f})')


#if using termux
#plt.savefig('/home/krishna/Krishna/python/figs/opt.pdf')
#subprocess.run(shlex.split("termux-open /home/krishna/Krishna/python/figs/opt.pdf")
#else
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.show()
