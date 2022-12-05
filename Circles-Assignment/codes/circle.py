#To find the incenter of a circle

#Python libraries for math and graphics
import numpy as np
import math 
import matplotlib.pyplot as plt
from numpy import linalg as LA
import mpmath as mp
from numpy.linalg import norm

import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/Download/Matrix/CoordGeo')


#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
from sympy import symbols


#if using termux
import subprocess
import shlex
#end if
#Input parameters for given circle
V=np.array([[1,0],[0,1]])     
print('V=', V)
U=np.array([-2,3]).reshape(2,1)
print('U=', U)
f=9
print('f=',f)
x,y=symbols('x y')
X=np.array([x,y]).reshape(2,1)
C=X.T@V@X+2*U.T@X+f
print(C ,'=0')

O=(-LA.inv(V)@U)                #center of circle1
print('O=',O)

r1=mp.sqrt(norm(U)**2-f)        #radius of circle1
print(r1)

r4=np.array(r1)                 #radius to array

O3= np.array(([-2,3]))          #center to array

#Input parameters for locus of M
x,y=symbols('x y')
M=symbols('M')
x=M/2
y=(M+3)/2
X1=np.array([x,y]).reshape(2,1)
expr=X1.T@V@X1+2*U.T@X1+f
print(expr,'=0')
V=np.array([[1,0],  [0,1]])     
print('V=', V)
U=np.array([4,-3]).reshape(2,1)
print('U=', U)
f=9
print('f=',f)

O1=(-LA.inv(V)@U)                #center of circle2
print('O=',O1)

r2=mp.sqrt(norm(U)**2-f)         #radius of circle2
print(r2)

O2=np.array(([-4,3]))            #center to array

r5=np.array(r2)                  #radius to array

A = np.array(([0,3]))            #Given A point

B= np.array(([-2,1]))
M1= np.array(([-4,-1]))
M2= np.array(([-8,3]))
###Generating all circles
x_circ1 = circ_gen(O3,r4)
x_circ2 = circ_gen(O2,r5)

#generate the radius
x_OR = line_gen(O3,A)
plt.plot(x_OR[0,:],x_OR[1,:],label='$Radius$')
x_AM1 = line_gen(A,M1)
plt.plot(x_AM1[0,:],x_AM1[1,:],label='$Chord$', linestyle='dotted')
x_AM2 = line_gen(A,M2)
plt.plot(x_AM2[0,:],x_AM2[1,:],label='$Chord$', linestyle='dotted')

#plt.plot(line2_x ,line2_y, color='red', linewidth = 5, label = 'line2-dashed', linestyle='dotted')

##Plotting all lines
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$circle2$')


#Labeling the coordinates
tri_coords = np.vstack((O3,O2,A,B,M1,M2)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O_1','O_2','A','B','M$\_$1','M$\_$2']
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
plt.savefig('/sdcard/Download/Sreshta circles/circle.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/Sreshta circles/circle.pdf' "))
plt.show()
