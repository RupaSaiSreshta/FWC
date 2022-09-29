#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/FWC/matrices/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
f=3
d=-3
C = np.array(([0,0]))
e1=np.array(([1,0]))
e2=np.array(([0,1]))
D=d*e1
F=f*e1
theta =110* np.pi/180
a=6
A =a*np.array(([np.cos(theta),np.sin(theta)]))
B=A+F
ar_t1=0.5*np.linalg.norm((np.cross(A,F)))
ar_t2=0.5*np.linalg.norm((np.cross(A,B)))
E=np.array(([-5,3]))
v1=E-A
v2=E-D
v3=D-A
v4=D-C
ar3=0.5*np.linalg.norm((np.cross(v1,v2)))
ar4=0.5*np.linalg.norm((np.cross(v3,v4)))
area=ar3+ar4

print(ar_t1,ar_t2)
print(area+ar_t1,area+ar_t2)


##Generating all lines
x_CF = line_gen(C,F)
x_CA = line_gen(C,A)
x_BF = line_gen(B,F)
x_AB = line_gen(A,B)
x_CB = line_gen(C,B)
x_AF = line_gen(A,F)
x_DC = line_gen(D,C)
x_ED = line_gen(E,D)
x_EA = line_gen(E,A)

#Plotting all lines
plt.plot(x_CF[0,:],x_CF[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BF[0,:],x_BF[1,:])
plt.plot(x_CF[0,:],x_CF[1,:])
plt.plot(x_CB[0,:],x_CB[1,:])
plt.plot(x_AF[0,:],x_AF[1,:])
plt.plot(x_DC[0,:],x_DC[1,:])
plt.plot(x_ED[0,:],x_ED[1,:])
plt.plot(x_EA[0,:],x_EA[1,:])

#Labeling the coordinates
tri_coords = np.vstack((D,C,F,A,B,E)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['D','C','F','A','B','E']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/sdcard/FWC/matrices/matrix.pdf')
subprocess.run(shlex.split("termux-open  /sdcard/FWC/matrices/matrix.pdf"))
#else
#plt.show()
